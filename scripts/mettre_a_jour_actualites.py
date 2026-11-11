#!/usr/bin/env python3
"""Mise à jour RSS de l'affiche TNI LearnWithDom.

Python standard library seulement, sans clé API.
Exécution manuelle : python scripts/mettre_a_jour_actualites.py
Flux manquant/inaccessible : conserve les dernières entrées disponibles.
"""
from __future__ import annotations

import email.utils
import html
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "actualites_sciences.json"
TODAY = datetime.now(timezone.utc).date()
FEEDS = {
    "Québec Science": "https://www.quebecscience.qc.ca/feed/",
    "New Scientist": "https://www.newscientist.com/feed/",
    "Scientific American": "https://www.scientificamerican.com/platform/syndication/rss/",
    "Nature": "https://www.nature.com/nature.rss",
    "Quanta Magazine": "https://www.quantamagazine.org/feed/",
    "Agence Science-Presse": "https://www.sciencepresse.qc.ca/rss.xml",
}
HOSTS = {
    "Québec Science": {"quebecscience.qc.ca", "www.quebecscience.qc.ca"},
    "New Scientist": {"newscientist.com", "www.newscientist.com"},
    "Scientific American": {"scientificamerican.com", "www.scientificamerican.com"},
    "Nature": {"nature.com", "www.nature.com"},
    "Quanta Magazine": {"quantamagazine.org", "www.quantamagazine.org"},
    "Agence Science-Presse": {"sciencepresse.qc.ca", "www.sciencepresse.qc.ca"},
}
XMLNS = {"atom": "http://www.w3.org/2005/Atom", "dc": "http://purl.org/dc/elements/1.1/"}


def node_text(node: ET.Element, *tags: str) -> str:
    for tag in tags:
        child = node.find(tag, XMLNS)
        if child is not None and child.text and child.text.strip():
            return re.sub(r"\s+", " ", html.unescape(child.text)).strip()
    return ""


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]*>", " ", text))).strip()


def normalize_date(raw: str) -> str:
    if not raw:
        return ""
    try:
        parsed = email.utils.parsedate_to_datetime(raw)
        if parsed:
            return parsed.date().isoformat()
    except (TypeError, ValueError, IndexError):
        pass
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return raw[:10] if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw[:10]) else ""


def topic_of(title: str) -> str:
    t = title.casefold()
    if re.search(r"math|math[ée]mat|calculus|algorithm|theorem|proof|équation|geometry|statistic|probab|number theory|combinatori|ferm[ae]t", t):
        return "Mathématiques"
    if re.search(r"quantum|physic|particle|galax|cosm|orbit|black hole|telescope|étoil|astronom|solar|moon|lunar|space|univers|sonde|voyager|planet|fusion|relativ|cern", t):
        return "Physique et espace"
    if re.search(r"chim|chem|molecule|cell|cellul|biolog|dna|genom|microb|protein|life|vie|alzheimer|lipid|brain|neuron", t):
        return "Biologie et chimie"
    if re.search(r"climat|climate|energy|énergie|renewable|electric|ia |\bai\b|machine learning|algorithmic|technolog|ocean|glac|environment", t):
        return "Technologies et environnement"
    return "Sciences"


def summary_for(topic: str) -> str:
    return {
        "Mathématiques": "Une nouvelle à explorer avec les outils de la logique et du raisonnement mathématique.",
        "Physique et espace": "Une actualité qui invite à questionner les lois physiques et la façon dont nous observons l’Univers.",
        "Biologie et chimie": "Une découverte à examiner à partir d’expériences, de modèles et de données scientifiques.",
        "Technologies et environnement": "Une actualité qui soulève des questions sur les technologies et leurs effets.",
        "Sciences": "Une actualité scientifique à lire, questionner et discuter en classe.",
    }[topic]


def normal_link(url: str, source: str) -> str | None:
    url = clean_text(url)
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    if parsed.scheme != "https" or parsed.hostname not in HOSTS[source]:
        return None
    # Retire les paramètres de suivi courants lorsque possible.
    return url


def entries_from_xml(xml: bytes, source: str) -> list[dict]:
    root = ET.fromstring(xml)
    records = root.findall("./channel/item")
    if not records:
        records = root.findall("./atom:entry", XMLNS)
    results: list[dict] = []
    seen = set()
    for record in records:
        title = clean_text(node_text(record, "title", "atom:title"))
        rawlink = node_text(record, "link")
        if not rawlink:
            for anchor in record.findall("atom:link", XMLNS):
                if anchor.attrib.get("rel", "alternate") == "alternate":
                    rawlink = anchor.attrib.get("href", "")
                    break
        if not rawlink:
            rawlink = node_text(record, "guid", "atom:id")
        url = normal_link(rawlink, source)
        pubdate = normalize_date(node_text(record, "pubDate", "dc:date", "atom:published", "atom:updated"))
        if not title or not url or url in seen or not pubdate:
            continue
        try:
            date_obj = date.fromisoformat(pubdate)
        except ValueError:
            continue
        if date_obj > TODAY + timedelta(days=1) or date_obj < TODAY - timedelta(days=50):
            continue
        topic = topic_of(title)
        results.append({"title": title[:220], "source": source, "url": url, "date": pubdate,
                        "topic": topic, "lang": "fr" if source in ("Québec Science", "Agence Science-Presse") else "en",
                        "summary": summary_for(topic)})
        seen.add(url)
    results.sort(key=lambda a: a["date"], reverse=True)
    return results[:12]


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "LearnWithDomClassroomFeed/1.0 (academic classroom project)",
                                                   "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*"})
    with urllib.request.urlopen(request, timeout=22) as response:
        data = response.read(1_800_000)
        if len(data) >= 1_800_000:
            raise ValueError("Flux trop volumineux")
        return data


def main() -> None:
    old = {"items": []}
    if OUTPUT.exists():
        try:
            old = json.loads(OUTPUT.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    old_items = old.get("items", [])
    all_items = []
    successes = 0
    for source, endpoint in FEEDS.items():
        try:
            fresh = entries_from_xml(fetch(endpoint), source)
            if not fresh:
                raise ValueError("Aucun article récent valide trouvé")
            print(f"{source}: {len(fresh)} articles récents")
            all_items.extend(fresh)
            successes += 1
        except Exception as exc:
            print(f"{source}: non disponible ({str(exc)[:160]}). Conservation des anciens articles.")
            all_items.extend(x for x in old_items if x.get("source") == source)
    # Les autres sources non gérées automatiquement (ex. NASA) restent disponibles dans le réservoir.
    all_items.extend(x for x in old_items if x.get("source") not in FEEDS)
    by_url = {}
    for item in all_items:
        if isinstance(item, dict) and item.get("url") and item.get("title"):
            by_url[item["url"]] = item
    items = sorted(by_url.values(), key=lambda x: (x.get("date", ""), x.get("source", "")), reverse=True)
    if not items:
        print("Aucune donnée accessible, fichier précédent conservé")
        return
    # N'afficher une date d'actualisation nouvelle que si une source a effectivement répondu.
    generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds") if successes else old.get("generated_at")
    result = {"generated_at": generated_at, "items": items[:100]}
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != serialized:
        OUTPUT.write_text(serialized, encoding="utf-8")
    print(f"Total: {len(items)} articles, {successes}/{len(FEEDS)} sources mises à jour")


if __name__ == "__main__":
    main()

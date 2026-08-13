---
title: "Notes de cours"
layout: default
---

<style>
body {
  font-family: "Nunito Sans", sans-serif !important;
  background-color: #fffaf0;
}

/* Main page container */
.notes-home {
  max-width: 1100px;
  margin: 0 auto;
}

/* Main introduction */
.hero {
  background: #fff3cd;
  border-left: 7px solid #f4b400;
  border-radius: 12px;
  padding: 35px 40px;
  margin: 30px 0 45px 0;
}

.hero h1 {
  margin-top: 0;
  color: #1e4fb8;
  font-size: 2.3em;
}

.hero p {
  font-size: 1.1em;
  line-height: 1.7;
}

/* Course grid */
.course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
  margin: 25px 0 45px 0;
}

/* Course cards */
.course-card {
  background: #ffffff;
  border: 1px solid #d9e7f7;
  border-top: 6px solid #2f6fed;
  border-radius: 10px;
  padding: 25px;
  box-shadow: 0 3px 10px rgba(0,0,0,0.06);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.course-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 18px rgba(0,0,0,0.10);
}

.course-card h2 {
  color: #1e4fb8;
  margin-top: 0;
}

.course-card p {
  line-height: 1.6;
}

.course-card ul {
  line-height: 1.7;
}

/* Links */
.course-link {
  display: inline-block;
  margin-top: 10px;
  padding: 9px 16px;
  background: #2f6fed;
  color: white !important;
  text-decoration: none;
  border-radius: 6px;
}

.course-link:hover {
  background: #1e4fb8;
}

/* About section */
.about {
  background: #f3f7ff;
  border-left: 5px solid #2f6fed;
  border-radius: 8px;
  padding: 25px 30px;
  margin: 30px 0;
}

.about h2 {
  margin-top: 0;
  color: #1e4fb8;
}

/* Mobile */
@media (max-width: 700px) {
  .hero {
    padding: 25px;
  }

  .hero h1 {
    font-size: 1.8em;
  }

  .course-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="notes-home">

<div class="hero">

<h1>Notes de cours</h1>

<p>
Bienvenue dans mes notes de cours de mathématiques.
</p>

<p>
Cette section rassemble des notes, des explications, des exemples et des
représentations visuelles conçus pour accompagner l'apprentissage des
mathématiques.
</p>

<p>
L'objectif n'est pas seulement de mémoriser des procédures, mais de
<strong>comprendre les mathématiques et le raisonnement qui se trouve derrière elles.</strong>
</p>

</div>

## Cours

<div class="course-grid">

<div class="course-card">

<h2>MAT1101</h2>

<h3>Arithmétique appliquée aux finances</h3>

<p>
Notions fondamentales d'arithmétique et applications aux situations de la
vie quotidienne.
</p>

<ul>
<li>Nombres entiers</li>
<li>Opérations arithmétiques</li>
<li>Nombres décimaux</li>
<li>Fractions</li>
<li>Nombres rationnels</li>
<li>Proportions et pourcentages</li>
<li>Applications financières</li>
</ul>

<a class="course-link" href="nombre-rationnel/">
Voir le cours →
</a>

</div>

<div class="course-card">

<h2>MAT1102</h2>

<h3>Statistiques et probabilités</h3>

<p>
Introduction aux concepts fondamentaux des statistiques et des probabilités.
</p>

<ul>
<li>Population et échantillon</li>
<li>Échantillonnage</li>
<li>Biais</li>
<li>Fréquences</li>
<li>Moyenne et mode</li>
<li>Étendue</li>
<li>Probabilités</li>
</ul>

<a class="course-link" href="#">
Voir le cours →
</a>

</div>

<div class="course-card">

<h2>MAT2101</h2>

<h3>Mathématiques</h3>

<p>
Notes et ressources consacrées aux notions mathématiques plus avancées.
</p>

<ul>
<li>Notation exponentielle</li>
<li>Puissances</li>
<li>Racines carrées</li>
<li>Racines cubiques</li>
<li>Expressions algébriques</li>
<li>Fonctions</li>
</ul>

<a class="course-link" href="#">
Voir le cours →
</a>

</div>

</div>

<div class="about">

<h2>Une façon différente d'apprendre les mathématiques</h2>

<p>
Les mathématiques ne sont pas seulement une collection de règles à mémoriser.
Derrière chaque formule se trouve une idée.
</p>

<p>
Pourquoi une fraction représente-t-elle une division?
Pourquoi ne peut-on pas diviser par zéro?
Pourquoi les fractions équivalentes représentent-elles la même quantité?
Pourquoi les statistiques utilisent-elles des échantillons?
</p>

<p>
Ces notes cherchent à répondre à ce genre de questions et à montrer
<strong>le raisonnement qui se trouve derrière les mathématiques.</strong>
</p>

</div>

</div>

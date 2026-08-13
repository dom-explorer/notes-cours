---
title: "MAT1101 — Introduction aux fractions"
layout: default
---

<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap" rel="stylesheet">

<style>
body {
  font-family: "Nunito Sans", sans-serif !important;
  background-color: #fffaf0;
}

.def-box {
  background: #f3f7ff;
}

.tip-box {
  background: #fff3cd;
}

.result-box {
  background: #eef8f1;
}
.def-box {
  background: #eef5fc;
  border-left: 5px solid #2f6fed;
  border-radius: 6px;
  padding: 14px 20px;
  margin: 20px 0;
}
.def-title {
  font-weight: 700;
  font-size: 1.15em;
  margin-bottom: 12px;
  color: #1e4fb8;
}

.def-box {
  line-height: 1.6;
}

.def-box p {
  margin: 10px 0;
}

.def-box mjx-container[display="true"] {
  margin: 18px 0 !important;
}
.tip-box {
  background: #fff8e1;
  border-left: 5px solid #f4b400;
  border-radius: 6px;
  padding: 14px 20px;
  margin: 20px 0;
}
.result-box {
  background: #e6f7ee;
  border-left: 5px solid #2ecc71;
  border-radius: 6px;
  padding: 14px 20px;
  margin: 20px 0;
}
h1 { color: #2f6fed; }
h2 { color: #2f6fed; border-bottom: 2px solid #cfe0fb; padding-bottom: 4px; }
h3 { color: #1e4fb8; }

.fraction-visual {
  margin: 25px auto;
  padding: 20px;
  background: #f8fbff;
  border-radius: 10px;
  border: 1px solid #d9e7f7;
  text-align: center;
}
.fraction-visual-title {
  font-weight: bold;
  margin-bottom: 15px;
  color: #1e4fb8;
}
.rectangle-fraction {
  display: flex;
  max-width: 500px;
  height: 80px;
  margin: 15px auto;
  border: 3px solid #333;
  border-radius: 6px;
  overflow: hidden;
}
.rectangle-fraction .part {
  flex: 1;
  border-right: 1px solid #333;
  background: #fff;
}
.rectangle-fraction .part:last-child {
  border-right: none;
}
.rectangle-fraction .filled {
  background: #f4b400;
}
.pizza {
  width: 180px;
  height: 180px;
  margin: 20px auto;
  border-radius: 50%;
  border: 4px solid #333;
  background: conic-gradient(
    #f4b400 0deg 270deg,
    #fff 270deg 360deg
  );
  position: relative;
}
.pizza-fourths {
  background: conic-gradient(
    #f4b400 0deg 90deg,
    #fff 90deg 180deg,
    #f4b400 180deg 270deg,
    #fff 270deg 360deg
  );
}
.pizza-sixths {
  background: conic-gradient(
    #f4b400 0deg 60deg,
    #fff 60deg 120deg,
    #f4b400 120deg 180deg,
    #fff 180deg 240deg,
    #f4b400 240deg 300deg,
    #fff 300deg 360deg
  );
}
.pizza-eighths {
  background: conic-gradient(
    #f4b400 0deg 45deg,
    #fff 45deg 90deg,
    #f4b400 90deg 135deg,
    #fff 135deg 180deg,
    #f4b400 180deg 225deg,
    #fff 225deg 270deg,
    #f4b400 270deg 315deg,
    #fff 315deg 360deg
  );
}
.visual-caption {
  margin-top: 10px;
  font-size: 1.05em;
}
.visual-comparison {
  display: flex;
  justify-content: center;
  gap: 40px;
  flex-wrap: wrap;
}
.visual-item {
  min-width: 180px;
  text-align: center;
}
@media (max-width: 600px) {
  .rectangle-fraction {
    height: 60px;
  }
  .pizza {
    width: 140px;
    height: 140px;
  }
  .visual-comparison {
    gap: 20px;
  }
}
</style>

#  MAT1101 — Les fractions

##  Table des matières

1. [Les fractions — pourquoi est-ce qu'on en a besoin? ](#les-fractions--pourquoi-est-ce-quon-en-a-besoin)
2. [Un petit voyage dans l'histoire ](#un-petit-voyage-dans-lhistoire)
3. [Les mathématiques de la Mésopotamie ](#les-mathématiques-de-la-mésopotamie)
4. [Pourquoi est-ce encore important aujourd'hui? ](#pourquoi-est-ce-encore-important-aujourdhui)
5. [Qu'est-ce qu'une fraction? ](#quest-ce-quune-fraction)
6. [Une fraction, c'est aussi une division ](#une-fraction-cest-aussi-une-division)
7. [Les différents types de fractions ](#les-différents-types-de-fractions)
8. [Les fractions équivalentes ](#les-fractions-équivalentes)
9. [Les fractions irréductibles ](#les-fractions-irréductibles)
10. [Pourquoi garder les fractions plutôt que toujours utiliser les décimales? ](#pourquoi-garder-les-fractions-plutôt-que-toujours-utiliser-les-décimales)
11. [Et pourquoi est-ce qu'on ne peut pas diviser par zéro? ](#et-pourquoi-est-ce-quon-ne-peut-pas-diviser-par-zéro)
12. [Et maintenant? ](#et-maintenant)

---

## Les fractions — pourquoi est-ce qu'on en a besoin? 

Avant de commencer à parler de fractions, j'aimerais qu'on se pose une question toute simple : pourquoi est-ce qu'on a inventé les fractions?

Imaginez une situation assez concrète. Vous avez un beau vase en céramique. Par malchance, vous l'accrochez et il tombe par terre. Il se brise en 1000 morceaux. Si vous voulez maintenant réparer le vase et le remettre dans son état original, vous allez devoir travailler avec tous ces petits morceaux. Le vase était un tout, mais maintenant il est séparé en plusieurs parties.

C'est un peu ça, l'idée derrière les fractions : prendre un tout et être capable de parler des différentes parties qui le composent.

On peut prendre un autre exemple, encore plus simple :

Vous allez au restaurant avec 4 amis et vous commandez une pizza . La pizza complète représente un tout. Mais vous voulez la partager entre vous. Vous allez donc la couper en plusieurs parties pour que chacun puisse en manger une partie.

Mais les fractions ne servent pas seulement à partager une pizza!

Depuis très longtemps, les humains ont eu besoin de représenter des parties d'un tout. On avait besoin de partager de la nourriture, de mesurer des quantités, de faire du commerce, de calculer des impôts ou des taxes, de mesurer des terrains et même de mesurer le temps.

En fait, les fractions sont apparues très tôt dans l'histoire des mathématiques parce que les humains avaient besoin de quantifier le monde qui les entourait.

## Un petit voyage dans l'histoire 

Si on retourne aux premières grandes civilisations, on retrouve déjà des façons de représenter les fractions. On peut notamment penser aux Égyptiens, aux civilisations de la vallée de l'Indus et aux civilisations de Mésopotamie.

Les Égyptiens utilisaient déjà des fractions il y a plusieurs milliers d'années. Leur façon de les représenter était cependant assez différente de la nôtre. Ils travaillaient surtout avec des fractions dites unitaires, c'est-à-dire des fractions dont le numérateur était 1.

Par exemple, pour représenter $\frac{1}{5}$, ils avaient leur propre système de symboles.

>  **Figure : Hiéroglyphe représentant 1/5**
> *<img width="90" height="94" alt="image" src="https://github.com/user-attachments/assets/76b2ea71-7dee-4963-828f-81b6d82a81d7" />*

Ça fonctionnait, mais il y avait quand même certaines limitations. Lorsqu'on voulait faire des calculs avec plusieurs fractions, ça pouvait rapidement devenir compliqué. Il fallait connaître différentes façons de décomposer les fractions et utiliser des tables pour faciliter les calculs.

Ce n'était donc pas nécessairement la façon la plus pratique de faire des opérations avec les fractions.

## Les mathématiques de la Mésopotamie 

Un peu plus tard, les civilisations de la Mésopotamie ont développé des méthodes très efficaces pour travailler avec les nombres. Les Babyloniens, par exemple, utilisaient un système basé sur 60. On appelle ça un système sexagésimal. Et vous utilisez encore ce système aujourd'hui sans nécessairement vous en rendre compte!

Une minute contient 60 secondes et une heure contient 60 minutes . Lorsqu'on mesure des angles, on utilise aussi ce système : un degré contient 60 minutes d'arc, et une minute d'arc contient 60 secondes d'arc.

Les Babyloniens avaient donc développé une façon très efficace de représenter et de calculer avec les fractions.

Pourquoi avaient-ils besoin de faire tout ça?

Parce que les mathématiques étaient très utiles dans la vie de tous les jours, particulièrement pour le commerce, l'agriculture, les impôts, les mesures et la gestion des ressources. Imaginez, par exemple, un marchand qui possède 10 sacs de céréales et qui veut vendre le quart de sa récolte.

Qu'est-ce que ça veut dire exactement, vendre un quart de sa récolte?

Il faut être capable de calculer combien de sacs cela représente, combien il lui en reste, combien il pourra vendre plus tard, etc. Et si une partie de la récolte doit être remise au roi ou utilisée pour payer des taxes? Encore une fois, il faut être capable de représenter précisément ces quantités.

Les fractions deviennent donc un outil pour organiser et comprendre la réalité.

## Pourquoi est-ce encore important aujourd'hui? 

Aujourd'hui, on pourrait se demander : *Pourquoi est-ce que je dois apprendre à faire des fractions? J'ai une calculatrice!*

Et c'est vrai. On possède maintenant des calculatrices, des ordinateurs et des téléphones capables d'effectuer énormément de calculs à notre place. Mais ça ne veut pas dire qu'on n'a plus besoin de comprendre les fractions. Au contraire.

Une calculatrice peut nous donner une réponse, mais elle ne nous explique pas nécessairement ce que cette réponse veut dire. Comprendre les fractions nous permet de saisir les quantités et les relations entre elles. Et les fractions sont partout autour de nous.

### En cuisine 

Vous voulez préparer un gâteau et la recette demande :

$$\frac{1}{2}\text{ tasse de lait}$$

ou

$$\frac{3}{4}\text{ de tasse de farine}$$

Mais finalement, vous voulez faire le double de la recette. Qu'est-ce que vous allez faire? Vous allez devoir multiplier les quantités par 2. C'est là qu'on va commencer à utiliser les opérations avec les fractions.

### Dans le temps 

Les fractions sont aussi présentes dans notre façon de parler du temps.

Une demi-heure, c'est :

$$\frac{1}{2}\times60=30$$

Donc une demi-heure correspond à 30 minutes.

Un quart d'heure correspond à :

$$\frac{1}{4}\times60=15$$

Donc un quart d'heure correspond à 15 minutes.

On utilise donc déjà les fractions dans notre langage de tous les jours, souvent sans même y penser.

### Les fractions sont partout 

Quand on y pense, les fractions sont finalement une façon très naturelle de décrire le monde.

-  On partage une pizza.
-  On mesure des ingrédients.
-  On partage de l'argent.
-  On calcule une taxe.
-  On mesure une distance.

Dans tous ces cas, on prend quelque chose qui représente un tout et on cherche à comprendre ou à représenter une partie de ce tout. C'est exactement ce que les fractions vont nous permettre de faire. Et maintenant qu'on comprend pourquoi les fractions existent et pourquoi elles sont utiles, on peut commencer à regarder mathématiquement ce qu'est réellement une fraction.

## Qu'est-ce qu'une fraction? 

Maintenant qu'on comprend un peu mieux pourquoi on utilise les fractions, il faut se demander : qu'est-ce qu'une fraction?

<div class="def-box">

<p class="def-title">Définition</p>

<p>Une fraction est une façon de représenter une partie d'un tout à l'aide de deux nombres.</p>

<p>On peut écrire une fraction comme ceci :</p>

$$
\frac{a}{b}
$$

<ul>
<li>Le nombre du haut, $a$, s'appelle le <strong>numérateur</strong>.</li>
<li>Le nombre du bas, $b$, s'appelle le <strong>dénominateur</strong>.</li>
</ul>

<p>Il y a cependant une règle très importante à retenir :</p>

$$
b \neq 0
$$

<p>Le dénominateur ne peut <strong>jamais être égal à zéro</strong>. On reviendra plus tard sur la raison pour laquelle on ne peut pas diviser par zéro. Pour le moment, retenez simplement que le dénominateur ne peut jamais être 0.</p>

</div>

### Prenons un exemple

$$\frac{3}{4}$$

On lit cette fraction *trois quarts*. Dans cette fraction :

- $3$ est le numérateur;
- $4$ est le dénominateur.

Mais qu'est-ce que ça veut réellement dire, $\dfrac{3}{4}$? Le dénominateur nous indique en combien de parties égales notre tout va être divisé. Donc, avec $4$ comme dénominateur, on divise notre tout en 4 parties égales. On pourrait, par exemple, prendre un rectangle et le diviser en quatre parties égales. Ensuite, le numérateur nous indique combien de ces parties on prend. Dans notre exemple, le numérateur est $3$. On prend donc 3 des 4 parties.

<div class="fraction-visual" markdown="1">
<div class="fraction-visual-title">Représentation de $\frac{3}{4}$</div>

<div class="rectangle-fraction">
  <div class="part filled"></div>
  <div class="part filled"></div>
  <div class="part filled"></div>
  <div class="part"></div>
</div>

<div class="visual-caption">Le rectangle est divisé en 4 parties égales. On en prend 3.</div>
</div>

On a alors :

$$\frac{3}{4}$$

<div class="tip-box" markdown="1">
**Le dénominateur détermine la découpe, le numérateur compte les morceaux.**

C'est une petite phrase qui peut nous aider à nous en rappeler.
</div>

### À retenir 

- Dénominateur → combien de parties égales?
- Numérateur → combien de parties prend-on?

## Une fraction, c'est aussi une division 

Il y a une autre façon très importante de comprendre une fraction. Une fraction représente également une division. Par exemple :

$$\frac{3}{4}=3\div4$$

La barre de fraction représente donc une division. On peut aussi représenter une division avec le symbole :

$$3\div4$$

Le nombre qui est divisé, $3$, correspond au numérateur.

Le nombre par lequel on divise, $4$, correspond au dénominateur.

On peut donc retenir :

$$\text{numérateur}\div\text{dénominateur}$$

Dans notre exemple :

$$\frac{3}{4}=3\div4$$

Et si on effectue la division :

$$3\div4=0{,}75$$

<div class="result-box" markdown="1">
$$\boxed{\frac{3}{4}=0{,}75}$$
</div>

Une même quantité peut donc être représentée de plusieurs façons :

<div class="result-box" markdown="1">
$$\boxed{\frac{3}{4}=3\div4=0{,}75}$$
</div>

C'est exactement la même quantité, mais on la représente de différentes manières.

Et c'est ça qui est intéressant avec les fractions : une fraction n'est pas seulement deux nombres placés l'un au-dessus de l'autre. Elle représente une quantité, une partie d'un tout et aussi une division.

## Les différents types de fractions 

Maintenant qu'on sait ce qu'est une fraction, on peut regarder les différents types de fractions qu'on peut rencontrer.

### Les fractions propres

Une fraction propre est une fraction dont le numérateur est plus petit que le dénominateur.

Par exemple :

$$\frac{1}{2},\qquad \frac{3}{4},\qquad \frac{5}{8},\qquad \frac{7}{10}$$

Dans tous ces cas, le nombre du haut est plus petit que le nombre du bas.

Une fraction propre représente donc toujours une quantité inférieure à 1.

Par exemple :

$$\frac{3}{4}<1$$

Si on pense à notre rectangle, on prend seulement une partie du rectangle. On n'a pas encore pris le tout.

### Les fractions impropres

Une fraction impropre est une fraction dont le numérateur est plus grand ou égal au dénominateur.

Par exemple :

$$\frac{5}{4},\qquad \frac{7}{3},\qquad \frac{10}{10}$$

Ces fractions représentent une quantité égale ou supérieure à 1.

Par exemple :

$$\frac{10}{10}=1$$

et

$$\frac{5}{4}>1$$

On peut d'ailleurs écrire :

$$\frac{5}{4}=1+\frac{1}{4}$$

Cela nous amène à une autre façon de représenter les nombres.

### Les nombres mixtes

Un nombre mixte est composé d'un nombre entier et d'une fraction.

Par exemple :

$$2\frac{1}{3}$$

Cela signifie :

$$2+\frac{1}{3}$$

Donc « deux et un tiers », c'est deux unités complètes auxquelles on ajoute un tiers.

Mais on peut aussi représenter ce même nombre uniquement avec une fraction.

Comment fait-on?

On multiplie d'abord le nombre entier par le dénominateur :

$$2\times3=6$$

Ensuite, on ajoute le numérateur :

$$6+1=7$$

On garde le même dénominateur :

$$2\frac{1}{3}=\frac{7}{3}$$

<div class="result-box" markdown="1">
$$\boxed{2\frac{1}{3}=\frac{7}{3}}$$
</div>

Les deux écritures représentent exactement la même quantité.

### Une fraction n'est pas nécessairement entre zéro et un

Il est important de ne pas penser qu'une fraction est toujours une quantité entre 0 et 1.

Par exemple :

$$\frac{1}{2}$$

est effectivement entre 0 et 1.

Mais :

$$\frac{5}{4}$$

est plus grand que 1.

Une fraction peut donc représenter une quantité plus petite que 1, égale à 1 ou plus grande que 1.

On peut aussi représenter les fractions sur une droite numérique.

Par exemple :

$$0\qquad \frac14\qquad \frac12\qquad \frac34\qquad1$$

On peut alors voir immédiatement que :

$$\frac14<\frac12<\frac34<1$$

### Plus le dénominateur est grand, plus les morceaux sont petits

Voici une idée qui peut sembler un peu étrange au début.

Comparez :

$$\frac12,\qquad \frac13,\qquad \frac15$$

On pourrait penser que 5 est plus grand que 2, donc que $\frac15$ devrait être plus grand que $\frac12$.

Mais c'est l'inverse :

$$\frac12>\frac13>\frac15$$

Pourquoi?

Revenons à notre pizza .

Si vous coupez une pizza en 2 morceaux égaux, chaque morceau est assez gros. Si vous coupez cette même pizza en 5 morceaux égaux, chaque morceau devient beaucoup plus petit.

Donc :

Plus on divise le tout en morceaux, plus chaque morceau devient petit. C'est pour ça que, lorsque le numérateur est le même, un dénominateur plus grand donne une fraction plus petite.

Par exemple :

$$\frac15<\frac14<\frac13<\frac12$$

## Les fractions équivalentes 

Il existe aussi ce qu'on appelle des fractions équivalentes. Deux fractions sont équivalentes lorsqu'elles ont une apparence différente, mais qu'elles représentent exactement la même quantité.

Par exemple :

$$\frac12=\frac24=\frac36=\frac48$$

Toutes ces fractions représentent la même quantité.

### On peut le voir avec une pizza 

Une moitié de pizza est la même quantité que deux quarts de pizza. Et deux quarts représentent la même quantité que trois sixièmes, ou quatre huitièmes. On peut donc représenter la même quantité de différentes façons.

### Comment obtenir une fraction équivalente?

Pour obtenir une fraction équivalente, on peut multiplier le numérateur et le dénominateur par le même nombre.

Par exemple :

$$\frac23$$

Si on multiplie le numérateur et le dénominateur par 2 :

$$\frac46$$

<div class="result-box" markdown="1">
$$\boxed{\frac23=\frac46}$$
</div>

Pourquoi est-ce que ça fonctionne?

Parce que :

$$\frac22=1$$

Multiplier une fraction par 1 ne change pas sa valeur.

On peut donc écrire :

$$\frac46$$

Et puisque $\frac22=1$, on n'a pas changé la quantité.

C'est une idée très importante en mathématiques : on peut représenter la même quantité de plusieurs façons.

Par exemple :

$$\frac11=\frac22=\frac33=\frac{20}{20}=\frac{100}{100}$$

Toutes ces fractions représentent un tout.

## Les fractions irréductibles 

Une fraction peut aussi être irréductible. Une fraction irréductible est une fraction qu'on ne peut plus simplifier en divisant son numérateur et son dénominateur par un même nombre entier supérieur à 1.

Par exemple :

$$\frac68$$

n'est pas irréductible, parce que 6 et 8 peuvent tous les deux être divisés par 2 :

$$\frac68=\frac{6\div2}{8\div2}=\frac34$$

<div class="result-box" markdown="1">
$$\boxed{\frac68=\frac34}$$
</div>

Et $\dfrac34$ est irréductible, parce qu'on ne peut plus simplifier davantage.

Quand on simplifie une fraction, on cherche donc à obtenir une écriture plus simple qui représente exactement la même quantité.

## Pourquoi garder les fractions plutôt que toujours utiliser les décimales? 

On pourrait se demander : « Pourquoi utiliser des fractions? Pourquoi ne pas simplement transformer tout en nombres décimaux? » Parfois, les décimales sont effectivement très pratiques. Mais certaines quantités deviennent beaucoup moins pratiques à représenter avec des décimales.

Prenons :

$$\frac13$$

Si on fait la division :

$$1\div3=0{,}3333333\ldots$$

Les 3 continuent indéfiniment. Donc, on peut écrire :

$$0{,}\overline{3}$$

pour indiquer que le 3 se répète, mais la fraction

$$\frac13$$

est beaucoup plus simple et beaucoup plus précise.

Et surtout, elle nous dit immédiatement ce que représente la quantité : un tiers d'un tout.

Par exemple :

$$\frac13+\frac13+\frac13=1$$

C'est beaucoup plus clair que d'essayer d'utiliser des nombres décimaux arrondis.

Si on utilise $0{,}33$, on obtient :

$$0{,}33+0{,}33+0{,}33=0{,}99$$

On n'obtient pas exactement 1! 

Le problème vient de l'arrondissement.

La fraction, elle, représente exactement la quantité.

C'est donc une des grandes forces des fractions : elles permettent de représenter certaines quantités exactement, même lorsque leur écriture décimale est compliquée ou infinie.

## Et pourquoi est-ce qu'on ne peut pas diviser par zéro? 

Maintenant, on arrive à une règle extrêmement importante en mathématiques :

<div class="tip-box" markdown="1">
$$\boxed{\text{Le dénominateur ne peut jamais être égal à zéro.}}$$
</div>

Rappelons-nous qu'une fraction représente aussi une division :

$$\frac{a}{b}=a\div b$$

Prenons quelque chose de simple :

$$6\div2$$

On peut voir cette division comme une question :

**Combien de groupes de 2 peut-on faire avec 6?**

La réponse est 3.

$$6\div2=3$$

On peut aussi le voir avec une multiplication :

$$2\times3=6$$

Donc la réponse à $6\div2$ est le nombre qui, multiplié par 2, donne 6.

Mais maintenant, essayons :

$$6\div0$$

La question deviendrait :

**Combien de groupes de 0 faut-il pour obtenir 6?**

Et là, on a un problème.

On pourrait essayer n'importe quel nombre :

$$1\times0=0$$

$$100\times0=0$$

$$1\,000\,000\times0=0$$

Peu importe le nombre que l'on choisit :

<div class="result-box" markdown="1">
$$\boxed{\text{n'importe quel nombre}\times0=0}$$
</div>

Il est donc impossible de trouver un nombre $x$ qui satisfait :

$$x\times0=6$$

Il n'existe tout simplement **aucun nombre** qui peut faire ça.

C'est pourquoi :

<div class="tip-box" markdown="1">
$$\boxed{6\div0}$$

Cette division **n'est pas définie**. Elle ne donne **pas** zéro.
</div>

C'est une distinction très importante.

**Diviser par zéro ne donne pas 0. La division n'est tout simplement pas définie.**

### Une situation de la vie de tous les jours 

On peut aussi comprendre le problème avec quelque chose de très concret.

Imaginez que vous avez 10 \$ et que vous voulez partager cet argent entre 2 personnes.

Ça fonctionne :

$$10\div2=5$$

Chaque personne reçoit 5 \$.

Mais si vous voulez partager les 10 \$ entre zéro personne, ça devient quoi?

Il n'y a personne avec qui partager l'argent.

La situation n'a tout simplement pas de sens.

C'est la même idée en mathématiques.

Le zéro représente ici une absence de quantité ou de groupes, et on ne peut pas construire une division à partir de zéro groupe pour obtenir une quantité non nulle.

<div class="tip-box" markdown="1">
**Le dénominateur ne peut jamais être zéro. Jamais.**
</div>

Et croyez-moi, en avançant en mathématiques, vous allez probablement rencontrer une situation où une erreur de calcul vous amènera à essayer de diviser par zéro. Lorsque ça arrive, ce n'est pas que les mathématiques ne fonctionnent plus : c'est qu'il y a une erreur quelque part dans notre démarche. Il faut alors revenir en arrière et trouver où l'erreur s'est produite.

## Et maintenant? 

On a maintenant une bonne base pour comprendre les fractions. On sait :

-  ce qu'est une fraction;
-  ce que sont le numérateur et le dénominateur;
-  la différence entre une fraction propre et une fraction impropre;
-  ce qu'est un nombre mixte;
-  comment représenter une fraction sur une droite numérique;
-  pourquoi le dénominateur influence la taille des morceaux;
-  ce que sont les fractions équivalentes;
-  comment simplifier une fraction;
-  ce qu'est une fraction irréductible;
-  pourquoi certaines fractions sont plus pratiques que leur écriture décimale;
-  et surtout, pourquoi on ne peut jamais diviser par zéro.

Dans la prochaine partie, on va commencer à travailler avec les fractions : comment les additionner, les soustraire, les multiplier et les diviser, et surtout comment mettre des fractions sur un même dénominateur lorsque c'est nécessaire. 

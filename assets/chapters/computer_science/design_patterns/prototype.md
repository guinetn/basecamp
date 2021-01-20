## prototype
 
CREATIONAL PATTERN
 
Clonage d'une instance existance qui sert de modèle
A fully initialized instance to be copied or cloned
Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

Specify the kind of objects to create using a prototypical instance, and create new objects by copying this prototype.


ntroduction problem
Original GoF pattern can not be introduced to the existing program without modifying the source code. (This problem is mentioned at p.120, line.37-39 in the GoF book.)
Used programming technique(s)

Abstract method addition of "copy()" method to the existing classes.

Consequences

(+) Prototype pattern can be introduced into existing classes.

Intention

des prototypes variés existent qui sont copiés et assemblésOn utilise le Prototype lorsque :• un système doit être indépendant de la façon dont ses produits sont créés, assemblés, représentés• quand la classe n'est connue qu'à l'exécution• pour éviter une hiérarchie de Factory parallèle à une hiérarchie de produits
Motivation
Solution
 
![](assets/chapters/computer_science/design_patterns/prototype.png)


```js
```
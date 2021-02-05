## strategy 

BEHAVIOURAL PATTERN

Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

Mécanisme permettant de modifier un algorithme de façon transparente (tris...)
Encapsulates an algorithm inside a class
Define a family of algorithms, encapsulate each one, and make them interchangeable.
Strategy lets the algorithm vary independently from clients that use it.
Plus vaste que le pattern "state", permet de choisir un algorithme adapté au contexte.

Intention
On utilise Strategy lorsque :
• de nombreuses classes associées ne diffèrent que par leur comportement. Stratégie offre un moyen de configurer une classe avec un comportement parmi plusieurs.
• on a besoin de plusieurs variantes d'algorithme.• un algorithme utilise des données que les clients ne doivent pas connaitre.Motivation
Solution

![](assets/books/computer_science/design_patterns/strategy.png)


```js
public class IndentDocument {
 public void setIndenter( Indenter indenter );

 // Depend on the context
 public void indent( Document doc ) {
 indenter.indent( doc );  
 }
}

// Indent document strategy
public interface Indenter {
 public void indent( Document doc );
}
```
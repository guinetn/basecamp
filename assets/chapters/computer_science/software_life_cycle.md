# SOFTWARE LIFECYCLE
 
### SDLC Phases
planning, creating, developing, testing, deploying an application
 
 
 
* Analyse des besoins et faisabilité
c'est-à-dire l'expression, le recueil et la formalisation des besoins du demandeur (le client) et de l'ensemble des contraintes, puis l'estimation de la faisabilité de ces besoins
* Spécifications ou conception générale
il s'agit de l'élaboration des spécifications de l'architecture générale du logiciel
* Conception détaillée
cette étape consiste à définir précisément chaque sous-ensemble du logiciel
* Codage (Implémentation ou programmation)
c'est la traduction dans un langage de programmation des fonctionnalités définies lors de phases de conception Interfaces...
* Tests unitaires
ils permettent de vérifier individuellement que chaque sous-ensemble du logiciel est implémenté conformément aux spécifications
* Intégration
l'objectif est de s'assurer de l'interfaçage des différents éléments (modules) du logiciel. Elle fait l'objet de tests d'intégration consignés dans un document
* Qualification (ou recette)
c'est-à-dire la vérification de la conformité du logiciel aux spécifications initiales
* Documentation
elle vise à produire les informations nécessaires pour l'utilisation du logiciel et pour des développements ultérieurs
* Mise en production
c'est le déploiement sur site du logiciel
* Maintenance
elle comprend toutes les actions correctives (maintenance corrective) et évolutives (maintenance évolutive) sur le logiciel.
 
L'origine de ce découpage provient du constat que les erreurs ont un coût d'autant plus élevé qu'elles sont détectées tardivement dans le processus de réalisation. Le cycle de vie permet de détecter les erreurs au plus tôt et ainsi de maîtriser la qualité du logiciel, les délais de sa réalisation et les coûts associés.

 
### WATERFALL MODEL - 1970's
Easy to manage and a sequential approach. 
Testing activities are carried out after the development activities are over:it not a continuous process
 
Cons: vérification du bon fonctionnement du système est réalisée trop tardivement : lors de la phase d'intégration, ou pire, lors de la mise en production.

    Specifications
        ↓     ↑ validation
    Detailed conception 
        ↓     ↑ unit test
      Coding
       ↓  ↑ integration
    Integration
        ↓ ↑ validation  
    Production
        ↓ ↑ validation
    Maintenance
    
chaque phase se termine à une date précise par la production de certains documents ou logiciels. Les résultats sont définis sur la base des interactions entre étapes, ils sont soumis à une revue approfondie et on ne passe à la phase suivante que s'ils sont jugés satisfaisants.

Le modèle original ne comportait pas de possibilité de retour en arrière. Celle-ci a été rajoutée ultérieurement sur la base qu'une étape ne remet en cause que l'étape précédente, ce qui, dans la pratique, s'avère insuffisant.    

### V model
a simultaneous process (dev/deploy/test)
modèle en cascade dans lequel le développement des tests et du logiciel sont effectués de manière synchrone
Le principe de ce modèle est qu'avec toute décomposition doit être décrite la recomposition et que toute description d'un composant est accompagnée de tests qui permettront de s'assurer qu'il correspond à sa description.

Ceci rend explicite la préparation des dernières phases (validation-vérification) par les premières (construction du logiciel), et permet ainsi d'éviter un écueil bien connu de la spécification du logiciel : énoncer une propriété qu'il est impossible de vérifier objectivement après la réalisation.

Cependant, ce modèle souffre toujours du problème de la vérification trop tardive du bon fonctionnement du système.
   
  Specifications       <-- validated by -->      Validation
        \                                          /
         \                                        /
    Detailed conception <-- validated by ->   Unit tests
             \                                  /
              \                                /
            Coding         <--- ---->    Qualification
                \                            /
                 \                          /
                  \                        /
                          Integration
    
### Scrum
Product focused, Business oriented.
  
### Agile
Flexible and allows to make changes in any phase. 
Project requirements can change frequently.


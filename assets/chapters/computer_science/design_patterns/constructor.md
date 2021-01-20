## constructor 

Called whenever we create an object of a class
The class represents an entity: something like Car, Person…
The constructor method does the work of assigning values to the instance variables of the class to create a new object.

![](assets/chapters/computer_science/design_patterns/constructor.png)


```js
class Pokemon {
    name: string
    baseExperience: number
    abilities: string[]

    constructor(name: string, baseExperience: number, abilities: string[]) {
        this.name = name
        this.baseExperience = generation
        this.abilities = [...abilities]
    }

    addAbility(ability: string) {
        /* Method to add new abilities */
    }    
}

let bulbasaurObj = new Pokemon("bulbasaur", 64, ["chlorophyll"])
```

### Prototype Design Pattern

To create clones of the existing objects. This is similar to the prototypal inheritance in JavaScript. All of the properties and methods of an object can be made available on any other object by leveraging the power of the __proto__ property

Used to implement inheritance in JavaScript: It add the properties of the parent to the child objects. Inherited properties are present on the __proto__ key.

```js
let obj = Object.create(Pokemon.prototype)

let shapePrototype = {
    width: 10,
    height: 10,

    draw: function (shape) {

    }
}

function Rectangle () {}

/* The prototype of Rectangle is shapePrototype, which means Rectangle should be cloned as shapePrototype */
Rectangle.prototype = shapePrototype

let rectObj = new Rectangle()

/* draw method is present on the rectObj as shapePrototype is attached to it __proto__ property */
rectObj.draw('rectangle')
```
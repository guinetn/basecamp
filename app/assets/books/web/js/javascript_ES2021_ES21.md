# ES21 - ECMAScript 2021
	
## String.prototype.replaceAll()

```js
const string = "it-is-just-a-test";
 
// instead of doing this
string.replace(/-/g, "_")
// "it_is_just_a_test"
 
// in ES2021 we can do
string.replaceAll("-", "_")
// "it_is_just_a_test"
```

## Promise.any()

Promise combinators: 
- Promise.all()
- Promise.race()            renvoie la première valeur réglée (soit remplie, soit rejetée)
- Promise.allSettled()
- Promise.any()             ES21 add. ignore les promesses rejetées jusqu'à la première promesse remplie
in: iterable object. As soon as one promise if filled it return this Promise

```js
const API = "https://api.github.com/users"
 
Promise.any([
  fetch(`${API}/pawelgrzybek`),
  fetch(`${API}/gabriel403`)
])
  .then(response => response.json())
  .then(({name}) => console.log(`Cool dude is: ${name}`))
  .catch(error => console.error(error));
```

## weakref

weakref is used to implement cache & maps to big objects 
to avoid to keep a lot of memory for a long term. Allow memory to be collected early or later and if you need it again you can regerneate a new cache
assign an object to a variable = it point to a chunk of memory wher ethe object is stored (strong reference)

```js
const obj = { spec: "ES2021" };
const objWeakRef = new WeakRef(obj);
 
// do something cool
 
objWeakRef.deref();
// returns obj in case it is still in memory
// returns undefined in case it has been garbage collected
```

## FinalizationRegistry

To register callbacks to call when an object has been collected. Related to weakRef

```js
const obj = { spec: "ES2021" };
const registry = new FinalizationRegistry(value => {
    console.log(`The ${value} object has been garbage collected.`)
});
registry.register(obj, "ECMAScript 2021");
 
// perform some action that triggers garbage collector on obj
// The ECMAScript 2021 object has been garbage collected.
```

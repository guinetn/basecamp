# ELM

http://elm-lang.org/
http://package.elm-lang.org/
https://guide.elm-lang.org/
https://github.com/evancz/elm-architecture-tutorial/
http://elmlang.herokuapp.com/
https://bendyworks.com/blog/elm-frontend-right-now-updated-for-0-18
https://www.toptal.com/front-end/getting-started-elm-language
https://www.npmjs.com/package/elm-upgrade
https://github.com/elm-lang/elm-platform/blob/master/upgrade-docs/0.18.md

# Functional language that compiles to JavaScript with code that's fast, hard to break, easily testable, and extremely maintenable
# Purely functional, strongly typed, reactive, and event-driven web client language. 
# Lightweight and easy
# It takes a step back from the norms and really changes the way you reason about and program web application front-ends.
# Great performance and no runtime exceptions
# Virtual DOM implementation that is very fast compared to React, Angular, and Ember.
# Elm has influenced projects like Redux

functional programming language aimed at frontend web development

* Blazing-fast virtual DOM
* Friendly compile-time errors
* Zero runtime exceptions
* Constraints as guarantees
* Piped syntax
* Easy refactoring
* Increased productivity
* Helpful type system
* Time-traveling debugger

# ELM Architecture 
https://github.com/evancz/elm-architecture-tutorial/
is a simple pattern for architecting webapps

# THE CORE IDEA IS THAT YOUR CODE IS BUILT AROUND: 
  * a Model of your application state
  * a way to update your model
  * a way to view your model

## install
npm install --save redux
git clone https://github.com/evancz/elm-architecture-tutorial.git
cd elm-architecture-tutorial
elm-reactor
http://localhost:8000/ 



# SAMPLES

http://elm-lang.org/examples
https://github.com/patrik-piskay/elm-tweet-search/blob/master/src/client/Main.elm
https://gist.github.com/pablohirafuji

elm-lang/html collapsed Html.App into Html
# Remove any import Html.App imports and refer to Html.program instead.
evancz/elm-http => elm-lang/http


### a simple counter (you can increment and decrement the counter)

```js
import Html exposing (Html, button, div, text)
import Html.Events exposing (onClick)

main = Html.beginnerProgram { model = 0, view = view, update = update }

type Msg = Increment | Decrement

update msg model =
  case msg of
    Increment ->
      model + 1

    Decrement ->
      model - 1

view model =
  div []
    [ button [ onClick Decrement ] [ text "-" ]
    , div [] [ text (toString model) ]
    , button [ onClick Increment ] [ text "+" ]
    ]



### button.elm
import Html exposing (Html, button, div, text)
import Html.Events exposing (onClick)

main =
  Html.beginnerProgram { model = model , view = view , update = update }

-- MODEL

type alias Model = Int

model : Model
model = 0

-- UPDATE

type Msg = Increment | Decrement

update : Msg -> Model -> Model
update msg model =
  case msg of
    Increment -> model + 1
    Decrement -> model - 1

-- VIEW

view : Model -> Html Msg
view model =
  div []
    [ button [ onClick Decrement ] [ text "-" ]
    , div [] [ text (toString model) ]
    , button [ onClick Increment ] [ text "+" ]
    ]

```    




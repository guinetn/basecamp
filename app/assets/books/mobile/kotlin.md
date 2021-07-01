# Kotlin

https://kotlinlang.org/
https://kotlinlang.org/docs/tutorials
https://hackernoon.com/kotlin-a-deeper-look-8569d4da36f
http://kotlin.jetbrains.org/
https://www.i-programmer.info/news/150/13113.html
https://pub.dartlang.org/  										Find and use packages to build Dart↗ and Flutter↗ apps.

# 31 Days Of Kotlin
https://medium.com/google-developers/31daysofkotlin-week-1-recap-fbd5a622ef86

https://try.kotlinlang.org/#/Examples/Canvas/Fancy%20lines/Fancy%20lines.kt

http://www.gamefromscratch.com/post/2015/12/02/Cheat-sheet-for-Learning-the-Kotlin-Language.aspx
[Online Kotlin](https://try.kotlinlang.org/#/Examples/Hello,%20world!/Simplest%20version/Simplest%20version.kt)
https://kotlinlang.org/docs/kotlin-docs.pdf

[Cheat Sheet Part 1](https://gist.github.com/dodyg/5823184)
[Cheat Sheet Part 2]()
[Cheat Sheet Part 3]()

Programming language that compiles to JVM, JavaScript and native code
You can develop server side apps in Kotlin also.
Kotlin team is also working on iOS app development using Kotlin/Native.

a programming language that compiles to JVM, JavaScript and native code
Kotlin is a general purpose programming language. Based on that, learning Kotlin will give you more benefits.

Flutter:
    is a framework for cross-platform (Android and iOS) mobile development which uses Dart programming language 
    Flutter solves a specific problem, it’s a UI framework. 


Modern statically typed programming language that boost productivity and developer happiness
Safer code
Interoperable with Java

"Android development will become increasingly Kotlin-first," Google said in a blog post today (May 7). "Many new Jetpack APIs and features will be offered first in Kotlin. If you're starting a new project, you should write it in Kotlin."

Android Jetpack comprises a collection of Android software components to make it easier to create Android apps.
https://developer.android.com/jetpack

language developed by JetBrains and a close competitor of Java. Kotlin runs on the Java virtual machine, but can also be compiled into JavaScript. It’s designed to be less verbose than Java, adds first-class function support and offers additional safety measures to avoid common errors. Like Java, it can also be used to develop Android applications.


Statically typed programming language for modern multiplatform applications
100% interoperable with Java and Android
new programming language for the JVM. It produces Java bytecode, supports Android and generates JavaScript. 

Build Applications For
JVM
Android
Browser
Native

Kotlin programming language is now a first-class citizen in Android,

interoperability with Java: this means that you can call Kotlin code from Java in the same way that you can call Java code from Kotlin. 

the four most used methods of the Kotlin Standard Library:
apply
with
let
run


# Kotlin Basic syntax

# Basic syntax 

# Program entry point 
	fun main (args: Array<String>) { } 		

# Define a function 

	Can be declared 
		outside of a class
		as member functions of a class
		as extension functions
		as local functions (function inside another function)
			Local function can access local variables of outer functions (closure)

 			Parameters: Pascal notation (name: type)
 			   ↓ 	   	           ___ default value
 			   ↓                  /    
	fun double(x: Int, off: Int = 0): Int {
    	return 2 * x 				   ↑
	}	 							return type: 	fun F(): Unit {...}
															  ↑ 
															 default empty return type (optional)

	fun double(x: Int): Int = x * 2 	Single-Expression function, omitted curly braces 
	fun double(x: Int) = x * 2

	Call a function 
	val result = double(2)
	Sample().double(3)

	print ln ("Hello world") 

	use Pair to return more than one value
		fun someFunction(): Pair<String, Int> = Pair("foo", 1)
		// ...
		val (foo, one) = someFunction() // foo 1st, one 2nd value of a Pair

## Infix notation

	infix fun Int.shl(x: Int): Int { ... }

	1 shl 2 	// calling the function using the infix notation
	1.shl(2) 	// is the same 

# Control structures 
	if (a < b) a e Ise b  		Conditional 

	possiblyNu11 ? "default" 	Elvis operator for working With nullable variables 

	while (a < b) { } 

# COLLECTIONS

# Tuples
	Pair("foo", "bar")
	Triple(1, "wom", "bat")


# Mutable collections

			Iterable<T>
		Collection<T> 
	List<out T> 

# Immutable collections


mapOf(1 to 3, 4 to 2)
map
filter
reduce
immutable Lists
# Sets: plus or minus

# Kotlin Standard Library

# TUTORIALS

package hello 							Optional package header
fun main(args: Array<String>) {			Package-level function, which takes an Array of strings as a parameter
   println("Hello World!")
}



https://try.kotlinlang.org/#/Kotlin%20Koans/Collections/Introduction/Task.kt

task.kt
----------------------
fun start(): String  {
    return "OK"
}


# JSON

import kotlin.browser.*
import org.w3c.fetch.*

fun main(args: Array<String>) {
    window.fetch(Request("https://raw.githubusercontent.com/JetBrains/kotlin/master/.gitignore")).then(onFulfilled = {
        it.text().then(onFulfilled = {
            println(it)
        })
    })
}

# API REQUEST

https://antonioleiva.com/api-request-kotlin/
	val result = URL("<api call>").readText()
	This function is not recommended for huge responses, but it will be enough in most situations. 

	Asynchronous call
		As you know, the main thread is in charge of UI rendering and interaction, and we shouldn’t block it with long tasks, because the UI performance will be affected. In the case of HTTP requests, even the Android SDK will prevent us from doing it by throwing an exception. The typical solution in Android is the use of AsyncTask. An AsyncTask has an abstract method called doInBackground, which is executed in a secondary thread.


https://www.infoworld.com/article/3224868/what-is-kotlin-the-java-alternative-explained.html

# Coroutines 

	lightweight threads
	You start them with the launch coroutine builder in the context of some CoroutineScope. 
	One of the most useful coroutine scopes is runBlocking{}, which applies to the scope of its code block.

	import kotlinx.coroutines.*

	fun main() = runBlocking { // this: CoroutineScope
	    launch { // launch a new coroutine in the scope of runBlocking
	        delay(1000L) // non-blocking delay for 1 second
	        println("World!")
	    }
	    println("Hello,")
	}
	This code produces the following output, with a one-second delay between lines:

	Hello,
	World!		

# DOKKA

	Dokka is a popular documentation engine for Kotlin projects
	https://github.com/Kotlin/dokka

## See sample https://guides.gradle.org/building-kotlin-jvm-libraries/


# SAMPLE

https://guides.gradle.org/building-kotlin-jvm-libraries/


# A text editor or IDE
# A Java Development Kit (JDK), version 8 or higher
# A Gradle distribution, version 5.0 or better

$ mkdir -p my-kotlin-library/src/main/kotlin/org/example
$ cd my-kotlin-library

my-kotlin-library
├── build.gradle.kts        build script to compile our new Kotlin library
|    	plugins { kotlin("jvm") version "1.3.61"}               	Apply the Kotlin plugin, targeting the Java VM
|		repositories { jcenter() }                                  Declare a dependency repository on Bintray jcenter
|		dependencies { 
|                         implementation(kotlin("stdlib"))          Declare a dependency on the Kotlin standard library
|                         testImplementation("junit:junit:4.12")    Add test implementation dependency on JUnit
|                     }
|
└── src
    ├── main
    │   └── kotlin
    │       └── org
    │           └── example
    │               └── MyLibrary.kt

                            package org.example

							/**
							 * The `Language` type defines a programming language with a name and hotness score.
							 * @property name The name of the language.
							 * @property hotness A score from 1 to 10 of user enthusiasm. 10 = so hot right now
							 */
							data class Language(val name: String, val hotness: Int)

							class MyLibrary {
							    /**
							     * @return data relating to the Kotlin {@code Language}.
							     */
							    fun kotlinLanguage() = Language("Kotlin", 10)
							}
    └── test
        └── kotlin
            └── org
                └── example
                    └── MyLibraryTest.kt

                    		package org.example

							import org.junit.Assert.assertEquals
							import org.junit.Test

							class MyLibraryTest {
							    @Test fun testMyLanguage() {
							        assertEquals("Kotlin", MyLibrary().kotlinLanguage().name)
							        assertEquals(10, MyLibrary().kotlinLanguage().hotness)
							    }
							}


$ gradle test 				Execute tests
> Task :compileKotlin
# Using kotlin incremental compilation
> Task :compileTestKotlin
# Using kotlin incremental compilation
# BUILD SUCCESSFUL in 5s
3 actionable tasks: 3 executed




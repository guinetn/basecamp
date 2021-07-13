# F#  #

Functional programming
Interop with C#, .NET
Use NuGet
open source
cross-platform ( Linux, Mac OS X, Android, iOS, Windows, GPUs, browsers)

https://fsharp.org/
https://github.com/dotnet/fsharp
http://dungpa.github.io/fsharp-cheatsheet/

## F# 1.0  #
## F# 2.0  #

## F# 3.0  #

## F# 4.0  #

## F# 5.0  #

```f#
printfn "Hello World from F#"
```
>dotnet fsi hello.fsx

To create a project:
>dotnet new console --language F#
>dotnet run


### Variables
let numbers = [0 .. 10]
numbers
numbers.[3]
Take the numbers from 2nd index to the 5th
numbers.[2..5]    .[start .. end] to slice a subset of the data 

let s1 = "Hello"
let s2 = "World"
s1 + ", " + s2 + "!"
"""A triple-quoted string can contain quotes "like this" anywhere within it"""

(1, "fred", Math.PI)   Tuples
struct (1, Math.PI)    Struct tuples for performance

Record: combine different kinds of data into an aggregate. They cannot be null and come with default comparison and equality. Records are comparable and equatable:
type ContactCard =
    { Name: string
      Phone: string
      ZipCode: string }
// Create a new record
{ Name = "Alf"; Phone = "(555) 555-5555"; ZipCode = "90210" }
// . to access a record
let alf = { Name = "Alf"; Phone = "(555) 555-5555"; ZipCode = "90210" }
alf.Phone
let showContactCard contact = contact.Name + " - Phone: " + contact.Phone + ", Zip: " + contact.ZipCode
    showContactCard alf

### Data structures

* Arrays: are mutable
let firstTwoHundred = [| 1 .. 200 |]
firstTwoHundred.[197..]
// Filter the previous list of numbers and sum their squares.
firstTwoHundred |> Array.filter (fun x -> x % 3 = 0) |> Array.sumBy (fun x -> x * x)

* Lists: linear sequences of values of the same type
[0 .. 10]

let thisYear = DateTime.Now.Year
let fridays =
    [
        for month in 1 .. 10 do
            for day in 1 .. DateTime.DaysInMonth(thisYear, month) do
                let date = DateTime(thisYear, month, day)
                if date.DayOfWeek = DayOfWeek.Friday then
                    date.ToShortDateString()
    ]
// Get the first five fridays of this year
fridays |> List.take 5
fridays.[..4]    First five


### Functions
let sampleFunction x = 2*x*x - 5*x + 3             infered types
let sampleFunction' (x: int) = 2*x*x - 5*x + 3     figure out
sampleFunction 5
sampleFunction' 12

* Functions composition
let negate x = -x
let square x = x * x
let print x = printfn "The number is %d" x

let squareNegateThenPrint x = print (negate (square x))
squareNegateThenPrint 5

* Pipeline operator |>
let squareNegateThenPrint x = x |> square |> negate |> print
squareNegateThenPrint 5


Parallel Programming
#!time
let bigArray = [| 0 .. 100_000 |]
let rec fibonacci n = if n <= 2 then n else fibonacci (n-1) + fibonacci (n-2)
// We'll use the '%A' print formatter for F# constructs for these results, since they are enormous
let results =
    bigArray
    |> Array.Parallel.map (fun n -> fibonacci (n % 25))
printfn "%A" results
#!time
​



```f#
open System.Reflection

[<EntryPoint>]
let main argv =
  let asm =
    argv
    |> Array.tryHead
    |> Option.map Assembly.LoadFrom
    |> Option.defaultWith (Assembly.GetExecutingAssembly)

  printfn "%s" asm.FullName

  for t in asm.GetTypes () do
    printfn " * %s" t.FullName
```

## more

- https://hub-binder.mybinder.ovh/user/dotnet-interactive-cb9ukwlm/lab/tree/fsharp/Introduction%20to%20F%23.ipynb




































# CheatSheets

https://github.com/dungpa/fsharp-cheatsheet

# This cheatsheet glances over some of the common syntax of [F# 3.0](http://research.microsoft.com/en-us/um/cambridge/projects/fsharp/manual/spec.html).
# If you have any comments, corrections, or suggested additions, please open an issue or send a pull request to [https://github.com/dungpa/fsharp-cheatsheet](https://github.com/dungpa/fsharp-cheatsheet).

# Contents
--------
[Comments](#Comments)  
[Strings](#Strings)  
[Basic Types and Literals](#BasicTypesAndLiterals)  
[Functions](#Functions)  
[Pattern Matching](#PatternMatching)  
[Collections](#Collections)  
[Tuples and Records](#TuplesAndRecords)  
[Discriminated Unions](#DiscriminatedUnions)  
[Exceptions](#Exceptions)  
[Classes and Inheritance](#ClassesAndInheritance)  
[Interfaces and Object Expressions](#InterfacesAndObjectExpressions)  
[Active Patterns](#ActivePatterns)  
[Compiler Directives](#CompilerDirectives)

----------------
# COMMENTS
----------------
# Block comments are placed between `(*` and `*)`. Line comments start from `//` and continue until the end of the line.

    (* This is block comment *)

    // And this is line comment

# XML doc comments come after `///` allowing us to use XML tags to generate documentation.    

    /// The `let` keyword defines an (immutable) value
    let result = 1 + 1 = 2

--------------
# STRINGS
--------------
# F# `string` type is an alias for `System.String` type.

    /// Create a string using string concatenation
    let hello = "Hello" + " World"

# Use *verbatim strings* preceded by `@` symbol to avoid escaping control characters (except escaping `"` by `""`).

    let verbatimXml = @"<book title=""Paradise Lost"">"

# We don't even have to escape `"` with *triple-quoted strings*.

    let tripleXml = """<book title="Paradise Lost">"""

*Backslash strings* indent string contents by stripping leading spaces.

    let poem = 
        "The lesser world was daubed\n\
         By a colorist of modest skill\n\
         A master limned you in the finest inks\n\
         And with a fresh-cut quill."

------------------------------------------------
# BASIC TYPES AND LITERALS
------------------------------------------------
# Most numeric types have associated suffixes, e.g., `uy` for unsigned 8-bit integers and `L` for signed 64-bit integer.

    let b, i, l = 86uy, 86, 86L

    // [fsi:val b : byte = 86uy]
    // [fsi:val i : int = 86]
    // [fsi:val l : int64 = 86L]

# Other common examples are `F` or `f` for 32-bit floating-point numbers, `M` or `m` for decimals, and `I` for big integers.

    let s, f, d, bi = 4.14F, 4.14, 0.7833M, 9999I

    // [fsi:val s : float32 = 4.14f]
    // [fsi:val f : float = 4.14]
    // [fsi:val d : decimal = 0.7833M]
    // [fsi:val bi : System.Numerics.BigInteger = 9999]

# See [Literals (MSDN)](http://msdn.microsoft.com/en-us/library/dd233193.aspx) for complete reference.

------------------
# FUNCTIONS
------------------
# The `let` keyword also defines named functions.

    let negate x = x * -1 
    let square x = x * x 
    let print x = printfn "The number is: %d" x

    let squareNegateThenPrint x = 
        print (negate (square x)) 

### Pipe and composition operators
# Pipe operator `|>` is used to chain functions and arguments together. Double-backtick identifiers are handy to improve readability especially in unit testing:

    let ``square, negate, then print`` x = 
        x |> square |> negate |> print

# This operator is essential in assisting the F# type checker by providing type information before use:

    let sumOfLengths (xs : string []) = 
        xs 
        |> Array.map (fun s -> s.Length)
        |> Array.sum

# Composition operator `>>` is used to compose functions:

    let squareNegateThenPrint' = 
        square >> negate >> print

### Recursive functions
# The `rec` keyword is used together with the `let` keyword to define a recursive function:

    let rec fact x =
        if x < 1 then 1
        else x * fact (x - 1)

*Mutually recursive* functions (those functions which call each other) are indicated by `and` keyword:

    let rec even x =
       if x = 0 then true 
       else odd (x - 1)

    and odd x =
       if x = 0 then false
       else even (x - 1)

--------------------------------
# PATTERN MATCHING
--------------------------------
# Pattern matching is often facilitated through `match` keyword.

    let rec fib n =
        match n with
        | 0 -> 0
        | 1 -> 1
        | _ -> fib (n - 1) + fib (n - 2)

# In order to match sophisticated inputs, one can use `when` to create filters or guards on patterns:

    let sign x = 
        match x with
        | 0 -> 0
        | x when x < 0 -> -1
        | x -> 1

# Pattern matching can be done directly on arguments:

    let fst' (x, _) = x

or implicitly via `function` keyword:

    /// Similar to `fib`; using `function` for pattern matching
    let rec fib' = function
        | 0 -> 0
        | 1 -> 1
        | n -> fib' (n - 1) + fib' (n - 2)

# For more complete reference visit [Pattern Matching (MSDN)](http://msdn.microsoft.com/en-us/library/dd547125.aspx).

----------------------
# COLLECTIONS
----------------------

### Lists
# A *list* is an immutable collection of elements of the same type.

    // Lists use square brackets and `;` delimiter
    let list1 = [ "a"; "b" ]
    // :: is prepending
    let list2 = "c" :: list1
    // @ is concat    
    let list3 = list1 @ list2   

    // Recursion on list using (::) operator
    let rec sum list = 
        match list with
        | [] -> 0
        | x :: xs -> x + sum xs

### Arrays
*Arrays* are fixed-size, zero-based, mutable collections of consecutive data elements.

    // Arrays use square brackets with bar
    let array1 = [| "a"; "b" |]
    // Indexed access using dot
    let first = array1.[0]  

### Sequences
# A *sequence* is a logical series of elements of the same type. Individual sequence elements are computed only as required, so a sequence can provide better performance than a list in situations in which not all the elements are used.

    // Sequences can use yield and contain subsequences
    let seq1 = 
        seq {
            // "yield" adds one element
            yield 1
            yield 2

            // "yield!" adds a whole subsequence
            yield! [5..10]
        }

### Higher-order functions on collections
# The same list `[ 1; 3; 5; 7; 9 ]` or array `[| 1; 3; 5; 7; 9 |]` can be generated in various ways.

 - Using range operator `..`

        let xs = [ 1..2..9 ]

 - Using list or array comprehensions

        let ys = [| for i in 0..4 -> 2 * i + 1 |]

 - Using `init` function

        let zs = List.init 5 (fun i -> 2 * i + 1)

# Lists and arrays have comprehensive sets of higher-order functions for manipulation.

  - `fold` starts from the left of the list (or array) and `foldBack` goes in the opposite direction

        let xs' = Array.fold (fun str n -> 
                    sprintf "%s,%i" str n) "" [| 0..9 |]

  - `reduce` doesn't require an initial accumulator

        let last xs = List.reduce (fun acc x -> x) xs

  - `map` transforms every element of the list (or array)

        let ys' = Array.map (fun x -> x * x) [| 0..9 |]

  - `iter`ate through a list and produce side effects

        let _ = List.iter (printfn "%i") [ 0..9 ] 

# All these operations are also available for sequences. The added benefits of sequences are laziness and uniform treatment of all collections implementing `IEnumerable<'T>`.

    let zs' =
        seq { 
            for i in 0..9 do
                printfn "Adding %d" i
                yield i
        }

------------------------------------
# TUPLES AND RECORDS
------------------------------------
# A *tuple* is a grouping of unnamed but ordered values, possibly of different types:

    // Tuple construction
    let x = (1, "Hello")

    // Triple
    let y = ("one", "two", "three") 

    // Tuple deconstruction / pattern
    let (a', b') = x

# The first and second elements of a tuple can be obtained using `fst`, `snd`, or pattern matching:

    let c' = fst (1, 2)
    let d' = snd (1, 2)

    let print' tuple =
        match tuple with
        | (a, b) -> printfn "Pair %A %A" a b

*Records* represent simple aggregates of named values, optionally with members:

    // Declare a record type
    type Person = { Name : string; Age : int }

    // Create a value via record expression
    let paul = { Name = "Paul"; Age = 28 }

    // 'Copy and update' record expression
    let paulsTwin = { paul with Name = "Jim" }

# Records can be augmented with properties and methods:

    type Person with
        member x.Info = (x.Name, x.Age)

# Records are essentially sealed classes with extra topping: default immutability, structural equality, and pattern matching support.

    let isPaul person =
        match person with
        | { Name = "Paul" } -> true
        | _ -> false

----------------------------------------
# DISCRIMINATED UNIONS
----------------------------------------
*Discriminated unions* (DU) provide support for values that can be one of a number of named cases, each possibly with different values and types.

    type Tree<'T> =
        | Node of Tree<'T> * 'T * Tree<'T>
        | Leaf


    let rec depth = function
        | Node(l, _, r) -> 1 + max (depth l) (depth r)
        | Leaf -> 0

# F# Core has a few built-in discriminated unions for error handling, e.g., [Option](http://msdn.microsoft.com/en-us/library/dd233245.aspx) and [Choice](http://msdn.microsoft.com/en-us/library/ee353439.aspx).

    let optionPatternMatch input =
       match input with
        | Some i -> printfn "input is an int=%d" i
        | None -> printfn "input is missing"

# Single-case discriminated unions are often used to create type-safe abstractions with pattern matching support:

    type OrderId = Order of string

    // Create a DU value
    let orderId = Order "12"

    // Use pattern matching to deconstruct single-case DU
    let (Order id) = orderId

--------------------
# EXCEPTIONS
--------------------
# The `failwith` function throws an exception of type `Exception`.

    let divideFailwith x y =
        if y = 0 then 
            failwith "Divisor cannot be zero." 
        else x / y

# Exception handling is done via `try/with` expressions.

    let divide x y =
       try
           Some (x / y)
       with :? System.DivideByZeroException -> 
           printfn "Division by zero!"
           None

# The `try/finally` expression enables you to execute clean-up code even if a block of code throws an exception. Here's an example which also defines custom exceptions.

    exception InnerError of string
    exception OuterError of string

    let handleErrors x y =
       try 
         try 
            if x = y then raise (InnerError("inner"))
            else raise (OuterError("outer"))
         with InnerError(str) -> 
              printfn "Error1 %s" str
       finally
          printfn "Always print this."

----------------------------------------------
# CLASSES AND INHERITANCE
----------------------------------------------
# This example is a basic class with (1) local let bindings, (2) properties, (3) methods, and (4) static members.

    type Vector(x : float, y : float) =
        let mag = sqrt(x * x + y * y) // (1)
        member this.X = x // (2)
        member this.Y = y
        member this.Mag = mag
        member this.Scale(s) = // (3)
            Vector(x * s, y * s)
        static member (+) (a : Vector, b : Vector) = // (4)
            Vector(a.X + b.X, a.Y + b.Y)

# Call a base class from a derived one.

    type Animal() =
        member __.Rest() = ()

    type Dog() =
        inherit Animal()
        member __.Run() =
            base.Rest()

*Upcasting* is denoted by `:>` operator.

    let dog = Dog() 
    let animal = dog :> Animal

*Dynamic downcasting* (`:?>`) might throw an `InvalidCastException` if the cast doesn't succeed at runtime.

    let shouldBeADog = animal :?> Dog

------------------------------------------------------------------
# INTERFACES AND OBJECT EXPRESSIONS
------------------------------------------------------------------
# Declare `IVector` interface and implement it in `Vector'`.

    type IVector =
        abstract Scale : float -> IVector

    type Vector'(x, y) =
        interface IVector with
            member __.Scale(s) =
                Vector'(x * s, y * s) :> IVector
        member __.X = x
        member __.Y = y

# Another way of implementing interfaces is to use *object expressions*.

    type ICustomer =
        abstract Name : string
        abstract Age : int

    let createCustomer name age =
        { new ICustomer with
            member __.Name = name
            member __.Age = age }

------------------------------
# ACTIVE PATTERNS
------------------------------
*Complete active patterns*:

    let (|Even|Odd|) i = 
        if i % 2 = 0 then Even else Odd

    let testNumber i =
        match i with
        | Even -> printfn "%d is even" i
        | Odd -> printfn "%d is odd" i

*Parameterized active patterns*:

    let (|DivisibleBy|_|) by n = 
        if n % by = 0 then Some DivisibleBy else None

    let fizzBuzz = function 
        | DivisibleBy 3 & DivisibleBy 5 -> "FizzBuzz" 
        | DivisibleBy 3 -> "Fizz" 
        | DivisibleBy 5 -> "Buzz" 
        | i -> string i

*Partial active patterns* share the syntax of parameterized patterns but their active recognizers accept only one argument.

--------------------------------------
# COMPILER DIRECTIVES
--------------------------------------
# Load another F# source file into FSI.

    #load "../lib/StringParsing.fs"

# Reference a .NET assembly (`/` symbol is recommended for Mono compatibility).

    #r "../lib/FSharp.Markdown.dll"

# Include a directory in assembly search paths.

    #I "../lib"
    #r "FSharp.Markdown.dll"

# Other important directives are conditional execution in FSI (`INTERACTIVE`) and querying current directory (`__SOURCE_DIRECTORY__`).

    #if INTERACTIVE
    let path = __SOURCE_DIRECTORY__ + "../lib"
    #else
    let path = "../../../lib"
    #endif










let projectFile = "decoders.nuspec"
trace "Building Decoders Package..."    
let doc = System.Xml.Linq.XDocument.Load(projectFile)
let vers = doc.Descendants(XName.Get("version", doc.Root.Name.NamespaceName)) 
// "vers" reason: https://blog.codeinside.eu/2015/06/21/fake-create-nuget-packages/

    NuGet (fun p -> 
      {p with       
        Project = "Decoders_Package"
        Version = (Seq.head vers).Value
        OutputPath = @"./"
        WorkingDir = "./"
        AccessKey = "-ApiKey API-VWF5WDPKXXMVIHQPN27OW75YOK"
        PublishUrl = "http://dev-a-build-03:8080/nuget/packages?replace=true"
        Publish = true        
       }) projectFile



#r <reference>
open System
let argsAsString = Environment.GetEnvironmentVariable("fsiargs-buildscriptargs")





build.fsx

#r "../../packages/FAKE/tools/FakeLib.dll"
#r "../../packages/OndeoSystems.FakeTasks/lib/OndeoSystems.FakeTasks.dll"

open System
open System.IO
open System.Text.RegularExpressions

open Fake
open Fake.FileSystemHelper
open Fake.OpenCoverHelper
open Fake.PicklesHelper
open Fake.Testing

open OndeoSystems.FakeTasks

# Environment.CurrentDirectory <- __SOURCE_DIRECTORY__

let argsAsString = Environment.GetEnvironmentVariable("fsiargs-buildscriptargs")
let configuration = argsAsString

// Properties
let properties = [ ("Configuration", configuration); ("Platform", "Any CPU") ]
let propertiesForPortal = [ ("Configuration", configuration); ("Platform", "x64") ]
let propertiesForInstallation = [ ("Configuration", "Release"); ("Platform", "x64") ]
let binDir = "../../bin"
let nuGetPackagesDir = "../../packages"
let commonAssembliesDir = binDir @@ "common"
let decodersDir = commonAssembliesDir @@ "decoders"
let testsDir  = "../../tests"
let artifactsDir = "../../artifacts"

let credentials fileName = 
    let fmtDebug = "{0}/{1}@DEV11G" 
    let fmtIntegration = "{0}/{1}@ESM" 

    let m = Regex.Match(fileName, @".*-(.*)_.*\.sql")
    if not m.Success then
        failwith (String.Format("Script {0} name doesn't respect the naming convention", fileName))

    let schema = m.Groups.[1].Value

    match(configuration, schema) with
    | ("Debug", "Acquisition") -> String.Format(fmtDebug, "MDC_SITRV3_ACQ", "MDC")
    | ("Debug", "Business") -> String.Format(fmtDebug, "MDC_SITRV3_BUS", "MDC")
    | ("Debug", "Configuration") -> String.Format(fmtDebug, "MDC_SITRV3_CONFIG", "MDC")
    | ("Development", "Acquisition") -> String.Format(fmtDebug, "MDC_SITRV3_ACQ", "MDC")
    | ("Development", "Business") -> String.Format(fmtDebug, "MDC_SITRV3_BUS","MDC")
    | ("Development", "Configuration") -> String.Format(fmtDebug, "MDC_SITRV3_CONFIG", "MDC")
    | ("Integration", "Acquisition") -> String.Format(fmtIntegration, "TC_2G_ACQUISITION", "telecollect78")
    | ("Integration", "Business") -> String.Format(fmtIntegration, "TC_2G_BUSINESS", "telecollect78")
    | ("Integration", "Configuration") -> String.Format(fmtIntegration, "TC_2G_CONFIG", "telecollect78")
    | _ -> failwith "Unknown configuration"

# Target "RestorePackages" (fun _ -> 
    !! "../../src/**/*.sln"
    |> SetBaseDir Environment.CurrentDirectory
    |> Seq.filter (fun s -> not (s.Contains("Kerlink"))) // To do : make a specific build script for Kerlink solution
    |> Seq.iter (fun s ->
        printfn "%s" s
        RestoreMSSolutionPackages (fun p ->
            { p with
                ToolPath = "../../tools/NuGet/nuget.exe"
                // Sources = ["HeadendPackages";"nuget.org"]
                OutputPath = nuGetPackagesDir
                Retries = 1 }) s
    )
)

# Target "Clean" (fun _ ->
    DirectoryUtils.DeleteDirectory commonAssembliesDir
    DirectoryUtils.DeleteDirectory testsDir
    DirectoryUtils.DeleteDirectory artifactsDir
)

# Target "SetConfigFilesWritable" (fun _ ->
    [| @"..\..\Services\AcquisitionWebSite\web.config";
       @"..\..\Services\AcquisitionWebSite\NLog.config";
       @"..\..\Services\BusinessWebSite\web.config";
       @"..\..\Services\BusinessWebSite\NLog.config";
       @"..\..\Services\WanFrontWebSite\web.config";
       @"..\..\Services\WanFrontWebSite\NLog.config";
       @"..\..\Services\ConcentratorServicesWebSite\web.config";
       @"..\..\Services\TeleoperationWebApp\web.config";
       @"..\..\Services\GenericFramesWebSite\web.config";
       @"..\..\Portal\PortalWebSite\web.config";
       @"..\..\Portal\PortalWebSite\NLog.config";
       @"..\..\Tools\ToolsWebSite\web.config" |]
    |> SetReadOnly false
)

# Target "BuildOndeoSystems" (fun _ ->
    MSBuild commonAssembliesDir "Build" properties [| "../../src/OndeoSystems/OndeoSystems.sln" |]
    |> ignore
)

# Target "BuildOndeoSystemsTests" (fun _ ->
    !! ("../../src/OndeoSystems/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildDomainOtherThanDecoders" (fun _ ->
    !! ("../../src/Domain/**/*Domain*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore
)

# Target "BuildDomainDecoders" (fun _ ->
    !! ("../../src/Domain/**/*FrameDecoder*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild decodersDir "Build" properties
    |> ignore
)

# Target "BuildDomainTests" (fun _ ->
    !! ("../../src/Domain/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildCommon" (fun _ ->
    !! ("../../src/Common/**/RemoteReadingSystem*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore
)

# Target "BuildCommonTests" (fun _ ->
    !! ("../../src/Common/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildBusiness" (fun _ ->
    !! ("../../src/Business/**/RemoteReadingSystem*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore
)

# Target "BuildBusinessTests" (fun _ ->
    !! ("../../src/Business/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildServices" (fun _ ->
    MSBuild "" "Build" properties [| "../../src/Services/Services.sln" |]
    |> ignore

    !! ("../../src/Services/**/*WebSite.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild artifactsDir "Package" properties
    |> ignore

    !! ("../../src/Services/**/*WebApp.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild artifactsDir "Package" properties
    |> ignore
)

# Target "BuildServicesTests" (fun _ ->
    !! ("../../src/Services/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildPortal" (fun _ ->
    MSBuild "" "Build" propertiesForPortal [| "../../src/Portal/Portal.sln" |]
    |> ignore

    MSBuild artifactsDir "Package" propertiesForPortal [| "../../src/Portal/PortalWebSite/PortalWebSite.csproj" |]
    |> ignore
)

# Target "BuildTools" (fun _ ->
    MSBuild "" "Build" properties [| "../../src/Tools/Tools.sln" |]
    |> ignore

    MSBuild artifactsDir "Package" properties [| "../../src/Tools/ToolsWebSite/ToolsWebSite.csproj" |]
    |> ignore
)

# Target "BuildFrameCopier" (fun _ ->
    MSBuild "" "Build" properties [| "../../src/FrameCopier/FrameCopier.sln" |]
    |> ignore

    MSBuild artifactsDir "Package" properties [| "../../src/FrameCopier/FrameCopierWebSite/FrameCopierWebSite.csproj" |]
    |> ignore
)

# Target "BuildMSI" (fun _ ->
    !! ("../../src/Installation/**/*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore

    !! ("../../src/Installation/**/*.wixproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild artifactsDir "Build" propertiesForInstallation
    |> ignore
)

# Target "CleanArtifacts" (fun _ ->
    let di = System.IO.DirectoryInfo(artifactsDir)
    di.GetFiles()
    |> Seq.filter (fun fi -> fi.Extension.ToLowerInvariant() <> ".msi")
    |> Seq.iter (fun fi -> fi.Delete())

    di.GetDirectories()
    |> Seq.filter (fun innerDi -> innerDi.Name <> "_PublishedWebsites")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "Services")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "Tools")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "Docs")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "SQL")
    |> Seq.iter (fun innerDi -> innerDi.Delete true)
)

# Target "RunTests" (fun _ ->
    !! (testsDir @@ "*Test*.dll")
    |> SetBaseDir Environment.CurrentDirectory
    |> xUnit2 (fun p -> { p with
                            HtmlOutputPath = Some (testsDir @@ "xunit.html")
                            ToolPath = "../../packages/xunit.runner.console/tools/xunit.console.exe" })
)

# Target "Run tests and compute code coverage" (fun _ ->

    let xUnitReportPath = Path.GetFullPath(testsDir @@ "xunit.xml")
    let openCoverReportPath = Path.GetFullPath(testsDir @@ "opencover.xml")
    let coberturaReportPath = Path.GetFullPath(testsDir @@ "cobertura.xml")
    let openCoverageReportDir = Path.GetFullPath(testsDir @@ "OpenCoverageReport")
    let srcDir = Path.GetFullPath("../../src")

    let assemblies = Directory.GetFiles(testsDir, "*Test*.dll") 
                     |> Seq.map(fun c -> Path.GetFullPath(c))
                     |> Seq.fold (fun acc cur -> (sprintf " %s %s" acc cur)) ""

    OpenCover (fun p -> { p with
                            ExePath = "../../packages/OpenCover/tools/OpenCover.Console.exe"
                            WorkingDir = Environment.CurrentDirectory
                            TestRunnerExePath = "../../packages/xunit.runner.console/tools/xunit.console.exe"
                            Filter="+[OndeoSystems*]* +[RemoteReadingSystem*]* +[FrameDecoder*]* -[*Tests*]*"
                            Register = RegisterType.Register
                            Output = openCoverReportPath
                             }) (sprintf "%s -nologo -parallel none -noshadow -xml %s" assemblies xUnitReportPath)

    let exitCode = ExecProcess (fun psi -> 
        psi.FileName <- @"../../packages/ReportGenerator/tools/ReportGenerator.exe"
        psi.Arguments <- sprintf "-reports:%s -targetdir:%s" openCoverReportPath openCoverageReportDir) (TimeSpan.FromMinutes 5.0)

    if exitCode <> 0 then failwithf "ReportGenerator failed."

    let exitCode = ExecProcess (fun psi -> 
        psi.FileName <- @"../../packages/OpenCoverToCoberturaConverter/tools/OpenCoverToCoberturaConverter.exe"
        psi.Arguments <- sprintf "-input:%s -output:%s -sources:%s" openCoverReportPath coberturaReportPath srcDir) (TimeSpan.FromMinutes 5.0)

    if exitCode <> 0 then failwithf "OpenCoverToCoberturaConverter failed."
)

# Target "GenerateDocs" (fun _ ->

    let inputDir = artifactsDir @@ "tempdoc"
    Directory.CreateDirectory(inputDir) |> ignore

    Directory.GetFiles("../../src/Domain/Tests.BDD", "*.feature")
    |> Seq.iter (fun f -> File.Copy(f, inputDir @@ Path.GetFileName(f)))

    Directory.GetFiles("../../src/Services/Tests.BDD", "*.feature")
    |> Seq.iter (fun f -> File.Copy(f, inputDir @@ Path.GetFileName(f)))

    Directory.GetFiles(inputDir)
    |> SetReadOnly false

    Pickles (fun p -> { p with
                            ToolPath = "../../packages/Pickles.CommandLine/tools/pickles.exe"
                            FeatureDirectory = inputDir
                            OutputDirectory = artifactsDir @@ "Docs" })    
)

// Dependencies
"Clean"
    ==> "RestorePackages"
    ==> "SetConfigFilesWritable"
    ==> "BuildOndeoSystems"
    ==> "BuildOndeoSystemsTests"
    ==> "BuildDomainOtherThanDecoders"
    ==> "BuildDomainDecoders"
    ==> "BuildDomainTests"
    ==> "BuildCommon"
    ==> "BuildCommonTests"
    ==> "BuildBusiness"
    ==> "BuildBusinessTests"
    ==> "BuildServices"
    ==> "BuildServicesTests"
    ==> "BuildPortal"
    ==> "BuildTools"
    =?> ("Run tests and compute code coverage", "Debug" = configuration)
    =?> ("RunTests", "Release" = configuration)
    ==> "BuildMSI"
    ==> "GenerateDocs"
    ==> "CleanArtifacts"

// Start build
# RunTargetOrDefault "CleanArtifacts"








build-octopus.fsx

#r "../../packages/FAKE/tools/FakeLib.dll"
#r "../../packages/OndeoSystems.FakeTasks/lib/OndeoSystems.FakeTasks.dll"
#r "System.Xml.Linq"

open System
open System.IO
open System.Text.RegularExpressions
open System.Xml.Linq

open Fake
open Fake.FileSystemHelper
open Fake.OpenCoverHelper
open Fake.PicklesHelper
open Fake.Testing

open OndeoSystems.FakeTasks

# Environment.CurrentDirectory <- __SOURCE_DIRECTORY__

let argsAsString = Environment.GetEnvironmentVariable("fsiargs-buildscriptargs")
let configuration = argsAsString

// Properties
let properties = [ ("Configuration", configuration); ("Platform", "Any CPU") ]
let propertiesForPortal = [ ("Configuration", configuration); ("Platform", "x64"); ("RunOctoPack","true"); ("OctoPackPackageVersion", "5.0.0-Iteration3-Release"); ("OctoPackPublishPackageToHttp", "http://dev-a-build-03:8080/nuget/packages?replace=true"); ("OctoPackPublishApiKey","API-VWF5WDPKXXMVIHQPN27OW75YOK") ]
let propertiesForInstallation = [ ("Configuration", "Release"); ("Platform", "x64") ]
let propertiesForOctopus = [ ("Configuration", "Octopus"); ("Platform", "Any CPU");  ("RunOctoPack","true"); ("OctoPackPackageVersion", "5.0.0-Iteration3-Release"); ("OctoPackPublishPackageToHttp", "http://dev-a-build-03:8080/nuget/packages?replace=true"); ("OctoPackPublishApiKey","API-VWF5WDPKXXMVIHQPN27OW75YOK") ]
let binDir = "../../bin"
let nuGetPackagesDir = "../../packages"
let commonAssembliesDir = binDir @@ "common"
let decodersDir = commonAssembliesDir @@ "decoders"
let testsDir  = "../../tests"
let artifactsDir = "../../artifacts"
let nugetPath = "../../tools/NuGet/nuget.exe"

let credentials fileName = 
    let fmtDebug = "{0}/{1}@DEV11G" 
    let fmtIntegration = "{0}/{1}@ESM" 

    let m = Regex.Match(fileName, @".*-(.*)_.*\.sql")
    if not m.Success then
        failwith (String.Format("Script {0} name doesn't respect the naming convention", fileName))

    let schema = m.Groups.[1].Value

    match(configuration, schema) with
    | ("Debug", "Acquisition") -> String.Format(fmtDebug, "MDC_SITRV3_ACQ", "MDC")
    | ("Debug", "Business") -> String.Format(fmtDebug, "MDC_SITRV3_BUS", "MDC")
    | ("Debug", "Configuration") -> String.Format(fmtDebug, "MDC_SITRV3_CONFIG", "MDC")
    | ("Development", "Acquisition") -> String.Format(fmtDebug, "MDC_SITRV3_ACQ", "MDC")
    | ("Development", "Business") -> String.Format(fmtDebug, "MDC_SITRV3_BUS","MDC")
    | ("Development", "Configuration") -> String.Format(fmtDebug, "MDC_SITRV3_CONFIG", "MDC")
    | ("Integration", "Acquisition") -> String.Format(fmtIntegration, "TC_2G_ACQUISITION", "telecollect78")
    | ("Integration", "Business") -> String.Format(fmtIntegration, "TC_2G_BUSINESS", "telecollect78")
    | ("Integration", "Configuration") -> String.Format(fmtIntegration, "TC_2G_CONFIG", "telecollect78")
    | _ -> failwith "Unknown configuration"

# Target "RestorePackages" (fun _ -> 
    !! "../../src/**/*.sln"
    |> SetBaseDir Environment.CurrentDirectory
    |> Seq.filter (fun s -> not (s.Contains("Kerlink"))) // To do : make a specific build script for Kerlink solution
    |> Seq.iter (fun s ->
        printfn "%s" s
        RestoreMSSolutionPackages (fun p ->
            { p with
                ToolPath = "../../tools/NuGet/nuget.exe"
                // Sources = ["HeadendPackages";"nuget.org"]
                OutputPath = nuGetPackagesDir
                Retries = 1 }) s
    )
)

# Target "Clean" (fun _ ->
    DirectoryUtils.DeleteDirectory commonAssembliesDir
    DirectoryUtils.DeleteDirectory testsDir
    DirectoryUtils.DeleteDirectory artifactsDir
)

# Target "SetConfigFilesWritable" (fun _ ->    
    [| @"..\..\Services\Acquisition\App.config"; 
       @"..\..\Services\AcquisitionWebSite\web.config";
       @"..\..\Services\AcquisitionWebSite\NLog.config";
       @"..\..\Services\BusinessWebSite\web.config";
       @"..\..\Services\BusinessWebSite\NLog.config";
       @"..\..\Services\WanFrontWebSite\web.config";
       @"..\..\Services\WanFrontWebSite\NLog.config";
       @"..\..\Services\ConcentratorServicesWebSite\web.config";
       @"..\..\Services\TeleoperationWebApp\web.config";
       @"..\..\Services\GenericFramesWebSite\web.config";
       @"..\..\Portal\PortalWebSite\web.config";
       @"..\..\Portal\PortalWebSite\NLog.config";
       @"..\..\Tools\ToolsWebSite\web.config" |]
    |> SetReadOnly false
)

# Target "BuildOndeoSystems" (fun _ ->
    MSBuild commonAssembliesDir "Build" properties [| "../../src/OndeoSystems/OndeoSystems.sln" |]
    |> ignore
)

# Target "BuildOndeoSystemsTests" (fun _ ->
    !! ("../../src/OndeoSystems/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildDomainOtherThanDecoders" (fun _ ->
    !! ("../../src/Domain/**/*Domain*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore
)

# Target "BuildDomainDecoders" (fun _ ->
    !! ("../../src/Domain/**/*FrameDecoder*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild decodersDir "Build" properties
    |> ignore
)

# Target "BuildDomainTests" (fun _ ->
    !! ("../../src/Domain/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildCommon" (fun _ ->
    !! ("../../src/Common/**/RemoteReadingSystem*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore
)

# Target "BuildCommonTests" (fun _ ->
    !! ("../../src/Common/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildBusiness" (fun _ ->
    !! ("../../src/Business/**/RemoteReadingSystem*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore
)

# Target "BuildBusinessTests" (fun _ ->
    !! ("../../src/Business/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildServices" (fun _ ->
    MSBuild "" "Build" propertiesForOctopus [| "../../src/Services/Services.sln" |]
    |> ignore

    !! ("../../src/Services/**/*WebSite.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild artifactsDir "Package" propertiesForOctopus
    |> ignore

    !! ("../../src/Services/**/*WebApp.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild artifactsDir "Package" propertiesForOctopus
    |> ignore
)

# Target "BuildServicesTests" (fun _ ->
    !! ("../../src/Services/**/*Test*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild testsDir "Build" properties
    |> ignore
)

# Target "BuildPortal" (fun _ ->
    MSBuild "" "Build" propertiesForPortal [| "../../src/Portal/Portal.sln" |]
    |> ignore

    !! ("../../src/Portal/PortalWebSite/PortalWebSite.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild artifactsDir "Package" propertiesForPortal
    |> ignore
)

# Target "BuildTools" (fun _ ->
    MSBuild "" "Build" properties [| "../../src/Tools/Tools.sln" |]
    |> ignore

    MSBuild artifactsDir "Package" properties [| "../../src/Tools/ToolsWebSite/ToolsWebSite.csproj" |]
    |> ignore
)

# Target "BuildFrameCopier" (fun _ ->
    MSBuild "" "Build" properties [| "../../src/FrameCopier/FrameCopier.sln" |]
    |> ignore

    MSBuild artifactsDir "Package" properties [| "../../src/FrameCopier/FrameCopierWebSite/FrameCopierWebSite.csproj" |]
    |> ignore
)

# Target "BuildMSI" (fun _ ->
    !! ("../../src/Installation/**/*.csproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild commonAssembliesDir "Build" properties
    |> ignore

    !! ("../../src/Installation/**/*.wixproj")
    |> SetBaseDir Environment.CurrentDirectory
    |> MSBuild artifactsDir "Build" propertiesForInstallation
    |> ignore
)

# Target "CleanArtifacts" (fun _ ->
    let di = System.IO.DirectoryInfo(artifactsDir)
    di.GetFiles()
    |> Seq.filter (fun fi -> fi.Extension.ToLowerInvariant() <> ".msi")
    |> Seq.iter (fun fi -> fi.Delete())

    di.GetDirectories()
    |> Seq.filter (fun innerDi -> innerDi.Name <> "_PublishedWebsites")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "Services")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "Tools")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "Docs")
    |> Seq.filter (fun innerDi -> innerDi.Name <> "SQL")
    |> Seq.iter (fun innerDi -> innerDi.Delete true)
)

# Target "RunTests" (fun _ ->
    !! (testsDir @@ "*tests.dll")
    |> SetBaseDir Environment.CurrentDirectory
    |> xUnit2 (fun p -> { p with
                            HtmlOutputPath = Some (testsDir @@ "xunit.html")
                            ToolPath = "../../packages/xunit.runner.console/tools/xunit.console.exe" })
)

# Target "Run tests and compute code coverage" (fun _ ->

    let xUnitReportPath = Path.GetFullPath(testsDir @@ "xunit.xml")
    let openCoverReportPath = Path.GetFullPath(testsDir @@ "opencover.xml")
    let coberturaReportPath = Path.GetFullPath(testsDir @@ "cobertura.xml")
    let openCoverageReportDir = Path.GetFullPath(testsDir @@ "OpenCoverageReport")
    let srcDir = Path.GetFullPath("../../src")

    let assemblies = Directory.GetFiles(testsDir, "*tests.dll") 
                     |> Seq.map(fun c -> Path.GetFullPath(c))
                     |> Seq.fold (fun acc cur -> (sprintf " %s %s" acc cur)) ""

    OpenCover (fun p -> { p with
                            ExePath = "../../packages/OpenCover/tools/OpenCover.Console.exe"
                            WorkingDir = Environment.CurrentDirectory
                            TestRunnerExePath = "../../packages/xunit.runner.console/tools/xunit.console.exe"
                            Filter="+[OndeoSystems*]* +[RemoteReadingSystem*]* +[FrameDecoder*]* -[*Tests*]*"
                            Register = RegisterType.Register
                            Output = openCoverReportPath
                             }) (sprintf "%s -nologo -parallel none -noshadow -xml %s" assemblies xUnitReportPath)

    let exitCode = ExecProcess (fun psi -> 
        psi.FileName <- @"../../packages/ReportGenerator/tools/ReportGenerator.exe"
        psi.Arguments <- sprintf "-reports:%s -targetdir:%s" openCoverReportPath openCoverageReportDir) (TimeSpan.FromMinutes 5.0)

    if exitCode <> 0 then failwithf "ReportGenerator failed."

    let exitCode = ExecProcess (fun psi -> 
        psi.FileName <- @"../../packages/OpenCoverToCoberturaConverter/tools/OpenCoverToCoberturaConverter.exe"
        psi.Arguments <- sprintf "-input:%s -output:%s -sources:%s" openCoverReportPath coberturaReportPath srcDir) (TimeSpan.FromMinutes 5.0)

    if exitCode <> 0 then failwithf "OpenCoverToCoberturaConverter failed."
)

# Target "GenerateDocs" (fun _ ->

    let inputDir = artifactsDir @@ "tempdoc"
    Directory.CreateDirectory(inputDir) |> ignore

    Directory.GetFiles("../../src/Domain/Tests.BDD", "*.feature")
    |> Seq.iter (fun f -> File.Copy(f, inputDir @@ Path.GetFileName(f)))

    Directory.GetFiles("../../src/Services/Tests.BDD", "*.feature")
    |> Seq.iter (fun f -> File.Copy(f, inputDir @@ Path.GetFileName(f)))

    Directory.GetFiles(inputDir)
    |> SetReadOnly false

    Pickles (fun p -> { p with
                            ToolPath = "../../packages/Pickles.CommandLine/tools/pickles.exe"
                            FeatureDirectory = inputDir
                            OutputDirectory = artifactsDir @@ "Docs" })    
)

# Target "CreateDecodersPackage" (fun _ ->
    let projectFile = "decoders.nuspec"

    trace "Building Decoders Package..."    
    let doc = System.Xml.Linq.XDocument.Load(projectFile)
    let vers = doc.Descendants(XName.Get("version", doc.Root.Name.NamespaceName)) 
    // "vers" reason: https://blog.codeinside.eu/2015/06/21/fake-create-nuget-packages/

    NuGet (fun p -> 
      {p with       
        Project = "Decoders_Package"
        Version = (Seq.head vers).Value
        OutputPath = @"./"
        WorkingDir = "./"
        AccessKey = "-ApiKey API-VWF5WDPKXXMVIHQPN27OW75YOK"
        PublishUrl = "http://dev-a-build-03:8080/nuget/packages?replace=true"
        Publish = true        
       }) projectFile
)

// Dependencies
"Clean"
    ==> "RestorePackages"
    ==> "SetConfigFilesWritable"
    ==> "BuildOndeoSystems"
    ==> "BuildOndeoSystemsTests"
    ==> "BuildDomainOtherThanDecoders"
    ==> "BuildDomainDecoders"
    ==> "CreateDecodersPackage"
    ==> "BuildDomainTests"
    ==> "BuildCommon"
    ==> "BuildCommonTests"
    ==> "BuildBusiness"
    ==> "BuildBusinessTests"
    ==> "BuildServices"
    ==> "BuildServicesTests"
    ==> "BuildPortal"
    ==> "BuildTools"
    =?> ("Run tests and compute code coverage", "Debug" = configuration)
    =?> ("RunTests", "Release" = configuration)
    ==> "BuildMSI"
    ==> "GenerateDocs"
    ==> "CleanArtifacts"

// Start build
# RunTargetOrDefault "CleanArtifacts"





# FUNCTIONAL-FIRST WEB APPLICATIONS IN F#
https://compositional-it.com/blog/2017/09-18-safe-web/index.html
# Alternative F# server-side Web Stacks

Suave is not only F# library for the server-side web programming (although it's arguably the most popular, with the biggest community support). There also exist other options for creating web applications with F#:

Giraffe - an F# micro web framework for building rich web applications. It has been heavily inspired and is similar to Suave, but has been specifically designed with ASP.NET Core in mind and can be plugged into the ASP.NET Core pipeline via middleware. Giraffe applications are composed of so called HttpHandler functions which can be thought of a mixture of Suave's WebParts and ASP.NET Core's middleware.

Freya - a functional web stack built on top of OWIN. At its core, Freya wraps the OWIN environment dictionary with a computation expression and provides access to that dictionary with lenses. Additional layers of the stack provide types based on the HTTP (and related) RFCs, a pipeline abstraction for connecting Freya computations, a router, and an implementation of the HTTP finite state machine

WebSharper - allows end-to-end web applications with both client and server developed in F#. It includes TypeScript interoperability, mobile web apps, getting started material, templates and much more.

Azure Functions - an event driven, compute-on-demand experience that extends the existing Azure application platform with capabilities to implement code triggered by events occurring in Azure or third party service as well as on-premises systems. Developers can leverage Azure Functions to build HTTP-based API endpoints accessible by a wide range of applications




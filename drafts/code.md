# C

1972 - Dennis Ritchie
  	http://www.cplusplus.com/reference
	http://www.cplusplus.com/reference/cstdio/   	<cstdio> (stdio.h)
	

## hello.c

```c
#include <stdio.h>

int main(void) {
    printf("Hello, World!");
}
```
>gcc hello.c -o hello  
>./hello

## C is not OO (no classes)!

## C has no 
	try-catch type of 
	operator overloading
	C function cannot have a variable number arguments. See variadic, use (...)
	C don't support function overloading (many functions with same name but with different signatures)
	no native bool 
	
	
## C has 
	is case sensitive
	dynamic memory allocation
	enum 		enum jour {LUNDI, MARDI, MERCREDI, JEUDI, VENDREDI, SAMEDI, DIMANCHE} d1, d2=LUNDI;
	ternary 	a ? b : c;
	arrays in C can only hold a single type of data. Structs solve this: can store values of different types
	 	we need to declare the types of the fields that the struct can hold up front


## bool in C

	bool exists from C99, but not in C89/90...

	 * in C90 it must be defined as a typedef or enum:

		typedef int bool;
		#define TRUE  1
		#define FALSE 0

		bool f = FALSE;
		if (f) { ... }

		Alternatively:

		typedef enum { FALSE, TRUE } boolean;
		boolean b = FALSE;
		if (b) { ... }

	* C99 added a builtin _Bool data type and if you #include <stdbool.h>, it provides bool as a macro to _Bool.

		// C99 defines bool, true, false in stdbool.h
		#include <stdbool.h>  // <cstdbool> en C++
		#define bool unsigned int    // pseudo type booléen (en fait un entier non signé) afin d'améliorer la lisibilité de vos signatures functions/typage de vos variables
		#define true 1
		#define false 0


		stdbool.h
			#ifndef STDBOOL_H
			#define STDBOOL_h

			#define bool _Bool
			#ifndef true
			  #define true 1
			#endif

			#ifndef false
			  #define false 0
			#endif

			#endif


	* C++ cette entête est inutile et neutre (par le jeu subtil de la compilation conditionnelle) car ces trois éléments sont intrinsèque à ce langage.
	  In C++, which supports those directly, the header simply contains a macro that can be used to check if the type is supported




## Difference dot (.) operator and ->

*pointervariable.foo 	 	. operator is for direct member access
							. operator has greater precedence than * operator (. is evaluated first)
(*pointervariable).foo 		Use parenthesis to change operator precedence
pointervariable.foo  		Avoid typing ()´s all time. -> is a shortcut to (*)
If you are accessing a property of an object or object reference, use 
	. 		If you are accessing a property of an object through a pointer: object.Field
	->   	syntactic sugar for a pointer dereference
			arrow dereferences a pointer (allowing access the object/memory it is pointing to pClass->Field)
			pSomething->someMember is equivalent to (*pSomething).someMember
			pointer->method() is saying 	(*pointer).method()
			foo->bar() is the same as (*foo).bar()
			*foo.bar() wouldn't work because Dot (.) operator binds stronger and is executed first.
	.* 		when the left-hand argument is a reference to an object
	->* 	when it is a pointer to an object

int score[3] = {0}; // Tableau des 3 meilleurs scores
&score[0], &score[1], &score[2]

magic  wand of dereferencing: http://www.youtube.com/watch?v=UvoHwFvAvQE




## Les pointeurs:	Variable contenant l'adresse d'une zone mémoire (autre variable…)
		Puissants par les nombreux usages possibles mais délicats.
		&variable   désigne l'adresse mémoire du pointeur
		*variable    désigne la valeur de la variable pointée
		variable	     désigne l’adresse contenant l’adresse de la variable pointée.
		int * p;
		int q=5;  p=&q;  // *p sera égal à 5
		*p=10; // q sera égal à 10
		a= (*p)+10;
		



void*
	void pointer: generic pointer type that CAN POINT TO AN OBJECT OF ANY TYPE
	Pointers to different types of objects are pretty much the same in memory and so you can use void pointers to avoid type checking, which would be useful when writing functions that handle multiple data types.
	Void pointers are more useful with C than C++. 

## Pointeur de fonction
	int (*p)(void) ;	// déclaration du pointeur de fonction  
	p=fct ;		// Initialisation du pointeur de fonction  
	p() ;		// Appel de la fonction fct()  


----


# C++

# C++

1983 - Bjarne Stroustrup
C with classes, virtual functions, templates
 
http://cpp.sh/    online shell
https://developer.nvidia.com/get-started-cuda-cc
https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/ ********
https://zestedesavoir.com/tutoriels/822/la-programmation-en-c-moderne/le-debut-du-voyage/5210_le-minimum-pour-commencer/#4-un-mot-concernant-gnu-linux

http://www.java2s.com/Code/Cpp/Class/CatalogClass.htm
https://www.codingame.com/playgrounds/53666/dpc/hello-dpc
https://www.codingame.com/playgrounds/52875/apprendre-le-c/vos-premieres-lignes-de-c

https://www.toptal.com/c-plus-plus/interview-questions


# Gems
  
  https://github.com/onelonecoder

  [Forbidden C++](https://www.youtube.com/watch?v=j0_u26Vpb4w)
    * system("pause");
    * Global variables
        #include "GlobalHeader.h"
            extern int g_MyGlobalVar;
            inline int g_MyGlobalVar;

    * Macros
        Max(a,b) → MACRO → #define Max(a,b) ( (a<b) ? b : a)
        vs
        #include <algorithm>
        std::max(...)

    * Goto
        Antipattern...but...
        if (..) goto Part1:
        if (..) goto Part2:
        Part1:
            x++;
            goto Part3; // avoid to execute Part2
        Part2:
            x--;
        Part3:
        
        for (i    
            for (j    
                for (k
                    if (.) goto Panic;   // nice way to break
        Panic:

    * Void *
        void* remove the type (can turn data in anything you want)
        void DumpToFile_v1(void a*, size_t bytes)  
        {
          std::ofstream f("dump.bin", std::ios::binary);
          f.write((char*)a, bytes);
          f.close();
          Test b = *(Test*)a;
          double b = *(double*)a;        
        }
        void DumpToFile_v2(const std::any& a, size_t bytes)  
        {
          std::ofstream f("dump.bin", std::ios::binary);
          f.write((char*)&a, bytes);
          f.close();
          Test b = std::any_cast<Test>(a);
          double b = std::any_cast<double>(a); // compil error
        }

    * Using namespace std
      namespace ns1   { void f() {std::cout << "f1"} }
      namespace ns2   { void f() {std::cout << "f1"} }
      ns1::f()

    * New and Delete
    #include <vector>
    for(int i=0; ..)
    {
      std::vector<SomeObject*> vecObjects;
      vecObjects.push_back(new SomeObject(1));
      vecObjects.push_back(new SomeObject(2));
      ...
      vecObjects.clear();  // ~ not called, mem ↑

      fix 1:
        ...
        for(auto& o: vecObjects)
            delete o;
        ...
        vecObjects.clear();  // ~ not called, mem ↑

      fix 2:
        std::vector<std::unique_ptr<SomeObject>> vecObjects;
        vecObjects.push_back(std::make_unique<SomeObject>(1));
        ...
        vecObjects.clear();  // ~ called, mem ---, no need 'delete xxx'

#include <iostream>
std::string name;
std::cout << i << std::endl;
int main() {
↑
vs
↓
#include <iostream>
using namespace std;
int main() {
cout << i << endl;

https://visualstudio.microsoft.com/fr/visual-cpp-build-tools/
  outils de génération Microsoft C++ fournissent des ensembles d’outils MSVC via un programme d’installation scriptable autonome 
  sans Visual Studio. Recommandé si vous créez des applications et des bibliothèques C++ ciblant Windows à partir de la ligne de commande
  
  https://docs.microsoft.com/en-us/cpp/build/walkthrough-compiling-a-native-cpp-program-on-the-command-line?redirectedfrom=MSDN&view=vs-2019
  Visual Studio includes a command-line C and C++ compiler. You can use it to create everything from basic console apps to Universal Windows Platform apps, Desktop apps, device drivers, and .NET components.

C libraries

  http://www.cplusplus.com/reference
  http://www.cplusplus.com/reference/cstdio/    <cstdio> (stdio.h)
  http://www.cplusplus.com/reference/cstring/   <cstring> (string.h)    to manipulate C strings and arrays
  http://www.cplusplus.com/reference/cassert/   <cassert> (assert.h)    defines one macro function that can be used as a standard debugging tool
  http://www.cplusplus.com/reference/cstdbool/

Containers

  Sequence containers:
    array              http://www.cplusplus.com/reference/array         Iterators: begin, end, cbegin, rbegin, fill, swap, []
    vector             http://www.cplusplus.com/reference/vector        arrays that can change in size. Iterators + resize, push_back, pop_back
    deque              http://www.cplusplus.com/reference/deque         Double ended queue. dynamic size sequence containers that can be expanded/contracted on both ends. Iterators + resize, push_back, push_front, pop_back
    forward_list       http://www.cplusplus.com/reference/forward_list  sequence containers that allow constant time insert and erase operations anywhere within the sequence.
    list               http://www.cplusplus.com/reference/list
  
  Container adaptors:    
    stack              http://www.cplusplus.com/reference/stack
    queue              http://www.cplusplus.com/reference/queue
    priority_queue

  Associative containers
    set                http://www.cplusplus.com/reference/set
    map                http://www.cplusplus.com/reference/map    
                       FAST LOOK UP in near constant time: O(1) in N elements: better than 2 nested 'for loops'
                       But look up in hash table should be amortized O(1)O(1) time as long 
                       as the hash function was chosen carefully. 

                      Ex: challenge LeetCode 'twosum', v3
                      https://leetcode.com/problems/two-sum/solution/

                      public int[] twoSum(int[] nums, int target) {
                            Map<Integer, Integer> map = new HashMap<>();
                            for (int i = 0; i < nums.length; i++) {
                                int complement = target - nums[i];
                                if (map.containsKey(complement)) {
                                    return new int[] { map.get(complement), i };
                                }
                                map.put(nums[i], i);
                            }
                            throw new IllegalArgumentException("No two sum solution");
                        }
  
  Unordered Associative containers
    unordered_map         http://www.cplusplus.com/reference/unordered_map
    unordered_multimap    http://www.cplusplus.com/reference/unordered_map
    unordered_set         http://www.cplusplus.com/reference/unordered_set
    unordered_multiset    http://www.cplusplus.com/reference/unordered_set

In/Out

    fstream           http://www.cplusplus.com/reference/fstream
    iomanip           http://www.cplusplus.com/reference/iomanip
    ios               http://www.cplusplus.com/reference/ios
    iosfwd            http://www.cplusplus.com/reference/iosfwd
    iostream          http://www.cplusplus.com/reference/iostream
    istream           http://www.cplusplus.com/reference/istream
    ostream           http://www.cplusplus.com/reference/ostream
    sstream           http://www.cplusplus.com/reference/sstream
    streambuf         http://www.cplusplus.com/reference/streambuf

Multi-threading
  Atomic and thread support

    atomic              https://www.cplusplus.com/reference/atomic
    thread              https://www.cplusplus.com/reference/thread
    mutex               https://www.cplusplus.com/reference/mutex
    condition_variable  https://www.cplusplus.com/reference/condition_variable
    future              https://www.cplusplus.com/reference/future

Others...
  http://www.cplusplus.com/reference/algorithm/
  http://www.cplusplus.com/reference/bitset/
  




https://www.geeksforgeeks.org/sorting-a-map-by-value-in-c-stl/?ref=leftbar-rightbar

https://medium.freecodecamp.org/some-awesome-modern-c-features-that-every-developer-should-know-5e3bf6f79a3c
https://www.topcoder.com/community/data-science/data-science-tutorials/power-up-c-with-the-standard-template-library-part-1/
https://www.oreilly.com/ideas/c++17-upgrades-you-should-be-using-in-your-code

Threading

  cuda  htt

  
  Event loop
    sometimes called a message loop, is a thread that waits for and dispatches incoming events. The thread blocks waiting for requests to arrive and then dispatches the event to an event handler function. A message queue is typically used by the loop to hold incoming messages. Each message is sequentially dequeued, decoded, and then an action is performed. Event loops are one way to implement inter-process communication.
    
    Thread Event Loop with Message Queue and Timer
    https://www.codeproject.com/Articles/1169105/Cplusplus-std-thread-Event-Loop-with-Message-Queue


LUA scripting language
  
  C++ and Lua work very well together. 
  Using Lua you can create modifiable programs by embedding it into your C++ program
  [Embedding Lua in C++](https://www.youtube.com/watch?v=4l5HdmPoynw)

Graphics: C++ GUI library

  Toute bibliothèque qui permet d’ouvrir une fenêtre, afficher des images et gérer la souris est valide. 

  * oclPixelGameEngine
    https://github.com/OneLoneCoder/olcPixelGameEngine
    https://github.com/OneLoneCoder/olcPixelGameEngine/wiki

  * SDL2
    https://www.libsdl.org/
    SDL2 semble la plus simple et légère puisque consistant en une unique DLL et n’ayant aucune dépendance.
    https://jeux.developpez.com/tutoriels/?page=prog-2d#sdl-2

  * https://www.wxwidgets.org 

    wxWidgets is an open source C++ framework allowing to write cross-platform GUI applications with native look and feel in C++ and other languages.
    [Cross Platform Graphical User Interfaces in C++](https://www.youtube.com/watch?v=FOIbK4bJKS8)
    C++ library that lets developers create applications for Windows, macOS, Linux and other platforms with a single code base. It has popular language bindings for Python, Perl, Ruby and many other languages, and unlike other cross-platform toolkits, wxWidgets gives applications a truly native look and feel because it uses the platform's native API rather than emulating the GUI. It's also extensive, free, open-source and mature.
    
    1. Download Source Code → Windows ZIP
    2. C:\tools\sdks\wxWidgets\build\msw\wx_vc16.sln   open
    3. Build → Batch Build → All → Generate
        It compil in C:\tools\sdks\wxWidgets\lib
    4. Env Vars
      Add System Variable
        WXWIN=C:\tools\sdks\wxWidgets\build\msw
    5. In solution
      Menu → Project → Propterties → All Configurations
          C/C++
            Precompiled Headers: Not using
            General → Additional Include Directories: $(WXWIN)\include;$(WXWIN)\include\msvc
             Linker → Additional Include Directories: $(WXWIN)\lib\vc_lib

    6. New Solution → Visual C++ → Windows Desktop Application
       You get a windows complex code: the native way windows is doing things
       Delete all files and do https://docs.wxwidgets.org/trunk/overview_helloworld.html
       ! update includes path in the file 
         include <"">  Use IDE paths    include "" Use current dir
             
    * https://docs.wxwidgets.org/trunk/overview_helloworld.html
    * C:\tools\sdks\wxWidgets\samples


# ENVIRONMENT
  
  Configurer la variable système OMP_NUM_THREADS:  $ setenv OMP_NUM_THREADS 8


Games
  https://bousk.developpez.com/cours/reseau-c++/Jeux/01-tictactoe/

ST3
    Ctrl-B → Build C++ files .cpp

    1. Install g++ from http://www.mingw.org/
    2. in Path, add "C:\MinGW\bin"
    3. test: g++ -v
    4. Test a file compilation

    #include <iostream>
    using namespace std;
    int main()
    {
       cout << "Hello World";
       return 0;
    }

    Save in C:\Tmp\test.cpp
    Menu Tools → Build System → C++ Single file
    CTRL+B
    ST Console: g++ "C:\Tmp\test.cpp" -o "C:\Tmp/test" && "C:\Tmp/test"
    or via cmd/ps: g++ hi.cpp -o hi.exe

VSCode
  test.c
  open FOLDER! in vscode  
  F5 ... choose C++ (GDB/LLDB)...   Need to have C/C++ Extension
  This will create launch.json
    C/C++ extension overview
      Get Started with C++ and Windows Subsystem for Linux (WSL)
      Get Started with C++ and Mingw-w64
      Get Started with C++ and Clang/LLVM on macOS
      Get Started with C++ and Microsoft C++ compiler (MSVC)
  F5 again
  configure task
    {
      // See https://go.microsoft.com/fwlink/?LinkId=733558
      // for the documentation about the tasks.json format
      "version": "2.0.0",
      "tasks": [
          {
              "label": "echo",
              "type": "shell",
              "command": "echo Hello"
          }
      ]
  }
  CTRL+SHIFT+B
  

  !! !! select the .c file before doing CTRL-SHIFT-B !!!
  {
      // See https://go.microsoft.com/fwlink/?LinkId=733558
      // for the documentation about the tasks.json format
      "version": "2.0.0",
      "tasks": [
          {
              "label": "Compile C File",
              "type": "shell",
              "command": "gcc ${file} -g -o ${fileBasename}.exe",              or C:\\mingw-w64\\...\\bin\\gcc if gcc not in path
              "group": {
                  "kind": "build",               = CTRL+SHIFT+B
                  "isDefault": true
              }
          }
      ]
  }

  Debug: to log paths/files: 
  !! !! select the .c file before doing CTRL-SHIFT-B !!!
    {
        // See https://go.microsoft.com/fwlink/?LinkId=733558
        // for the documentation about the tasks.json format
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Compile C File",
                "type": "shell",
                "command": "echo ${file}${fileBasename}.exe",   → c:\Temp\c\myapp.c    myapp.c.exe
                  "options": {
                          "cwd": "${fileDirname}"                
                      },
                "group": {
                    "kind": "build",
                    "isDefault": true
                }
            }
        ]
    }

  tasks.json
    {
          // See https://go.microsoft.com/fwlink/?LinkId=733558
          // for the documentation about the tasks.json format
          // https://code.visualstudio.com/docs/editor/variables-reference
          // https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html
          "version": "2.0.0",
          "tasks": [
              {
                  "label": "Compile C File",
                  "type": "shell",
                  "command": "C:\\mingw-w64\\x86_64-8.1.0-win32-seh-rt_v6-rev0\\mingw64\\bin\\gcc ${file} sqlite3.dll ocilibw.dll ociliba.dll -Wall -O3 -g -o ${file}.exe",
                  "options": {
                      "cwd": "${fileDirname}"                
                  },
                  "group": {
                      "kind": "build",           = CTRL+SHIFT+B
                      "isDefault": true
                  }
              },
            
              {
                  "label": "Compile C File V0",
                  "type": "shell",
                  "command": "gcc",
                  "args": [
                      "-g",
                      "${file}",
                      "-o",
                      "${workspaceRoot}\\${fileBasename}.exe"
                  ],
                  "group": {
                      "kind": "build",
                      "isDefault": false
                  }
              },

              {
                  "label": "Run C File",
                  "type": "shell",
                  "command": "${file}.exe",
                  "args": [
                      "c:\\out\\db3\\out\\2014"
                  ]
              }
          ]
      }

  launch.json
    {
      // Use IntelliSense to learn about possible attributes.
      // Hover to view descriptions of existing attributes.
      // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
      "version": "0.2.0",
      "configurations": [
          
          {
              "name": "(gdb) Launch",
              "type": "cppdbg",
              "request": "launch",
              "program": "${file}.exe",            
              //"args": ["c:\\out\\data\\imports\\contrats.sqlite3", "select * from contrats"],             
              "args": ["c:\\out\\data\\imports\\001_01_2014-31_12_2018_France.sqlite3", "select name, age, email from clients"],
              "stopAtEntry": false,
              "cwd": "${workspaceFolder}",
              "environment": [],
              "externalConsole": true,
              "MIMode": "gdb",
              "miDebuggerPath": "C:\\mingw-w64\\x86_64-8.1.0-win32-seh-rt_v6-rev0\\mingw64\\bin\\gdb.exe", // "miDebuggerPath2": "C:\\mingw-w64\\x86_64-8.1.0-win32-seh-rt_v6-rev0\\mingw64\\bin\\gdb.exe",
              "setupCommands": [
                  {
                      "description": "Enable pretty-printing for gdb",
                      "text": "-enable-pretty-printing",
                      "ignoreFailures": false
                  }
              ]
          }
      ]
  }




# C++ QUICK REFERENCE / C++ CHEATSHEET  
Based on Phillip M. Duxbury's C++ Cheatsheet and edited by Morten Nobel-Jørgensen. The cheatsheet focus is on C++ - not on the library. C++11 additions is inspired by ISOCPP.org C++11 Cheatsheet).  
  
The goal is to give a concise overview of basic, modern C++.  
  
The document is hosted on https://github.com/mortennobel/cpp-cheatsheet. Any comments and feedback are appreciated.  
  
### PREPROCESSOR  
// Comment to end of line    
/* Multi-line comment */   
#include  <stdio.h>         // Insert standard header file
#include "myfile.h"         // Insert file in current directory
#define X some text         // Replace X with some text
#define F(a,b) a+b          // Replace F(1,2) with 1+2
#define X \  
 some text                  // Multiline definition  
#undef X                    // Remove definition  
#if defined(X)              // Condional compilation (#ifdef X) 
#else                       // Optional (#ifndef X or #if !defined(X)) 
#endif                      // Required after #if, #ifdef 
  
### LITERALS  
255, 0377, 0xff             // Integers (decimal, octal, hex)   
2147483647L, 0x7fffffffl    // Long (32-bit) integers   
123.0, 1.23e2               // double (real) numbers   
'a', '\141', '\x61'         // Character (literal, octal, hex)   
'\n', '\\', '\'', '\"'      // Newline, backslash, single quote, double quote   
"string\n"                  // Array of characters ending with newline and \0   
"hello" "world"             // Concatenated strings  
true, false                 // bool constants 1 and 0   
nullptr                     // Pointer type with the address of 0   
  
### DECLARATIONS  
int x;                      // Declare x to be an integer (value undefined)   
int x=255;                  // Declare and initialize x to 255   
short s; long l;            // Usually 16 or 32 bit integer (int may be either)   
char c='a';                 // Usually 8 bit character   
unsigned char u=255;   
signed char s=-1;           // char might be either   
unsigned long x =   
  0xffffffffL;              // short, int, long are signed   
float f; double d;          // Single or double precision real (never unsigned)   
bool b=true;                // true or false, may also use int (1 or 0)   
int a, b, c;                // Multiple declarations   
int a[10];                  // Array of 10 ints (a[0] through a[9])   
int a[]={0,1,2};            // Initialized array (or a[3]={0,1,2}; )   
int a[2][2]={{1,2},{4,5}};  // Array of array of ints   
char s[]="hello";           // String (6 elements including '\0')  
std::string s = "Hello"     // Creates string object with value "Hello"  
std::string s = R"(Hello  
World)";                    // Creates string object with value "Hello\nWorld"  
int* p;                     // p is a pointer to (address of) int   
char* s="hello";            // s points to unnamed array containing "hello"   
void* p=nullptr;            // Address of untyped memory (nullptr is 0)   
int& r=x;                   // r is a reference to (alias of) int x   
enum weekend {SAT,SUN};     // weekend is a type with values SAT and SUN   
enum weekend day;           // day is a variable of type weekend   
enum weekend{SAT=0,SUN=1};  // Explicit representation as int   
enum {SAT,SUN} day;         // Anonymous enum  
enum class Color {Red,Blue};// Color is a strict type with values Red and Blue  
Color x = Color::Red;       // Assign Color x to red  
typedef String char*;       // String s; means char* s;   
const int c=3;              // Constants must be initialized, cannot assign to   
const int* p=a;             // Contents of p (elements of a) are constant   
int* const p=a;             // p (but not contents) are constant   
const int* const p=a;       // Both p and its contents are constant   
const int& cr=x;            // cr cannot be assigned to change x   
int8_t,uint8_t,int16_t,  
uint16_t,int32_t,uint32_t,  
int64_t,uint64_t            // Fixed length standard types  
auto it = m.begin();        // Declares it to the result of m.begin()   
auto const param = config["param"];  
                            // Declares it to the const result  
auto& s = singleton::instance();  
                            // Declares it to a reference of the result  
  
### STORAGE CLASSES  
int x;                      // Auto (memory exists only while in scope)   
static int x;               // Global lifetime even if local scope   
extern int x;               // Information only, declared elsewhere   
  
### STATEMENTS  
x=y;                        // Every expression is a statement   
int x;                      // Declarations are statements   
;                           // Empty statement   
{                           // A block is a single statement   
  int x;                    // Scope of x is from declaration to end of block   
}  
if (x) a;                   // If x is true (not 0), evaluate a   
else if (y) b;              // If not x and y (optional, may be repeated)   
else c;                     // If not x and not y (optional)   
  
while (x) a;                // Repeat 0 or more times while x is true   
  
for (x; y; z) a;            // Equivalent to: x; while(y) {a; z;}   
  
for (x : y) a;              // Range-based for loop e.g.  
                            // for (auto& x in someList) x.y();  
  
do a; while (x);            // Equivalent to: a; while(x) a;   
  
switch (x) {                // x must be int   
  case X1: a;               // If x == X1 (must be a const), jump here   
  case X2: b;               // Else if x == X2, jump here   
  default: c;               // Else jump here (optional)   
}   
break;                      // Jump out of while, do, or for loop, or switch   
continue;                   // Jump to bottom of while, do, or for loop   
return x;                   // Return x from function to caller   
try { a; }    
catch (T t) { b; }          // If a throws a T, then jump here   
catch (...) { c; }          // If a throws something else, jump here   
  
### FUNCTIONS  

https://www.modernescpp.com/index.php/c-20-coroutines-the-first-overview

int f(int x, int);          // f is a function taking 2 ints and returning int  
void f();                   // f is a procedure taking no arguments   
void f(int a=0);            // f() is equivalent to f(0)   
f();                        // Default return type is int   
inline f();                 // Optimize for speed   
f() { statements; }         // Function definition (must be global)   
T operator+(T x, T y);      // a+b (if type T) calls operator+(a, b)   
T operator-(T x);           // -a calls function operator-(a)   
T operator++(int);          // postfix ++ or -- (parameter ignored)   
extern "C" {void f();}      // f() was compiled in C   
Function parameters and return values may be of any type. A function must either be declared or defined before it is used. It may be declared first and defined later. Every program consists of a set of a set of global variable declarations and a set of function definitions (possibly in separate files), one of which must be:  
  
int main()  { statements... }     or   
int main(int argc, char* argv[]) { statements... }   
argv is an array of argc strings from the command line. By convention, main returns status 0 if successful, 1 or higher for errors.  
  
Functions with different parameters may have the same name (overloading). Operators except :: . .* ?: may be overloaded. Precedence order is not affected. New operators may not be created.  
  

# Evolution of Functions

  // functionEvolution.cpp

  int func1() {
      return 1972;
  }

  int func2(int arg) {
      return arg;
  }

  double func2(double arg) {
      return arg;
  }

  template <typename T>
  T func3(T arg) {
      return arg;
  }

  struct FuncObject4 {
      int operator()() { // (1)
          return 1998;
      }
  };

  auto func5 = [] {
      return 2011;
  };

  auto func6 = [] (auto arg){
      return arg;
  };

  int main() {

      func1();        // 1972

      func2(1998);    // 1998
      func2(1998.0);  // 1998.0
      func3(1998);    // 1998
      func3(1998.0);  // 1998.0
      FuncObject4 func4;
      func4();        // 1998

      func5();        // 2011

      func6(2014);    // 2014
      func6(2014.0);  // 2014

  } 

  * Since the first C standard in 1972, we have functions: func1.
  * With the first C++ standard in 1998 functions become way more powerful. We got
    Function overloading: func2.
    Function templates: func3.
    Function objects: func4. Often, they are erroneous, called functors. Function objects are due to the overload call operator (operator ()) objects, which can be invoked. The second pair of round braces in line (1) stands for the function call parameters.
  * C++11 gave us lambda functions: func5.
  * With C++14, lambda functions can be generic: func6. 
  * One step further. Generators are special coroutines.

# GENERATORS

  // GREEDYGENERATOR.CPP
  #include <iostream>
  #include <vector>

  std::vector<int> getNumbers(int begin, int end, int inc = 1) {
      std::vector<int> numbers;
      for (int i = begin; i < end; i += inc) { numbers.push_back(i); }
      return numbers;
  }

  int main() {
      std::cout << std::endl;
      const auto numbers= getNumbers(-10, 11);
      for (auto n: numbers) std::cout << n << " ";
      std::cout << "\n\n";
      for (auto n: getNumbers(0, 101, 5)) std::cout << n << " ";
      std::cout << "\n\n";
  }
  // NOTES
  // getNumbers() job could be done with the algorithm std::iota https://en.cppreference.com/w/cpp/algorithm/iota
  *  The vector 'numbers" always gets all values. 
      This holds even if I’m only interested in the first five elements of a vector 
      with 1000 elements
  * Easy to transform the function getNumbers into a lazy generator:



  // LAZYGENERATOR.CPP
  #include <iostream>
  #include <vector>

  generator<int> generatorForNumbers(int begin, int inc = 1) {
    for (int i = begin;; i += inc) { co_yield i; }
  }

  int main() {
      std::cout << std::endl;
      const auto numbers= generatorForNumbers(-10);                   // (2)
      for (int i= 1; i <= 20; ++i) std::cout << numbers << " ";       // (4)
      std::cout << "\n\n";
      for (auto n: generatorForNumbers(0, 5)) std::cout << n << " ";  // (3)
      std::cout << "\n\n";
  }

  // NOTES
  While the function getNumbers in the file greedyGenerator.cpp returns a std::vector, 
  the coroutine generatorForNumbers in lazyGenerator.cpp returns a generator. 
  The generator numbers in line (2) or generatorForNumbers(0, 5) in line (3) returns 
  a new number on request. 
  The range-based for-loop triggers the query. 
  To be more precise, the query of the coroutine returns the value i via co_yield i 
  and immediately suspends its execution. If a new value is requested, 
  the coroutine resumes its execution exactly at that place. 
  
  The expression generatorForNumbers(0, 5) in line (3) is a just-in-place usage 
  of a generator. I want to stress one point explicitly. 
  The coroutine generatorForNumbers creates an infinite data stream because the 
  for-loop in line (3) has no end condition. 
  This infinite data stream is fine if I only ask for a finite number of values such as in line (4).
  This does not hold for line (3) since there is no end condition. 
  Consequentially, the expression runs forever.

# COROUTINES (Evolution of functions)

  https://en.cppreference.com/w/cpp/language/coroutines
  https://www.modernescpp.com/index.php/c-20-coroutines-the-first-overview

  Coroutines are functions that can suspend and resume their execution while keeping their state.     
  a function that can suspend execution to be resumed later. 
  Coroutines are stackless: they suspend execution by returning to the caller and the data that is required to resume execution is stored separately from the stack. This allows for sequential code that executes asynchronously (e.g. to handle non-blocking I/O without explicit callbacks), and also supports algorithms on lazy-computed infinite sequences and other uses.

  With the new keywords co_await and co_yield, C++20 extends the execution of C++ functions with two new concepts.
  Thanks to co_await expression expression, it is possible to suspend and resume the execution of the an expression. If you use co_await expression in a function func, the call auto getResult = func() does not block if the result of the function is not available. Instead of resource-consuming blocking, you have resource-friendly waiting.
  co_yield expression expression allows it to write a generator function. The generator function returns a new value each time. A generator function is a kind of data stream from which you can pick values. The data stream can be infinite. Consequentially, we are in the center of lazy evaluation.


  A function is a coroutine if its definition does any of the following:

    uses the co_await operator to suspend execution until resumed
    task<> tcp_echo_server() {
      char data[1024];
      for (;;) {
        size_t n = co_await socket.async_read_some(buffer(data));
        co_await async_write(socket, buffer(data, n));
      }
    }
    uses the keyword co_yield to suspend execution returning a value
    generator<int> iota(int n = 0) {
      while(true)
        co_yield n++;
    }
    uses the keyword co_return to complete execution returning a value
    lazy<int> f() {
      co_return 7;
    }
    Every coroutine must have a return type that satisfies a number of requirements, noted below.






### EXPRESSIONS  
Operators are grouped by precedence, highest first. Unary operators and assignment evaluate right to left. All others are left to right. Precedence does not affect order of evaluation, which is undefined. There are no run time checks for arrays out of bounds, invalid pointers, etc.  
  
T::X                        // Name X defined in class T   
                                struct Foo { static void foo() {} };
                                Equivalents:   Foo::foo();    Foo().foo();

N::X                        // Name X defined in namespace N   
                                #include <iostream>
                                std::string name;
                                std::cout << i << std::endl;
                                int main() {
                                ↑
                                vs
                                ↓
                                #include <iostream>
                                using namespace std;
                                int main() {
                                cout << i << endl;

::X                         // Global name X  
                                int tuna = 69; // global variable/global scope
                                int main()
                                {    
                                    
                                    int tuna = 20; // local variable/local scope
                                    cout << tuna << endl; // local tuna
                                    cout << ::tuna << endl; // accessing global tuna using the unary scope resolution operator (::)

  
t.x                         // Member x of struct or class t   
p->x                        // Member x of struct or class pointed to by p  
a[i]                        // i'th element of array a   
f(x,y)                      // Call to function f with arguments x and y   
T(x,y)                      // Object of class T initialized with x and y   
x++                         // Add 1 to x, evaluates to original x (postfix)   
x--                         // Subtract 1 from x, evaluates to original x   
typeid(x)                   // Type of x   
typeid(T)                   // Equals typeid(x) if x is a T   
dynamic_cast< T>(x)         // Converts x to a T, checked at run time   
static_cast< T>(x)          // Converts x to a T, not checked   
reinterpret_cast< T>(x)     // Interpret bits of x as a T   
const_cast< T>(x)           // Converts x to same type T but not const   
  
sizeof x                    // Number of bytes used to represent object x   
sizeof(T)                   // Number of bytes to represent type T   
++x                         // Add 1 to x, evaluates to new value (prefix)   
--x                         // Subtract 1 from x, evaluates to new value   
~x                          // Bitwise complement of x   
!x                          // true if x is 0, else false (1 or 0 in C)   
-x                          // Unary minus   
+x                          // Unary plus (default)   
&x                          // Address of x   
*p                          // Contents of address p (*&x equals x)   
new T                       // Address of newly allocated T object   
new T(x, y)                 // Address of a T initialized with x, y   
new T[x]                    // Address of allocated n-element array of T   
delete p                    // Destroy and free object at address p   
delete[] p                  // Destroy and free array of objects at p   
(T) x                       // Convert x to T (obsolete, use .._cast<T>(x))   
  
x * y                       // Multiply   
x / y                       // Divide (integers round toward 0)   
x % y                       // Modulo (result has sign of x)   
  
x + y                       // Add, or \&x[y]   
x - y                       // Subtract, or number of elements from *x to *y   
x << y                      // x shifted y bits to left (x * pow(2, y))   
x >> y                      // x shifted y bits to right (x / pow(2, y))   
  
x < y                       // Less than   
x <= y                      // Less than or equal to   
x > y                       // Greater than   
x >= y                      // Greater than or equal to   
  
x & y                       // Bitwise and (3 & 6 is 2)   
x ^ y                       // Bitwise exclusive or (3 ^ 6 is 5)   
x | y                       // Bitwise or (3 | 6 is 7)   
x && y                      // x and then y (evaluates y only if x (not 0))   
x || y                      // x or else y (evaluates y only if x is false (0))   
x = y                       // Assign y to x, returns new value of x   
x += y                      // x = x + y, also -= *= /= <<= >>= &= |= ^=   
x ? y : z                   // y if x is true (nonzero), else z   
throw x                     // Throw exception, aborts if not caught   
x , y                       // evaluates x and y, returns y (seldom used)   
  
### CLASSES  
class T {                   // A new type   
private:                    // Section accessible only to T's member functions  
protected:                  // Also accessable to classes derived from T   
public:                     // Accessable to all   
    int x;                  // Member data   
    void f();               // Member function   
    void g() {return;}      // Inline member function   
    void h() const;         // Does not modify any data members  
    int operator+(int y);   // t+y means t.operator+(y)   
    int operator-();        // -t means t.operator-()   
    T(): x(1) {}            // Constructor with initialization list   
    T(const T& t): x(t.x) {}// Copy constructor   
    T& operator=(const T& t)  
    {x=t.x; return *this; } // Assignment operator   
    ~T();                   // Destructor (automatic cleanup routine)   
    explicit T(int a);      // Allow t=T(3) but not t=3  
    T(float x): T((int)x) {}// Delegate contructor to T(int)  
    operator int() const   
    {return x;}             // Allows int(t)   
    friend void i();        // Global function i() has private access   
    friend class U;         // Members of class U have private access   
    static int y;           // Data shared by all T objects   
    static void l();        // Shared code.  May access y but not x   
    class Z {};             // Nested class T::Z   
    typedef int V;          // T::V means int   
};  
void T::f() {               // Code for member function f of class T   
    this->x = x;}           // this is address of self (means x=x;)   
int T::y = 2;               // Initialization of static member (required)   
T::l();                     // Call to static member  
T t;                        // Create object t implicit call constructor  
t.f();                      // Call method f on object t  
   
struct T {                  // Equivalent to: class T { public:   
  virtual void i();         // May be overridden at run time by derived class  
  virtual void g()=0; };    // Must be overridden (pure virtual)  
class U: public T {         // Derived class U inherits all members of base T  
                            The only difference between a class and struct are the access modifiers. 
                                Struct members are public by default: use structs when you have a simple data object (no methods)
                                class members are private: use classes when you need an object that has methods 
  public:  
  void g(int) override; };  // Override method g   
class V: private T {};      // Inherited members of T become private   
class W: public T, public U {};    
                            // Multiple inheritance  
class X: public virtual T {};   
                            // Classes derived from X have base T directly   
All classes have a default copy constructor, assignment operator, and destructor, which perform the corresponding operations on each data member and each base class as shown above. There is also a default no-argument constructor (required to create arrays) if the class has no constructors. Constructors, assignment, and destructors do not inherit.  
  
### TEMPLATES (modèles de classe) 

pour la généralisation, l'abstraction et la réutilisation du code en C++.
permet aux classes d'être abstraites en ce sens qu'elles ne savent pas quel type de données sera transmis et traité par ses opérations. Un modèle ne dépend pas des caractéristiques d'un type de données particulier ; l'accent est plutôt mis sur la logique.

La classe de modèle std:vector est un exemple fourni par la STL. Elle est générique car un vecteur de n'importe quel type de données peut être instancié. Cette capacité permet une réutilisation efficace du code et, par conséquent, l'ensemble du système est plus facile à mettre en œuvre et à maintenir.

template <class T> T f(T t);// Overload f for all types   
template <class T> class X {// Class with type parameter T   
  X(T t); };                // A constructor   
template <class T> X<T>::X(T t) {}  
                            // Definition of constructor   
X<int> x(3);                // An object of type "X of int"   
template <class T, class U=T, int n=0>  
                            // Template with default parameters   
      
make sure a C++ function can be called as e.g. void foo(int, int) but not as any other type like void foo(long, long)
  void foo(int a, int b) {
  // whatever
  }

  …and delete all others through a template:
  template <typename T1, typename T2> void foo(T1 a, T2 b) = delete;
  Or without the delete keyword:

  template <class T, class U> 
  void f(T arg1, U arg2);

  template <>
  void f(int arg1, int arg2)
  {
      //...    
  }

### NAMESPACES  
namespace N {class T {};}   // Hide name T  
N::T t;                     // Use name T in namespace N   
using namespace N;          // Make T visible without N::   
  
### MATH.H, CMATH (Floating point math)  
#include <cmath>            // Include cmath (std namespace)  
sin(x); cos(x); tan(x);     // Trig functions, x (double) is in radians   
asin(x); acos(x); atan(x);  // Inverses  
atan2(y, x);                // atan(y/x)   
sinh(x); cosh(x); tanh(x);  // Hyperbolic   
exp(x); log(x); log10(x);   // e to the x, log base e, log base 10   
pow(x, y); sqrt(x);         // x to the y, square root   
ceil(x); floor(x);          // Round up or down (as a double)   
fabs(x); fmod(x, y);        // Absolute value, x mod y  
ASSERT.H, CASSERT (Debugging aid)  
#include <cassert>        // Include iostream (std namespace)  
assert(e);                // If e is false, print message and abort   
#define NDEBUG            // (before #include <assert.h>), turn off assert   
  
### IOSTREAM.H, IOSTREAM (Replaces stdio.h)  
#include <iostream>         // Include iostream (std namespace)  
cin >> x >> y;              // Read words x and y (any type) from stdin   
cout << "x=" << 3 << endl;  // Write line to stdout   
cerr << x << y << flush;    // Write to stderr and flush   
c = cin.get();              // c = getchar();   
cin.get(c);                 // Read char   
cin.getline(s, n, '\n');    // Read line into char s[n] to '\n' (default)   
if (cin)                    // Good state (not EOF)?   
                            // To read/write any type T:   

  #include <iostream>
  std::string name;
  std::cout << "What is your name? ";
  getline (std::cin, name);
  std::cout << "Hello, " << name << "!\n";

istream& operator>>(istream& i, T& x) {i >> ...; x=...; return i;}   
ostream& operator<<(ostream& o, const T& x) {return o << ...;}   
FSTREAM.H, FSTREAM (File I/O works like cin, cout as above)  
#include <fstream>          // Include filestream (std namespace)  
ifstream f1("filename");    // Open text file for reading   
if (f1)                     // Test if open and input available   
  f1 >> x;                  // Read object from file   
f1.get(s);                  // Read char or line   
f1.getline(s, n);           // Read line into string s[n]   
ofstream f2("filename");    // Open file for writing   
if (f2) f2 << x;            // Write to file   
STRING (Variable sized character array)  
#include <string>         // Include string (std namespace)  
string s1, s2="hello";    // Create strings   
s1.size(), s2.size();     // Number of characters: 0, 5   
s1 += s2 + ' ' + "world"; // Concatenation   
s1 == "hello world"       // Comparison, also <, >, !=, etc.   
s1[0];                    // 'h'   
s1.substr(m, n);          // Substring of size n starting at s1[m]   
s1.c_str();               // Convert to const char*   
s1 = to_string(12.05);    // Converts number to string  
getline(cin, s);          // Read line ending in '\n'   




# CONTENERS

En plus de la fonctionnalité de tableau intégrée dans le langage, la STL prévoit un certain nombre de classes de conteneurs. Deux d'entre elles sont List (std::list) et Vector (std::vector).
Le vecteur est stocké dans des emplacements mémoire contigus comme un tableau. Une liste, en revanche, est stockée en interne sous la forme d'une liste doublement liée.
structure de données dynamique:

# std::list

1. L'insertion ou la suppression à un point quelconque (début, milieu, fin) ne nécessite que la modification de quelques pointeurs. Lors de l'insertion, il faudra bien sûr allouer une nouvelle mémoire à l'élément entrant.
2. L'accès aléatoire n'est pas possible dans une liste. Pour accéder aux tâches de l'exemple précédent, les tâches [12], il faut commencer au début de la liste et parcourir les 11 premiers éléments un par un.
3. Les itérateurs ne sont pas invalidés par l'insertion ou la suppression de listes car aucun élément n'est déplacé de sa position.
4. Les itérateurs d'accès aléatoire sont par défaut non valables pour les listes. Par conséquent, des fonctions personnalisées utilisant des itérateurs d'accès non aléatoires doivent être mises en œuvre. En raison de la fréquence de tri des listes, cette fonctionnalité fait partie de la STL :
std::sort(..) ne fonctionne pas pour les listes ; cependant, std::list::sort() fait partie de la STL

# std::vector  
### VECTOR (Variable sized array/stack with built in memory allocation)  

1. L'insertion et la suppression sont coûteuses car :
Si l'un ou l'autre se trouve au milieu de la liste, tous les éléments doivent être déplacés, soit pour faire de la place, soit pour libérer l'espace non utilisé.
Si un élément est ajouté à la fin, il peut nécessiter une nouvelle allocation de la mémoire et la copie de tous les éléments.
2. Les itérateurs C++ peuvent être invalidés.
3. L'accès aléatoire est à la fois possible et efficace, grâce à l'opérateur de tableau (ex : tasks [12]).
D'autres algorithmes STL qui nécessitent des itérateurs à accès aléatoire peuvent être utilisés sans risque avec la classe de vecteur. Un exemple est std::sort(...), qui sur un vecteur peut être appelé : std::sort(monVecteur.début(), monVecteur.fin()) ;

http://www.java2s.com/Code/Cpp/Vector/CatalogVector.htm

#include <vector>         // Include vector (std namespace)  
vector<int> a(10);        // a[0]..a[9] are int (default size is 0)   
vector<int> b{1,2,3};        // Create vector with values 1,2,3  
a.size();                 // Number of elements (10)   
a.push_back(3);           // Increase size to 11, a[10]=3  
a.back()=4;               // a[10]=4;   
a.pop_back();             // Decrease size by 1   
a.front();                // a[0];   
a[20]=1;                  // Crash: not bounds checked   
a.at(20)=1;               // Like a[20] but throws out_of_range()   
for (int& p : a)   
  p=0;                    // C++11: Set all elements of a to 0  
for (vector<int>::iterator p=a.begin(); p!=a.end(); ++p)   
  *p=0;                   // C++03: Set all elements of a to 0   
vector<int> b(a.begin(), a.end());  // b is copy of a  
vector<T> c(n, x);        // c[0]..c[n-1] init to x   
T d[10]; vector<T> e(d, d+10);      // e is initialized from d   
  

std::vector<Ant*> ants;
for (int i = 0; i < num_ants; ++i) {
    ants.push_back(new Ant());
}

// Display vector elements using const_iterator
typename vector< T >::const_iterator constIterator;
for (constIterator = integers2.begin(); constIterator != integers2.end(); ++constIterator )
  cout << *constIterator << ' ';

 for (set<string>::const_iterator p = setStr.begin( );p != setStr.end( ); ++p)
      cout << *p << endl;


 // for_each. http://www.java2s.com/Code/Cpp/STL-Algorithms-Non-modifying-sequence-operations
 int a2[ 10 ] = { 100, 2, 8, 1, 50, 3, 8, 8, 9, 10 };
   std::vector< int > v2( a2, a2 + 10 ); // copy of a2
   cout << "Vector v2 contains: ";
   std::copy( v2.begin(), v2.end(), output );

   // output square of every element in v
   cout << "\n\nThe square of every integer in Vector v is:\n";
   std::for_each( v2.begin(), v2.end(), outputSquare );

   cout << endl;
   return 0;
}
void outputSquare( int value ) { cout << value * value << ' '; }



use the four-argument version of std::accumulate, and provide your own function which does the calculations properly
dMean = std::accumulate(
    m_vectorData.begin(), m_vectorData.end(), 0.0,
    [] (const double acc, const CData* data) { return acc + data->getData(); }
);



   Vector<int> x(5);   // Génère un vecteur pour stocker cinq entiers
   for (int i = 0; i < 5; ++i)
      x[i] = i;              //  Initialise le vecteur.


vector<int> vector1(5);
for (int i=0; i < 5; ++i)
    vector1[i] = i;
random_shuffle(vector1.begin(), vector1.end());
// Sort vector1 using push_heap and pop_heap:
for (int i = 2; i < 5; ++i)    
  push_heap(vector1.begin(), vector1.begin() + i);
for (int i = 5; i >= 2; --i)
  pop_heap(vector1.begin(), vector1.begin() + i);


vector<string> vec1;
string line;
vec1.clear();
ifstream infile("stl2in.txt");
while (getline(infile,line,'\n'))
{
  vec1.push_back (line);
}

  std::vector<int> vec {,2,3,4,5,6,7,8,9};
  std::vector<std::string> str {"Programming", "in", "a", "functional", "style"};
  std::transform(vec.begin(), vec.end(), vec.begin(), [](int i) {return i*i;} );
  auto it = std::remove_if(vec.begin(), vec.end(), [](int i) {return (i<3) or (i>8);} );     // 3 4 5 6 7 8
  auto it2 = std::remove_if(str.begin(), str.end(), [](string s) {return (std::lower(s[0])); // Programming
  std::accumulate(vec.begin(), vec.end(), [](int a, int b) { return a*b}); // 362880
  std::accumulate(str.begin(), str.end(), [](string a, string b) { return a + ":" + b}); // "Programming:in:a:functionale:style"
  I apply in the code snippet two powerful features of functional programming. 
  Both are now mainstream in modern C++: automatic type deduction with auto and lambda-functions.
  

http://stackoverflow.com/questions/6679096/using-find-if-on-a-vector-of-object

http://stackoverflow.com/questions/22713278/accumulate-through-a-vector-of-pointers
http://stackoverflow.com/questions/5914012/use-stl-find-if-to-find-a-specific-object-in-a-vector-of-object-pointers
http://stackoverflow.com/questions/5295616/how-to-deallocate-object-pointer-in-vector
http://www.java2s.com/Code/Cpp/Vector/Callmemberfunctionforeachelementinvector.htm

    vector<Widget> vw(500000);
    while (vw.size() < vw.capacity())
        vw.push_back(Widget());

    cout << "Size of vw: " << vw.size() << endl;

### DEQUE (array/stack/queue)  
deque is like vector<T>, but also supports:  
  
#include <deque>          // Include deque (std namespace)  
a.push_front(x);          // Puts x at a[0], shifts elements toward back   
a.pop_front();            // Removes a[0], shifts toward front   
  
### UTILITY (Pair)  
#include <utility>        // Include utility (std namespace)  
pair<string, int> a("hello", 3);  // A 2-element struct   
a.first;                  // "hello"   
a.second;                 // 3   
  
### MAP (associative array - usually implemented as red-black trees)  
#include <map>            // Include map (std namespace)  
map<string, int> a;       // Map from string to int   
a["hello"]=3;             // Add or replace element a["hello"]   
for (auto& p:a)   
  cout << p.first << p.second;  // Prints hello, 3  
a.size();                 // 1  
  
### ALGORITHM (A collection of 60 algorithms on sequences with iterators)  
#include <algorithm>      // Include algorithm (std namespace)   
min(x, y); max(x, y);     // Smaller/larger of x, y (any type defining <)   
swap(x, y);               // Exchange values of variables x and y   
sort(a, a+n);             // Sort array a[0]..a[n-1] by <   
sort(a.begin(), a.end()); // Sort vector or deque   










#include <iostream>
#include <math.h>

// function to add the elements of two arrays
void add(int n, float *x, float *y)
{
  for (int i = 0; i < n; i++)
      y[i] = x[i] + y[i];
}

int main(void)
{
  int N = 1<<20; // 1M elements

  float *x = new float[N];
  float *y = new float[N];

  // initialize x and y arrays on the host
  for (int i = 0; i < N; i++) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }

  // Run kernel on 1M elements on the CPU
  add(N, x, y);

  // Check for errors (all values should be 3.0f)
  float maxError = 0.0f;
  for (int i = 0; i < N; i++)
    maxError = fmax(maxError, fabs(y[i]-3.0f));
  std::cout << "Max error: " << maxError << std::endl;

  // Free memory
  delete [] x;
  delete [] y;

  return 0;
}




C++ is an enhanced version of the C language. C++ includes everything that is part of C and adds support for object-oriented programming (OOP). In addition, C++ also contains many improvements and features that make it a “better C”, independent of object oriented programming.

C++ is actually an extensible language since we can define new types in such a way that they act just like the predefined types which are part of the standard language.

1970 C 
  * Procedural
  * Structured
  In C you think in procedures and structures. 
1998 the first C++ standard was published. a new kind of abstraction. 
* object-orientation 
      Encapsulation
      An object encapsulates its attributes and methods and provides them via an interface to the outside world. This property that an object hides its implementation is often called data hiding.

      Inheritance
      A derived class get all characteristics from its base class. You can use an instance of a derived class as an instance of its base class. We often speak about code reuse because the derived class automatically gets all characteristics of the base class .

      Polymorphism
      Polymorphism is the ability to present the same interface for differing underlying data types. The term is from Greek and stands for "many forms"

      class HumanBeing {
        public HumanBeing(std::string n) : name(n) {} 
        virtual std::string getName() const{  return name; }
        private:
        std::string name; 
      }
      class Man   : public HumanBeing{}; 
      class Woman : public HumanBeing{}; 


* generic programming 
define families of functions or classes. By providing the concrete type you get automatically a function or a class for this type. 

13 years later the area of modern C++ began with C++11. 
  * functional programming style.
  typical functions in functional programming: filter, map, reduce. These are the functions std::transform, std::remove_if, and std::accumulate.
   https://www.linkedin.com/pulse/evolution-c-rainer-grimm

  std::vector<int> vec {,2,3,4,5,6,7,8,9};
  std::vector<std::string> str {"Programming", "in", "a", "functional", "style"};
  std::transform(vec.begin(), vec.end(), vec.begin(), [](int i) {return i*i;} );
  auto it = std::remove_if(vec.begin(), vec.end(), [](int i) {return (i<3) or (i>8);} );     // 3 4 5 6 7 8
  auto it2 = std::remove_if(str.begin(), str.end(), [](string s) {return (std::lower(s[0])); // Programming
  std::accumulate(vec.begin(), vec.end(), [](int a, int b) { return a*b}); // 362880
  std::accumulate(str.begin(), str.end(), [](string a, string b) { return a + ":" + b}); // "Programming:in:a:functionale:style"
  I apply in the code snippet two powerful features of functional programming. 
  Both are now mainstream in modern C++: automatic type deduction with auto and lambda-functions.
   
  # auto 
      le compilateur détermine le type de variable.
      auto simple = 5.5 ; // Simple sera un flottant
      auto count = 2 ;    // Count sera un entier
      déclare un type de variable simplifie le codage, accélère le temps de développement et entraîne moins de bogues. 
      Son utilisation devrait être naturelle pour les programmeurs C++ modernes.

      From C++14
        auto testFunction()     // peut être utilisé pour déclarer un type de déclaration.
        {
        return 5;           // The return value will be an integer
        }

http://www.modernescpp.com/index.php

[codingunit.com](http://www.codingunit.com/cplusplu-tutorial-constants-escape-codes-and-strings)
http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#S-interfaces
[C++ Programming Examples](https://www.geekboots.com/cpp)


## libraries
#include <stdio.h>        in/out functions. low-level access to a file, both in binary or text mode.
#include <string.h>       string functions
#include <stdlib.h>       memory allocation, rand and other functions
#include <math.h>         Math functions
#include <time.h>         time related functions

## C samples
http://www.engineersgarage.com/c-language-programs

# QUICK START
```C++
#include <iostream>
using namespace std;
int main()
{
    cout << "Hi" << endl;
    int tmp;
    cin >> tmp; // Pour empêcher la fenêtre DOS de disparaître.
    return 0;
}
```


```C++ REPL
void main()
{
  Forme *s; // * means compilateur cant know wich Forme version to use. That can be done at compil time (late binding)
  char c;
  cout << "Voulez-vous créer 1 : un rectangle ?\n";
  cout << " 2 : un triangle ?\n";
  cout << " 3 : une forme quelconque ?\n";
  cin >> c;
  switch (c)
  {
    case '1' : s = new Rectangle; break;
    case '2' : s = new Triangle; break;
    case '3' : s = new Forme;
  }
  s -> QuiSuisJe(); // (*) cet appel est polymorphe
}

# include <iostream.h>
class Forme
{
// données et fonctions-membres....
public:
virtual void QuiSuisJe(void); // Une fonction déclarée virtuelle doit ˆetre définie, mˆeme si elle ne comporte pas d’instruction.
};
void Forme::QuiSuisJe()
{
cout << "Je ne sais pas quel type de forme je suis !\n";
}
class Rectangle : public Forme
{
// données et fonctions-membres....
public:
void QuiSuisJe(void);
};
void Rectangle::QuiSuisJe()
{
cout << "Je suis un rectangle !\n";
}
class Triangle : public Forme
{
// données et fonctions-membres....
public:
void QuiSuisJe(void);
};
void Triangle::QuiSuisJe()
{
cout << "Je suis un triangle !\n";
}
```

http://www.nongnu.org/avr-libc/user-manual/group__avr__string.html

 <alloca.h>      Allocate space in the stack  
 <assert.h>      Diagnostics  
 <ctype.h>       Character Operations  
 <errno.h>       System Errors 
 <inttypes.h>    Integer Type conversions 
 <math.h>        Mathematics  
 <setjmp.h>      Non-local goto 
 <stdint.h>      Standard Integer Types 
 <stdio.h>       Standard IO facilities  
 <stdlib.h>      General utilities  
 <string.h>      Strings  
 <time.h>        Time









# HISTOR
---------
`1970` C - Denis Ritchie  
`1980` OOP Concepts  
`1990` C++ (C="C with Classes"  i++ ~ incrément du "C") - Bjarne Stroustrup  
`2011` C++11 (C++0x) - new C++ standard, adding many language [features](http://www.cprogramming.com/c++11/what-is-c++0x.html). To enable C++11 features, you must compile with `-std=c++0x`


# C++ FEATURE
------------------
* **Encapsulation** : Réunis les données (variables = données membres) et les traitements (fonctions membres = méthodes)  
* **Héritage**      : Permet d'améliorer une classe de base en créant une nouvelle classe qui "hérite" des caractéristiques de la classe de base.  
* **Polymorphisme**	: Permet à 2 objets issus de 2 classes différentes de réagir différemment au même appel de méthode
* Case sensitive
* void indique une procédure = fonction qui ne renvoi rien. ((void)0) do nothing (empty function pointer or assert() function not in debug)
* main( ) is the program entry point
* Fin d'un programme  
* Fin implicite : c'est la fin de main( )
* Fin explicite : on utilise exit( 0 );   // declare #include <stdlib.h> pour exit( )
* string surrounded by "        "Banana"
* Decimal separator is .        3.1415


# COMPILATIO
------------------
* Write code in .cpp file
* **Pre-processor**: Juste avant la compilation traite toutes les commandes qui débutent par  # 
* **Compilation**  : Création de l'exécutable (.obj ou .o)
* **Edition des liens** (Lie les .obj et les .lib, les .res)
Remplace les appels de fonctions par les adresses des fonctions. Transforme le .obj en .exe. Génère les messages : Success, Warning ou Error

On peut ajouter directement dans un projet un fichier .obj : il n’est pas nécessaire de disposer du fichier source .cpp correspondant. On pourra donc travailler avec des classes déj`a compilées.

###PRE-PROCESSOR (#): DIRECTIVES & MACROS

* **DIRECTIVES**
Alter source code before compilation  
**`ALWAYS GUARD YOUR HEADERS WITH #ifdef… ALWAYS ALWAYS ALWAYS`**  
* `#define`   Définir une constante, un identificateur ou  une macro-instruction  
* `#ifdef`    Tester l'existence d'une constante (évite d'inclure ++ fois le même fichier...)  
* `#ifndef`   Vérifier qu'une constante n'existe pas  
* `#else`     Code à exécuter avec les tests #ifdef ou #ifndef  
* `#endif`    Termine une séquence de test pré-processeur
* `#include`  Inclure un fichier d'en-tête : Remplace la ligne par le fichier  

Code ensuring that the code between #ifndef and #endif will be included only once:
```c++
#ifndef Unit1H   // Is Unit1H not already defined?
#define Unit1H   // If not then we reach that line and define it
// Header file code placed here...
#endif           // End of if Unit1H not defined
* **< File01.h ou .hpp…>**   Use IDE paths to search for the file   
* **"Filexxxx.h"**           File searched in the same directory as the source file

#include <iostream.h>  
#define  MAX 10  
#ifndef FACTURE_H  
#define FACTURE_H  
	float Price(float p);  
  float Price( );  
#endif  
#define TTC(X)	(X*1.206)      //  Remplace TTX(X) by (X*1.206). Faster execution but bigger file  
```

* **MACRO**  
**\#define identifier replacement**  
When the preprocessor encounters that directive, it replaces any occurrence of identifier in the rest of the code by replacement. 
The replacement can be an expression, a statement, a block or simply anything. The preprocessor does not understand C++ proper, it simply replaces any occurrence of identifier by replacement.

```c++
#define TABLE_SIZE 100
int table1[TABLE_SIZE];
int table2[TABLE_SIZE]; 
After the preprocessor has replaced TABLE_SIZE, the code becomes equivalent to: 
int table1[100];
int table2[100]; 
```

* **FUNCTION MACRO**  
\#define can work also with parameters to define function macros:  
Replacing each argument by its identifier, exactly as you would expect if it was a function:`  
  
```c++
#define cubeX(x) ( (x)*(x)*(x) )  
or
inline double cubeX(double x) { return x*x*x; }

#include <iostream>
using namespace std;
#define getmax(a,b) ((a)>(b)?(a):(b))   // replace any occurrence of getmax followed by two arguments by the replacement expression

int main()
{
    int x=5, y;
    y= getmax(x,2);
    cout << y << endl;
    cout << getmax(7,x) << endl;
    return 0;
}
```



## FILE TYP
----------------
|extension|usage|description|
|---|---|---|
|* .c .cpp  | Source file  ||
|* .h .hpp	| Header file  | Header file, contains only declarations|  
|* .obj		| compilation result ||  
|* .exe		| executable |  	|
|* .lib		| static library ~ toolbox. .obj concat | linked at compilation |  
|* .dll		| dynamic library | linked at execution, loaded once in memory, can be shared be many apps (then need importation lib in projet)|  

Header files ( .h ou .hpp ) contains
* Les prototypes des fonctions
* D'autres fichiers d'en-tête
* La déclaration des variables externes
* Les types de données
* La déclaration des structures
* Les déclarations des classes
* Ne peuvent pas contenir d'instructions (code exécutable)

http://www.cplusplus.com/forum/articles/10627/?bcsi-ac-707242f139ef902e=25D4579E00000303slXzsxaWG8/VUca5CuMS9Ubi3XAfAQAAAwMAAPnSEAAIBwAAAQAAANGvAwA=
The #include statement is basically like a copy/paste operation. The compiler will "replace" the #include line with the actual contents of the file you're including when it compiles the file.
you should **ALWAYS FORWARD DECLARE** (just '**class A;**') when you're only using a pointer or reference to it.

**Difference between .h/.cpp/.hpp/.cc/…**

All files are fundamentally the same in that they're all text files, however different kinds of files should have different extensions:

* Header files should use a .h__ extension (.h / .hpp / .hxx). Which of those you use doesn't matter.
* C++ Source files should use a .c__ extention (.cpp / .cxx / .cc). Which of those you use doesn't matter.
* C Source files should use .c (.c only).

The reason C and C++ source files are seperated here is because it makes a difference in some compilers. In all likelyhood, you'll be using C++ code, so refrain from using the .c extension. Also, files with header extensions might be ignored by the compiler if you try to compile them.

So what's the difference between Header files and Source files? Basically, `header files are #included and not compiled`, whereas `source files are compiled and not #included`. You can try to side-step these conventions and make a file with a source extension behave like a header or vice-versa, but you shouldn't.

The one exception is that it is sometimes (although very rarely) useful to include a source file. 
That scenario has to do with instantiating templates and is outside the scope of this article. For now... just put it in your brain: "do not #include source files"



## NULL POINTER CONSTAN
----------------------------    
* `0` has the double role of `constant integer` and `null pointer constant`
* C resolve ambiguity with `NULL` preprocessor → ((void*)0) or 0
* C++11 corrects it with `nullptr`

Since C, the constant 0 has had the double role of constant integer and null pointer constant. The ambiguity inherent in the double meaning of 0 was dealt with in C by using the preprocessor macro NULL, which commonly expands to either ((void*)0) or 0. C++ didn't adopt the same behavior, allowing only 0 as a null pointer constant. That interacts poorly with function overloading:
void foo(char *);
void foo(int);
If NULL is defined as 0 (which is usually the case in C++), the statement foo(NULL); will call foo(int), which is almost certainly not what the programmer intended, and not what a superficial reading of the code suggests.
C++11 corrects that with nullptr



# FUNCTION
---------------

Declared before use  (compiler checks args…)

### **FONCTION PROTOTYPE**	
Ex: int Add(int a, int b); // Simple function declaration for compiler

```C++
((void*)0)  do nothing (function pointer case. See assert definition)
void main() { }
int main() { }
int main(int argc, char const *argv[]) 
{
  // argc & argv are standards names, can be changed
  cout << "Path + Exe name  << argv[0] << "\n";
  cout << argc << " arguments" << "\n";
  for (int i=0; i<argc; i++)
       cout << "Argument[" << i << "] =" << argv[ i ] << "\n";
  return 0;
}
```

## FUNCTION's DEFAULT PARAMETER
```C++
void printAt(const char *msg, const int pos=1);
void myClass::printAt(const char *msg, const int pos) {…} ← do not redefine default param here else you get the error C2572: 'redefinition of default parameter : parameter 2'
```



# VARIABLE
----------------
* `Must be initialized **ELSE CONTAINS ANYTHING**`
* Bool: 0 is false, others values (1, 2, 3, -1 ,-2, -3… ) are true
* Hexadecimal: start by 0x:	i=0x1F;
* a char string cannot use = sign (reserved to short, int, char…): use strcpy, memset…

## TYPE
* Get type size: int sz = sizeof( int );

|Type|Famille|Taille|Intervalle de valeurs|
|----|-------|------|---------------------|
|char|Caractère|8 bits|-128 à 127|
|unsigned char|Octet|8 bits|0 à 255|
|short int|Entier|16 bits|-32 768 à 32 767|
|unsigned short int|Entier|16 bits|0 à 65 535|
|int|Entier|16 bits (ou 32)|-32 768 à 32 767|
|unsigned int|Entier|16 bits (ou 32)|0 à 65 535|
|long int|Entier|32 bits|-2 147 483 648 à 2 147 483 647|
|unsigned long int|Entier|32 bits|0 à 4 294 967 295|
|float|Réel|32 bits|3.4e-38 à 3.4e+38|
|double|Réel|64 bits|1.7e-308 à 1.7e+308|
|long double|Réel|80 bits|3.4e-4932 à 1.1e+4932|
|bool|Booléen|8 bits|false ( 0 )  ou true  ( 1 )| 

Infinite loop
       _____ is a 8-bit value: after reaching 255, will overflow (so go back to 0) and the loop will therefore go on forever.
      /
  -------------
  unsigned char half_limit = 150;

  for (unsigned char i = 0; i < 2 * half_limit; ++i)
  {
      // do something;
  }



### **USER TYPE**
**`typedef` type user_type**

```C++
typedef short int  INT16;	→   INT16  a=10;  
typedef long int   INT32;	→   INT32  b=20;  
typedef vector<int> iVector;
```

### **OPERATORS**  
`Logique` !  && ||  
`Comparators` == != < > <= >=  
`Increments` --x ++x  x-- x++   y=x++  
`Ternaire` (a>b ? 10 : 20)  
`Binary` 
* &
* |
* ^ (ou excl. bit à bit)
* ~ (complement à 1) 
* << >> Decalages n bits



### **VARIABLES SCOPE**
*	`Local`  
définie et utilisable au sein d'un bloc (fonction…)  
*	`Global`  
utilisable au niveau du fichier. Ajoutez un "g" au début !  
*	`Function arguments`
* `static`  
the bloc keep the value when we leave it and come back. 0 if not init
* `registre`  
Pour diminuer le temps de traitement
* `extern`  
shared between some source code files. Means its owned by another source file.  
rebate.cpp:   float percent=20.6;  
prices.cpp:   extern float percent;  // can now use percent in prices.cpp  

### **ENUM**  
Permet de définir une suite de constantes entières.  
```C++
  enum LanguagesSupported { English, Chinese, Japanese, French };
  enum DIRECTION {Nord=0, EST=-10, SUD=20, OUEST=3 };
  DIRECTION Inverse Sens(DIRECTION Sens)
  { if ( Sens == SUD ) return NORD; }
  typedef enum MessageRecipient {USER1=0, USER2=1, USER1_AND_USER2=2} MessageRecipient ;
  void AddMessage(Message & message, MessageRecipient recipient = USER1_AND_USER2);
  {
    if (recipient == USER1) ...
```

## CASTIN
Pour modifier le type de donnée stocké dans une variable.  
*	IMPLICITE (AUTOMATIC)  
>char c=65;	// équivalent à	char c='A';  
int i='A';	// équivalent à 	int i=65;  
int i=143/2;	// conversion d'un réel en entier  
*	EXPLICITE  
>On force la conversion avec l'opérateur de cast: on indique le type voulu entre ( )  
float f1=10.4;	float f2= (long) f1;  f2=10 !  
        





# CONTROL STRUCTURE
-----------------------
### **TESTS**
**if (cond)**  
{ }  
else if (cond2)  
{ }  
else   
{ }    
    
**switch(test)**  
	{  
 	   case valeur1: //instructions  
		          break;   // un break indique de quitter le test  
       case valeur2: //instructions  
                  break;   // un break indique de quitter le test         
       case valeur3: //instructions  
       case valeur4: //instructions  
	   case valeur5: //instructions  
		          break;  
	   default: // instructions  
}

Si l'expression testée est égale à une des valeurs, C++ exécute le code jusqu'à la fin du switch
ou jusqu'à ce qu'il rencontre un break.
**Les valeurs testées doivent être des constantes littérales ou symboliques: `no variables !`** 
It is not possible to use variables as labels or ranges, because they are not valid C++ constant expressions.
Pour tester un intervalle de valeurs, mettre un if dans default

### **LOOPS**

vector vec;
for (auto itr = vec.begin(); itr != vec.end(); itr++) {  itr->print(); }
for (auto itr = vec.begin(); itr != vec.end(); ++itr) {  itr->print(); }
* Both options will accomplish precisely the same thing
* Second option is better from a performance standpoint
    This is because the post-increment operator (i.e., itr++) is more expensive than pre-increment operator (i.e., ++itr). 
    The underlying implementation of the post-increment operator makes a copy of the element before incrementing it and then returns the copy. That said, many compilers will automatically optimize the first option by converting it into the second.


for (int i=0, j=100; i < Max ; i++, j--) { }

```C++
while ( condition )			
{ 					
  // Code	  (switch en général)	  	   
  break; // pour sortir de la boucle
  // Code		   
  continue; // remonte au while		     
}			
```
The `continue` statement causes the program to skip the rest of the loop in the current iteration, as if the end of the statement block had been reached, causing it to jump to the start of the following iteration or do { ...break ... continue... } while (cond)		

### **GOTO**
```C++
#include <iostream>
using namespace std;

int main ()
{
      int n=10;
    mylabel:
      cout << n << ", ";
      n--;
      if (n>0) goto mylabel;
  cout << "liftoff!\n";
}
```



## C CONCEPTS
------------

## ARRAY
int d1[10] = {0,1,2,2,3,4,2,2,6,7};  
ensemble de variables du même type   
int TabEntier[Nb_Elements];  
`**Un tableau non initialisé contient n’importe quoi !  **`

### STATIC ARRAY
Fixed size   
Caution: bug if you manipulate a value outside the array because of a bad array indice  
```c++
int Nb_Jours[12]={31,28,31,30,31,30,31,31,30,31,30,31};  
int Nb_Jours[ ]={31,28,31,30,31,30,31,31,30,31,30,31};  
TabEntier[9]++;         ou          A= TabEntier[0] * 15 ;  
int TableauA[10][5] ;   // tableau à 2 dimensions  
```
     
### DYNAMIC ARRAY*
Variable size


### JAGGED ARRAY*
In C++ use an array of pointers. 
```c++ 
int *jagged[5];  
jagged[0] = malloc(sizeof(int) * 10);
jagged[1] = malloc(sizeof(int) * 3);

int jagged[][3] = { {0,1}, {1,2,3} };

int jagged_row0[] = {0,1};
int jagged_row1[] = {1,2,3};
int *jagged[] = { jagged_row0, jagged_row1 };
 ```

### ARRAY SIZE*
Elements_Count = sizeof(tab_name)/sizeOf(tab_name[0])  
Passing an array to a function implies to transmit an additional argument (the element count or (array size + type size))
 ```c++
#include<iostream>
using namespace std ;
int main()
{
    int A[3][4] = { {1,2,3,4} , {4,5,7,8} , {9,10,11,12} } ;
    for(int rows=0 ; rows<sizeof(A)/sizeof(*A) ; rows++)
    {
        for(int columns=0 ; columns< sizeof(*A) / sizeof(*A[0]) ; columns++)        
            cout<<A[rows][columns] <<"\t" ;        
        cout<<endl;
    }
}

int main(int argc, char const *argv[])
{
    int arr[6][5] = {
        {1,2,3,4,5},
        {1,2,3,4,5},
        {1,2,3,4,5},
        {1,2,3,4,5},
        {1,2,3,4,5},
        {1,2,3,4,5}
    };
    int rows = sizeof(arr)/sizeof(arr[0]);
    int cols = sizeof(arr[0])/sizeof(arr[0][0]);
    cout<<rows<<" "<<cols<<endl;  // Output: 6 5
    return 0;
}
```


Objet **T; // Tableau de pointeurs sur Objet
T = new Objet* [taille]; // on peut prévoir ici un test de débordement mémoire
Boite::~Boite()
{  delete [] T; // lib`ere l’espace pointé par T


//---------------------- déclaration de la classe Boite ----------------------
class Boite // classe abstraite décrivant une structure de stockage
// les éléments stockés sont de type "pointeur sur Objet"
// la classe Objet est supposée déj`a déclarée
{
public:
Boite(int n = 10); // construit une bo^ıte contenant au maximum n pointeurs
~Boite(); // destructeur
virtual void Mets(Objet *po) = 0; // met dans la boite le pointeur po
virtual Objet *Extrais() = 0; // extrait un pointeur de la bo^ıte
int Vide(); // indique si la bo^ıte est vide
int Pleine(); // indique si la bo^ıte est pleine
protected:
int vide, pleine; // indicateurs
int taille; // capacité de la bo^ıte
Objet **T; // considéré comme tableau de pointeurs sur Objet
};
//---------------------- définition de la classe Boite ----------------------
Boite::Boite(int n)
{
taille = n;
T = new Objet* [taille]; // on peut prévoir ici un test de débordement mémoire
vide = 1;
pleine = 0;
};
Boite::~Boite()
{
delete [] T; // lib`ere l’espace pointé par T
};
int Boite::Vide()
{
return vide;
};
int Boite::Pleine()
{
return pleine;
};
//---------------------- déclaration de la classe Pile ----------------------
class Pile : public Boite // classe décrivant une pile
{
public:
Pile(int n = 10); // construit une pile contenant au maximum n pointeurs
void Mets(Objet *po); // met dans la pile le pointeur po
Objet *Extrais(); // extrait un pointeur de la pile
protected:
int nbelements; // nombre effectif d’éléments contenus dans la pile
};
//---------------------- définition de la classe Pile ----------------------
Pile::Pile(int n) : Boite(n)
{
nbelements = 0;
};
void Pile::Mets(Objet *po)
{
T[nbelements++] = po;
vide = 0;
pleine = nbelements == taille;
}
Objet *Pile::Extrais()
{
Objet *temp;
temp = T[--nbelements];
pleine = 0;
vide = nbelements == 0;
return temp;
}
//---------------------- déclaration de la classe Queue ----------------------
class Queue : public Boite // classe décrivant une queue
{
public:
Queue(int n = 10); // construit une queue contenant au maximum n pointeurs
void Mets(Objet *po); // met dans la queue le pointeur po
Objet *Extrais(); // extrait un pointeur de la queue
protected:
int tete, // indice o`u se trouve l’élément le plus ancien
queue; // indice o`u se mettra le prochain élément
// (T est utilisé comme un tableau circulaire)
};
//---------------------- définition de la classe Queue ----------------------
Queue::Queue(int n) : Boite(n)
{
tete = queue = 0;
};
void Queue::Mets(Objet *po)
{
T[queue++] = po;
queue %= taille; // retour au début du tableau si nécessaire
vide = 0;
pleine = tete == queue;
}
Objet *Queue::Extrais()
{
Objet *temp;
temp = T[tete++];
tete %= taille; // idem
pleine = 0;
vide = tete == queue;
return temp;
}

Queue *q = new Queue (1000);
if (! q -> Pleine())
  q -> Mets(pObjet); // pObjet pointe sur un Objet supposé cré par ailleurs
if (! q -> Vide())
  pObjet = q -> Extrais();
delete q;

## C-STYLE STRIN
---------------------
Strings are simple character arrays
* **STRING DECLARATION**
>char Title[40+1]; // 40 charact. max, last is '\0'  
Title = 'Paul';  
Title[0]='F'; Title[1]='i'; Title[2]='n'; Title[3]='\0';  
char* t = "Joe";  

* **CLEAN A STRING**
>T[0]='\0';  
strcpy (T,"");  
* **TRUNC A STRING**
>T[16]='\0';  

* **STRINGS COMPARAISON** 
>strcmp(ch1,ch2)   compare chars ASCII codes  
= 0 si ch1=ch2  
\>0 si ch1 plus grande que ch2	  	
<0 si ch1 plus petite que ch2	  	

* **PASS A STRING TO A FONCTION**  
>Send the 1st char address  
void print(char * ch)  
{  cout << ch << "\n";    	// print all the string (address)  
   cout << *ch  << "\n";	  // print 1st char  
   cout << *(ch+1) << "\n";	// print 2nd char  
}

* **STRINGS CONSTANTES**               
>char *p= "Total" ;   // max length of *p while all program life = 5 chars  
**`Memory overwrite`** if p has more than 5 chars:  strcpy(p, «1234567890123456789») ; // Too long !  
 


## STRING CLAS
-------------------
Avoids many problems associated with simple character arrays ("C-style strings") : concat, set…  
Based on a template class named basic_string  

```C++
#include <string>     // string
using namespace std;  // cout
...
string nom = "Bjarne";
string prenom;
prenom = "Stroustrup";
string names = first_name + " " + prenom;
cout << names << endl;
names = prenom + ", " + first_name;
cout << names << endl;
```

### MEMBER FUNCTION

**Initialization (constructor)**
>string str1;  
string str4 = "Hello there";  
string str5("Goodbye");  // Alternate form   
**single character**  
  string str6 = 'A';  // Incorrect  
  string str7('A');   // Also incorrect  
substring of another string object: string str9(str8,2,5);  

**Size**
>string str = "Hello";  
string::size_type len;  
len = str.length(); // len == 5   
len = str.size();   // len == 5   

**Conversion to character array ("C-style string")**
>.c_str()

**Inserts** a string into the current string, starting at the specified position.
>string& insert(size_type pos, const string& str);  
str11.insert (3,str12);

**Delete a substring from the current string**
>string& erase(size_type pos, size_type n);

**Replace **
>string& replace(size_type pos, size_type n, const string& str);  
Delete a substring from the current string, and replace it with another string.  
string str14 = "abcdefghi";  
string str15 = "XYZ";  
str14.replace (4,2,str15);  
cout << str14 << endl; // "abcdXYZghi"   

**find - rfind**  
>size_type **find**(const string& str, size_type pos);  
Search for the first occurrence of the substring str in the current string, starting at position pos  
**rfind** does the same thing, but returns the position of the last occurrence of the specified string
* Found:     return the position of the first character  
* Not found: return a special value (called string::npos)  

```C++
string str16 = "abcdefghi";
string str17 = "def";
string::size_type pos = str16.find (str17,0);
cout << pos << endl; // 3
pos = str16.find ("AB",0);
if (pos == string::npos) cout << "Not found" << endl;

Open a file stream with a user-specified file name:
string filename;
cout << "Enter file name: ";
cin >> filename;
ofstream outfile (filename.c_str());
outfile << "Data" << endl; 
```




# ENTREES & SORTIES

       ios
       / \
 istream  ostream              #include <iostream.h>
     /     \
ifstream   ofstream            #include <fstream.h>


**istream** décrits Les flots en entrée 
En C++, un fichier est considéré comme un flot (en anglais : stream), c’est-`a-dire une suite d’octets
représentant des données de mˆeme type. Si ces octets représentent des caract`eres, on parle de fichiertexte
; si ces octets contiennent un codage en binaire, on parle de fichier binaire. Les organes logiques
(clavier, console, écran) sont vus comme des fichiers-textes.
L’objet cin est une instance de cette classe, automatiquement cré et destiné aux entrées depuis le clavier.

l’opérateur de lecture >>

istream &get(char &destination); // read one char
    char c;
    short nb;
    cin.get(c) >> nb; // si on tape 123 entrée, c re¸coit ’1’, nb re¸coit 23

istream &get(char *tampon, int longueur, char delimiteur = ’\n’); // read until delimiter
    char tampon[10];
    cin.get(tampon, 10, ’*’);
Lit au plus longueur caract`eres, jusqu’au délimiteur (inclus) et les loge en mémoire `a l’adresse pointée
par tampon. La chaˆıne lue est complétée par un ’\0’. Le délimiteur n’y est pas inscrit, mais est remis
dans le flot d’entrée.

int &get();
Lit un seul caract`ere, transtypé en int. On peut par exemple récupérer le caract`ere EOF (marque de fin de fichier) qui correspond `a l’entier -1.
int c;
while ((c = cin.get()) != ’q’)
cout << (char) c;

istream &getline(char *tampon, int longueur, char delimiteur = ’\n’);
Lit une ligne. A la différence du get() 2`eme forme, le délimiteur est absorbé au lieu d’ˆetre remis dans le flot d’entrée.

istream &ignore(int longueur = 1, int delimiteur = EOF);
Elimine des caract`eres du flot d’entrée (fonctionne comme getline()).
char tampon[80];
cin.ignore(3).getline(tampon,80);

int peek();
Lit le caract`ere suivant sans l’enlever (fonctionne comme get() 3`eme forme).

istream &putback(char c);
Remet le caract`ere désigné par c dans le flot (ce caract`ere doit ˆetre le dernier `a avoir été lu).

istream &seekg(streampos p);
Acc`es direct au caract`ere numéro p, ce qui permettra sa lecture ; les caract`eres sont numérotés `a partir
de 0. On peut préciser une position relative en mettant en second param`etre ios::beg , ios::cur ou
ios::end.

istream &read(void *donnees, int taille);
Lecture de taille octets depuis le flot, et stockage `a l’adresse donnees.

size t gcount();
Renvoie le nombre d’octets lus avec succ`es avec read().



**ostream** classe ecrirvant les flots en sortie.
L’objet cout est une instance de cette classe, automatiquement cré et destiné aux sorties `a l’écran. cerr
et clog en sont également deux instances, généralement associées `a la console.

opérateur d’écriture << 

ostream &put(char c);
Ecrit le caract`ere spécifié et renvoie une référence sur le flot en cours, ce qui permet d’enchaˆıner les
écritures.
cout.put(’C’).put(’+’).put(’+’); // affiche C++

ostream &seekp(streampos p);
Accès direct `a la position p, pour écriture. Comme pour seekg(), on peut mettre un second param`etre

ostream &write(const void *donnees, size t taille);
Ecrit taille octets provenant de l’adresse donnees.

size t pcount();
Renvoie le nombre d’octets écrits avec write().

Utilitaires sur les caract`eres de <ctype.h>
  tolower() convertit une lettre majuscule en minuscule
  toupper() convertit une lettre minuscule en majuscule
  isalpha() teste si un caract`ere est une lettre
  islower() teste si un caract`ere est une lettre minuscule
  isupper() teste si un caract`ere est une lettre majuscule
  isdigit() teste si un caract`ere est un chiffre entre 0 et 9
  isalnum() teste si un caract`ere est une lettre ou un chiffre.


**fstream.h**
#include <fstream.h>

ifstream:istream     décrit les fichiers en lecture

                                          ::in     read mode 
                                          ::app    append mode: to add à the end
                                          ↓
ifstream(const char *nom, int mode = ios::in);
Crée un nouvel objet de type ifstream, lui attache le fichier-disque appelé nom et ouvre ce fichier en lecture.
   ifstream monfic("A:TOTO.TXT");
   ifstream monfic;
   monfic.open("A:TOTO.TXT"); // variante avec la fonction open()

• close() qui ferme le fichier en fin de traitement.



ofstream:ostream    décrit les fichiers en 
 
                                          ::out      text mode
                                          ::binary   bin mode
                                          ↓
ofstream(const char *nom, int mode = ios::out);
Crée un nouvel objet de type ofstream, lui attache un fichier-disque appelé nom et ouvre ce fichier en écriture.

• close() qui ferme le fichier en fin de traitement.

// fiel copy
void Copie(char *nomSource, char *nomDestination)
{
  ifstream source(nomSource);
  ofstream destination(nomDestination);
  char c;
  cout << "\nDébut de la copie...";
  while (source.get(c)) // source >> c  sauterait les espaces et les marques de fin de ligne
  destination << c;
  source.close();
  destination.close();
  cout << "\nCopie achevée.";
}


**STREAM CONTROL**
• good()       vraie si tout va bien et qu’en principe, la prochaine opération d’entrée-sortie devrait se dérouler normalement,
• eof()        vraie si la derni`ere opération a fait atteindre la fin du fichier,
• fail()       vraie s’il y a échec apr`es une opération,
• bad()        vraie s’il y a échec et si le fichier-disque est endommagé,
• clear()      permettant de réinitialiser les bits d’état du flot.

Stream reference in a conditional expression is replaced by good() 
while (source.get(c))
      ==
if (source.good())
..... // traitement normal
else if (cin.fail()) // ce n’est pas une expression de type short
{
cin.clear(); // on revient `a l’état normal
..... // message d’avertissement
}


Formatage des données

Indicateurs (out aspect)
  left        alignement `a gauche
  right       alignement `a droite
  fixed       flottants en virgule fixe
  scientific  flottants en notation scientifique
  showpoint   force l’affichage avec virgule d’un flottant
  showpos     force l’affichage d’un + devant un entier positif.

Read behavior
skipws                saute les blancs en lecture
setf(ios::<flag>)     active l’indicateur <flag>
unsetf(ios::<flag>)   désactive l’indicateur <flag>
   cin.setf(ios::skipws);   // saute les blancs en lecture au clavier
   cin.unsetf(ios::skipws); // ne saute pas les blancs en lecture au clavier

Fonctions utiles
width()       détermine le nombre minimum de caract`eres de la prochaine sortie
fill()        précise le caract`ere de remplissage
precision()   détermine le nombre de chiffres.

cout.width(12);
cout.fill(’*’);
cout.setf(ios::right);
cout << "Bonjour"; // affiche *****Bonjour

cout.width(8);
cout.precision(5);
cout << 100.0 / 3.0; // affiche 33.333 (avec deux blancs devant)


Manipulateurs <iomanip.h>
Ils permettent de modifier l’apparence des sorties 
endl               marque une fin de ligne et réinitialise le flot
setfill(c)         correspond `a fill()
setprecision(p)    correspond `a precision()
setw(n)            correspond `a width()
setbase(b)         fixe la base de numération
Sauf pour setprecision(), ces manipulateurs n’agissent que sur la prochaine sortie.
Sauf pour setprecision(), ces manipulateurs n’agissent que sur la prochaine sortie.

cout << setbase(16) << 256 << endl; // affiche 100 et passe.



Surcharge des opérateurs >> et <<
rendant ainsi possible la lecture (ou l’écriture) d’un objet depuis (ou vers) n’importe quel flot (fichier ou organe logique).
#include <iostream.h>
#include <fstream.h>
#include <string.h>
const short MAX = 40;
class Plat
{
public:
void Setnom(char *name);
char *Getnom();
void Setprix(float montant);
float Getprix();
private:
float prix;
char nom[MAX];
};
void Plat::Setnom(char *name) { ..... } // détails omis
char *Plat::Getnom() { ..... }
void Plat::Setprix(float montant) { ..... }
float Plat::Getprix() { ..... }
istream &operator>>(istream &is, Plat &article)
{
float montant;
char chaine[MAX];
is.getline(chaine, MAX); // mieux que is >> chaine
article.Setnom(chaine);
is >> montant;
article.Setprix(montant);
is. ignore(1, ’\n’);
return is; // pour pouvoir encha^ıner les entrées : is >> a >> b ...
}
ostream &operator<<(ostream &os, Plat &article)
{
os << article.Getnom() << " (F " << article.Getprix() << ")";
return os; // idem
}
void main() // lit des plats depuis un fichier et les affiche `a l’écran
{
ifstream menu("MENU.TXT");
Plat article;
while (menu >> article)
cout << article << "\n";
menu.close();
}


**NON STRING CLASS MEMBER FUNCTION**  
_istream& `getline` (istream& is, string& str, char delim = '\n'); _
>Reads characters from an input stream into a string, stopping when one of the following things happens:
* An end-of-file condition occurs on the input stream  
* Reach the maximum number of characters that can fit into a string have been read  
* A delimiter character (newline is the default) is read but  the delimiter is not appended to the string.   
The return value is a reference to the input stream. If the stream is tested as a logical value (as in an if or while), it is equivalent to true if the read was successful and false otherwise (e.g., end of file).  

**DO "LINE BY LINE" READS FROM A FILE**  
` REMEMBER THAT THE NORMAL EXTRACTION OPERATOR (>>) STOPS ON WHITE SPACE`, not necessarily the end of an input line. 
  The getline function can read lines of text with embedded spaces.
```C++
vector<string> vec1;
string line;
vec1.clear();
ifstream infile("stl2in.txt");
while (getline(infile,line,'\n'))
{
  vec1.push_back (line);
}
```









## STRUCT

struct T {                  // Equivalent to: class T { public:   

The only difference between a class and struct are the access modifiers. 
  * Struct members are public by default: use structs when you have a simple data object (no methods)
  * Class members are private: use classes when you need an object that has methods   

Type grouping some variables & associated functions. No memory reservation.  

  peu de différence entre les classes et les structures. 
  accessibilité par défaut des variables et méthodes membres est 
    publique dans une structure et privée dans une classe. Rien de plus. 
    En pratique, de nombreux programmeurs utilisent le type struct comme classe de stockage, uniquement. 
    C'est peut-être un retour au C, où les structures ne supportaient pas les fonctions (ou les méthodes)


```C++
struct User  	
{  
  char Name[30+1];  
  char Tel[30+1];  
};  
User  AB, XY[15];  
User  BC = { "Simon", "01 02 03 04 05" };  
cout << BC.Name << BC.Tel;  
```

* variations dans la façon dont elles sont définies
    
enum colour = {Red, Green, Yellow}; // Normally in header file
struct apple   // ne définit que le type: n'instancie pas la structure
{
    float weight;
    colour c; 
};

struct
{
    float weight;
    colour c; 
} apple;      // ne crée pas du tout de type
              // Elle instancie plutôt "pomme" pour l'utilisation dans le champ d'application actuel









##POINTERS
Variable contenant l'adresse d'une zone mémoire (autre variable…)  
A pointer is a variable. To be useful the program, somehow, sets the value of a pointer to the address of something.  
Puissants par les nombreux usages possibles mais délicats  
In C and C++ you can have a pointer to just about anything:
+ A pointer to any kind of C or C++ variable
+ A pointer to a C or C++ struct
+ A pointer to any kind of C++ class object
+ A pointer to a function
+ A pointer to a pointer
+ A pointer to (a pointer to a pointer to just about anything) - See more at: https://www.gidforums.com/t-12539.html#sthash.RbCCQxA3.dpuf

>__&variable__   adresse mémoire du pointeur  
__*variable__    valeur de la variable pointée  
__variable__	 adresse contenant l’adresse de la variable pointée.
  
  /* pint is an array of ten pointers to int */ 
  int *pint[10];

		int * p;
		int q=5;  p=&q;  // *p sera égal à 5
		*p=10; // q sera égal à 10
		a= (*p)+10;
        
|Adresse|Variable|Valeur|
|---|---|---|
|000|||
|…|||
|010|q|5|
|…|||
|050|p|0010|
        
__Null pointer (Not initialised Pointer)__  
__Contient n'importe quoi et pointe n'importe où__		
The null pointer is a constant with a value of zero defined in several standard libraries.
>int *p=NULL;  
cout << "The value of ptr is " << ptr ;   // The value of ptr is 0
if (ptr) // succeded if p is not null
if (!ptr) // succeded if p is null
if (ptr==NULL) // instructions

Si une fonction a un argument de type pointeur, il faut lui passer l’adresse d’une variable de même type.  CalculTTC(&TotalFacture) ;  
Permet à une fonction de « renvoyer » plusieurs résultats en même temps.
Fonction renvoyant un pointeur : Ne renvoyez pas l’adresse d’une variable locale à la fonction car elle est détruite avant que l’on utilise sa valeur !  

**pointer arithmetic**  
++, --, +, and -
ptr is an integer pointer which points to the address 1000. Assuming 32-bit integers, let us perform the following arithmatic operation on the pointer:
ptr++  the ptr will point to the location 1004
int  var[MAX] = {10, 100, 200};
int  *ptr;
 for (int i = 0; i < MAX; i++)
   {
      cout << "Address of var[" << i << "] = ";
      cout << ptr << endl;

      cout << "Value of var[" << i << "] = ";
      cout << *ptr << endl;

      // point to the next location
      ptr++;
   }

The magic behind square brackets with pointers

#include <iostream>
int main(int argc, const char * argv[]) {
    int a[] = {1, 2, 3, 4, 5, 6};
    std::cout << (1 + 3)[a] - a[0] + (a + 1)[2];
}
output 8

* (1+3)[a] is the same as a[1+3] == 5
* a[0] == 1
* (a + 1)[2] is the same as a[3] == 4



**Pointeurs et tableaux**  
Un tableau non initialisé contient n’importe quoi !  
>int TabEntiers[20] ;  
int *pTab ;       
pTab= &TabEntiers[0] ;                 ou        pTab= TabEntiers ;

int  var[MAX] = {10, 100, 200}; 
for (int i = 0; i < MAX; i++)
{
  *var = i;    // a correct syntax
  var++;       // incorrect syntax
}

  
Le nom d’un tableau correspond à l’adresse de son 1er élément  
>*pTab=10 ;  	→  TabEntiers[0]=10 ;  
*(pTab+1)=20 ;  →  TabEntiers[1]=20 ;     	

**Passer un tableau à une fonction**  
Envoyer l’adresse de ce tableau ainsi que le nombre d’éléments :            
>void InitTableau(int *pTab, int Nbr) ;

int *p=45 ;  est impossible  
il faut int p=new int ;p=458 ; ... delete p ;


##POINTER & CLASSES
## OBJECT ARRAY
Le nombre d'éléments est fixé à la compilation du programme et ne peut varier.  
Micro  Mic[Constante] ; // définition d'un tableau statique d'objets Micro


**Pointeurs et structures**  
On accède aux champs d’une structure avec -> ou .  
Si la fonction ne modifie pas la structure, passez-lui une copie de la structure, sinon l’adresse.  

** Pointeur de fonction**  
Un pointeur qui contient l’adresse d’une fonction permet d’appeler celle ci comme avec le nom de la fonction. 
On peut stocker les adresses de fonctions et les appeler à volonté.  
>int (*p)(void) ;	// déclaration du pointeur de fonction  
p=fct ;		// Initialisation du pointeur de fonction  
p() ;		// Appel de la fonction fct()  

(*p) permet au compilateur d’identifier un pointeur de fonction  
**L’adresse d’une fonction correspond à son nom (pas de & ici)**





## Tableaux dynamiques**
Le nombre d'éléments est fixé à l'exécution du programme et ne peut varier.
```C++
int *pNbr = new int[NbrElements] 
cin >> pNbr[i];    cout << pNbr[i]; 
delete []pNbr; 
```

## Linked Lis
Chaque objet possède un membre de type pointeur vers l'objet suivant.

## Pointers array
Store différents objects
```c++
Materiel *Liste[Constante] ;	// ici il faudra initialiser la liste avec NULL et créer les objets avec new.    
ParcMateriel::ParcMateriel() { for (int i=0 ; i<Max ; i++) Liste[i]=NULL; 	}   
int ParcMateriel::Ajouter(Materiel * pMat)  
{   
    for (int i=0; i<Max ; i ++)  
    {   if (Liste[i]!=NULL)	{ Liste[i]=pMat;  return 1;}	}  
}  
ParcMateriel::~ParcMateriel()  
{  
    for (int i=0; i<Max ; i++)  
    {	   if (Liste[i]!=NULL)   delete Liste[i];	}  
}  
```

```c++
class toy { public: int x; }; 


int main() { 
    toy **tPoint;                   // a pointer to a pointer to an object from the "toy" class - See more at: https://www.gidforums.com/t-12539.html#sthash.RbCCQxA3.dpuf
    tPoint = new toy *[33];         // use as an array of 33 pointers to "toy" objects
    toy *tArray[100];               // an array of 100 pointers to "toy" objects 
    int i; 
    for (i = 0; i < 5; i++) { 
       tPoint[i] = new toy; 
       tPoint[i]->x = 10*i; 
       tArray[i] = new toy; 
       tArray[i]->x = i; 
     } 
    
    for (i = 0; i < 5; i++) { 
        cout << "tPoint[" << i << "]->x = " << tPoint[i]->x << ", tArray[" << i << "]->x = " << tArray[i]->x << endl; 
    }
    for (i = 0; i < 5; i++) { delete tPoint[i]; delete tArray[i]; } delete [] tPoint; return 0; 
}

tPoint[0]->x = 0, tArray[0]->x = 0 
tPoint[1]->x = 10, tArray[1]->x = 1 
tPoint[2]->x = 20, tArray[2]->x = 2
tPoint[3]->x = 30, tArray[3]->x = 3 
tPoint[4]->x = 40, tArray[4]->x = 4 

```

## Returning a Double-Pointer*
```C++
#include <iostream>
using namespace std;

double ** GetWeeklySalary()
{
    double w      = 880.24;
    double *ws    = &w;
    double **wwss = &ws;

    return wwss;
}
//---------------------------------------------------------------------------
int main(int argc, char* argv[])
{
    double WeeklySalary = **GetWeeklySalary();

    cout << "Weekly Salary: " << WeeklySalary << endl;

    return 0;
}
//---------------------------------------------------------------------------

would produce:

Weekly Salary: 880.24
```

## vector
```C++
#include <vector>

std::vector<Ant*> ants;
for (int i = 0; i < num_ants; ++i) {
    ants.push_back(new Ant());
}
```



## **CLASSES (C++ CONCEPT)**

Un ensemble d’objets de mêeme type s’appelle une classe.
Tout objet appartient `a une classe, on dit aussi qu’il est une instance de cette classe.

Type de données ayant un comportement propre (famille d'objets) et contenant  
* Les données (données membres = attributs)   
* Les traitements (fonctions membres = méthodes)
Permet de créer des objets (instances de classe)
	      
Pour utiliser les objets on programmame une classe en 3 phases : déclaration, définition, utilisation
.les décrire (.h)
  . déclaration: fiche descriptive data / fonctions-membres: servira d’interface avec le monde extérieur
  . implémentation, contenant la programmation des fonctions-membres.
. les utiliser (.cpp)

Ce dernier fichier contient la fonction main, et c’est par cette fonction que commence l’exécution du programme

**Encapsulation**
Données et traitements sont regroupés au sein d’une classe et possèdent des droits d’accès  
protéger certaines données-membres ou fonctions-membres en les rendant invisibles de l’extérieur

class Cercle 
+ centre
+ rayon
- surface : surface ne doit pas être modifiable de l’extérieur car l’objet risquerait sa cohérence (la surface dépend  du rayon)

* `public`		Toutes les données et fonctions membres sont utilisables par toutes les fonctions
methods and variables may be accessed from any portion of the code that knows the class type. This should usually only be used for member functions
(and not variables) and should not expose implementation details

* `private` 	Toutes les données et fonctions membres ne sont utilisables que par les fonctions de la classe
for methods that can not be used in either subclasses or other places



Note: It's often misunderstood that different instances of the same class may access each
others' private or protected variables. A common case for this is in copy constructors.
class Foo
{
public:
Foo( const Foo &f )
{
m_value = f.m_value; // perfectly legal
}
private:
int m_value;
};

* `protected`	Toutes les données et fonctions membres ne sont utilisables que par les fonctions de la classe et les fonctions membres des classes dérivées.
Only subclasses of this type may access these functions or variables. Many people prefer to also keep this restricted to functions (as opposed to variables) and to use accessor methods for getting to the underlying data.

accès restreint qui est similaire à privé. La différence est qu'il est accessible par ses sous-classes, ou classes dérivées.

* friend class
Il ne faut pas abuser de la relation d’amitié, car elle constitue une entorse au principe d’encapsulation.

autorisé à accéder aux membres privés et protégés de toute classe qui l'a déclaré comme ami. La propriété n'est pas héritée (les sous-classes d'amis ne deviennent pas automatiquement amies), et n'est pas transitoire (les amis des amis ne sont pas des amis).

Lorsque toutes les fonctions-membres d’une classe B sont amies d’une classe A, on dit que la classe B est amie de A. 
Au lieu de déclarer dans la classe A chaque fonction-membre de B comme amie: 
class B; // informe le compilateur qu’il existe une classe nommée B
class A
{
  friend class B; // la classe B est déclarée amie de la classe A. B a accès à A.xxx
  public:
  .....
  private:
  .....
};

* friend function
fonction non membre de la classe
Accède aux données et fcts-membres quelles soient publiques, protégées ou privées.


class A
{
  friend truc machin(); // fonction libre amie de la classe A
  public:
  .....
  private:
  .....
};

S’il s’agit d’une fonction-membre d’une autre classe :
class B; // informe le compilateur qu’il existe une classe nommée B
class A
{
  friend truc B::machin(); // fonction-membre de la classe B, amie de la classe A
  public:
  .....
  private:
  .....
};


Utile pour surcharger certains opérateurs. 

class A
{
  friend ostream &operator<<(ostream &os, A &monObj); // déclaration
  private:
  int T[10];
  ......
};

ostream &operator<<(ostream &os, A &monObj) // définition de la surcharge
{
  for (int i = 0; i < 10; i++)
  os << monObj.T[i]; // donnée accessible gr^ace `a l’amitié
  return os;
}


## . and :: operators

`.` notation pointée
Sert à accèder aux données et fonctions-membres d’un objet
mon_objet.donnee

`::`  
Dans la définition d’une fonction-membre, on doit ajouter <nom de la classe>:: devant le nom de la fonction.
Opérateur de résolution de portée permet d’identifier une fonction dans une classe  
Utilisé dans une classe devant un nom de variable ou de fonction, il désigne une variable ou une fonction classique (non-membre)  
>void Factrure::AfficheTaux()  
{  
  Taux::Taux; // désigne la variable non-membre  
  cout << "Taux="  << :: AfficheTaux();  
}	 

Lorsqu’une fonction-membre virtuelle f d’une classe A est surchargée dans une classe B dérivée de A, un
objet b de la classe B peut faire appel aux deux versions de f : la version définie dans la classe B — elle
s’écrit simplement f — ou la version définie dans la classe parente A — elle s’écrit alors A::f, o`u :: est
l’opérateur de portée.

class  Micro    // la définition d’une classe n’entraîne pas de réservation mémoire ! ~ définition d’un type de donnée
{ 
   public :   // chaque classe à généralement une interface publique (fonctions accessibles par l’utilisateur) 
   char Marque[20+1] ;
   int Disque ;
   void Affiche( ) ;    // déclaration d’une fonction membre
} ;

void  Micro :: Affiche()         // fonction définie hors de la classe : définition déportée
{
  cout  << « Marque :  » << Marque << « \n » ;
  cout  << « Disque : » << Disque << « \n » ;
}

**Prototype de classe**  
class Facture;	// déclare le nom Facture comme étant une classe, on la définiera plus tard

##CRÉATION D’OBJETS
### statique
Les objets statiques sont __automatiquement détruits__ dès qu’ils sortent de leur portée.
>1) Création :				Micro Mic ;  
2) Utilisation avec le .			cout << Mic.Marque ;  
    
### DYNAMIQUE
>1) Créer un pointeur vers la classe :	Micro * pMic ;  
2) Utiliser l’opérateur new :		pMic = new Micro ;  
3) Utiliser l’objet avec ->			cout << pMic->Marque ;  
4) __Détruire l’objet après son utilisation__	delete pMic ;			// sinon mémoire non libérée  

Rq : Avant delete, vérifier que le pointeur n’est pas nul sinon risque d’erreur :
>if (pMic !=NULL)	// ou if (pMic)
{
    delete pMic ;
    pMic = NULL ;
}

**Membre statique** 
Donnée membre statique: elle est unique pour tous les objets de la classe.  
Déclaration:   				static float TauxTVA;    dans le corps de la classe Facture  
Initialisation se fait en dehors de la classe:	 float  Facture::TauxTVA = 0.206;  

!! Static member must be defined outside class body, so you have to add the definition and provide initializer there:
else you get an error "error LNKxxx: unresolved external symbol "private: static class ..." (Why are classes with static data members getting linker errors?)
All static members imply that you are trying for some kind of singleton,

class Platform :
public Object
{
    public:
        Platform(void);
        ~Platform(void);
        Platform(GLfloat xCoordIn, GLfloat yCoordIn, GLfloat widthIn);
        void draw();
        static int loadTexture();

    private:
        static GLuint tex_plat;
};

// static member variables have to be initialized explicitly at the module level. Add following in your cpp file:
GLuint Platform::tex_plat=0; // initialization of static member

            
**FONCTION MEMBRE STATIQUE** 
Elle ne sait pas travailler sur un objet particulier de la classe. 
Elle ne récupère pas t h i s
Elle ne travaille qu'avec les membres statiques.

**Fonction membre constante**   
**Elle ne peut pas modifier les données membres de la classe.**
>Class Materiel  
	{  
 	   virtual void affiche( ) const ;  
}		  
	void Materiel::Affiche ( ) const	{   …. }  
		
Une fonction virtuelle pure constante doit être redéfinie dans les classes dérivées comme étant constante.  
Sinon le classe dérivée deviendra abstraite.  
Chaque fonction membre qui n'a pas besoin de modifier les données membres devrait être déclarée constante.


# RÉFÉRENCE
Permet l'accès à des variables situées dans une autre portée (~alias)  
References are a way of assigning a "handle" to a variable
The ability to pass it by reference keeps us from needing to make a copy of the string and avoids the ugliness of using a pointer.
It should also be noted that this only makes sense for complex types — classes and structs. In
the case of ordinal types — i.e. int, float, bool, etc. — there is no savings in using a reference
instead of simply using pass by value.

Assigning References
int foo = 3;    // foo == 3
int &bar = foo; // foo == 3
bar = 5;        // foo == 5

>	int a ;  
	int &ref = a ;  // le compilateur vérifie que la référence est (cas présent) ou sera (arg. de fonction) initialisé  
	Ref = 10 ;       // équivalent à  a = 10 ;  
	Il n’existe pas de référence nulle (c’est à dire non initialisée)  

###PASSAGE D’ARGUMENTS AUX FONCTIONS  
* __Par valeur__ 	  L’argument reçu est une copie de la variable passée 
* __Par pointeur__	L’argument est une copie du pointeur et pointe donc vers la vraie  « variable » (dont l’adresse est passée à la fonction)  
* __Par référence__ 	C’est la variable qui est passée au lieu de son adresse


L'appel par valeur fonctionne en faisant passer une copie de la valeur dans la fonction. Les modifications apportées à l'intérieur de la fonction n'affectent pas la valeur qui a été utilisée pour spécifier le paramètre. C'est la méthode par défaut utilisée par le langage dans les paramètres pour les appels de fonction.
void myValueFunction(int value_1, float value_2) ;

Appelez les ouvrages de référence en passant la référence dans la fonction. La référence se comporte de la même manière qu'un pointeur déréférencé et, de ce fait, les modifications apportées à l'intérieur de la fonction se reflètent dans la fonction d'appel (ou scope). Cela laisse la possibilité d'effets secondaires, il faut donc être prudent lorsque l'on passe des paramètres par référence.
void myReferenceFunction(int &reference_1, float &reference_2) ;


void foo( int &i ) { i++; } // Add one to the i reference variable 
int main()
{
  int bar = 5; // bar == 5
  std::cout << "bar = " << foo( bar ) << '\n';  // bar = 6
  std::cout << "bar = " << foo( bar ) << '\n';  // bar = 7  
  return 0;
}

void foo( const std::string &s ) { std::cout << s << std::endl; }
void bar( std::string s ) { std::cout << s << std::endl; }
int main()
{
  std::string text = "This is a test.";
  foo( text ); // doesn't make a copy of "text"
  bar( text ); // makes a copy of "text"
  return 0;
}

####SURCHARGE DE FONCTIONS (CLASSIQUES, FONCTIONS MEMBRES…)  
On peut définir des fonctions qui ont le même nom mais qui se différencient par le type des arguments (et pas par 
le type renvoyé).

Valeurs par défaut des arguments
>void fct(int i , int j=10 , int k= 20) {code …}  
	fct( 1 , 2, 3 ) ;  
	fct( 1 , 2 ) ;  
	fct( 1 ) ;  
	fct ( ) ;    ou   fct ( 1 , , 5 ) ; // appels invalides  

Seuls les derniers arguments peuvent avoir une valeur par défaut
A partir du moment où un argument possède une valeur, les suivants doivent aussi en avoir une.
On peut indiquer les valeurs par défaut dans les prototypes mais alors il ne faut pas les répéter dans la définition
de la fonction

## thi

Désigne l’objet courant, c’est-à-dire l’objet auquel une fonction membre appartient
Il est passé de façon cachée à chaque fonction membre. (this ou this -> est ajouté par le compilateur. Ce n'est pas le cas en javascript)  
Permet de différencier une variable locale d’une donnée membre de la classe  
>void Telephone::Enregistrer (int Disque )  
		{   
    Agenda.Ajouter(this) ; 	// Agenda peut stocker l’adresse des objets de type Téléphone qui lui ont passé.  
    this.Disque=200 ;   	// Accès au membre de la classe Téléphone  
   disque=40 ;		// Accès à la variable locale  
}   

Dans le .cpp l'objet n’est jamais nommé, il est implicite (au besoin, on peut y faire référence en le désignant par *this).

##CONSTRUCTOR
Lors de la création d’un objet, il y a  
•	Allocation mémoire   
•	Appel d’une fonction membre de la classe : le constructeur. Il permet d’effectuer un traitement à la création  
Le compilateur intègre un constructeur par défaut (constructeur sans argument) à toute classe qui n’en contient pas.  

class  Micro    // la définition d’une classe n’entraîne pas de réservation mémoire ! ~ définition d’un type de donnée
{ 
   public :   // chaque classe à généralement une interface publique (fonctions accessibles par l’utilisateur) 
   char Marque[20+1] ;  
   Micro(char *r, char *m= " " , int d=4 ) ;   	// définition d’un constructeur qui possède des arguments par défaut
   Micro ( ) ;  				// surcharge d’un constructeur   
} ;

**constructeur avec liste d’initialisation**  
Micro : :Micro(char *r, char *m) : Reference( r ), Marque ( m ) ; 
Le nom de la donnée membre est suivi de la valeur d’initialisation  entre parenthèses.  
(Cette technique ne fonctionne pas avec les tableaux)   


**DESTRUCTOR** 

`a l’issue de l’exécution d’un bloc, le destructeur est automatiquement appelé pour
chaque objet de la classe Nom classe déclaré dans ce bloc. Cela permet par exemple de programmer la
restitution d’un environnement, en libérant un espace-mémoire alloué par l’objet.

special member function that is called when the lifetime of an object ends. Destructor's name is defined as the same way as constructor, but with a special character '~' in front. The purpose of the destructor is to free the resources that the object may have acquired during its lifetime.

Il est appelé automatiquement juste avant la destruction de l’objet et de la libération de la mémoire pour effectuer un dernier traitement.  
	Il n’a ni arguments ni valeur de retour.  
	
Protection des données et fonctions membres :
	private restreint l’utilisation des variables et des fonctions aux seules fonctions membres de la classe.
	
	Accesseurs ou Getter	 : Méthode qui renvoi le contenu d’une donnée membre protégée.
	Mutateurs ou Setter 	 : Fonction permettant  de modifier une donnée membre protégée.
	
	Utilisé car parfois on a accès aux seules fonctions membres.
	Un setter permet de valider la valeur affectée à la donnée.

GETTER-SETTER
  class Foo {
    public:
        const std::string& getName() const {return name_;}
        const void setName(const std::string n) const { name_ = n;}
    private:
        const std::string& name_;
};



**Fonction inline**  
L’appel de la fonction sera remplacé par le corps de la fonction elle-même. (rapidité mais exécutable plus gros)  
•	inline implicite
>class Micro
{ ……..  
  int GetDisque ( ) {return Disque ;}   // le corps de la fonction intégrée dans la classe  
………  
}  
• inline explicite	
>inline int GetDisque  
{ return Disque ; }  


## HÉRITAGE** - 'is
Faire partager aux classes dérivées le savoir-faire (attributs membres et fonctions) des classes de base.  
On ajoute de nouveaux membres et fonctions à la nouvelle classe pour modifier/améliorer/réutiliser/spécialiser le comportement de la classe de base.  
La classe dont dérive une classe est appelée : classe de base ou superclasse ou classe parent/ancêtre/mère/père  
La classe dérivée est appelée: classe fille ou sous-classe  

Une classe dérivée peut accéder à tous les membres publics et protected de la classe de base.   
Les données private ne sont manipulables que par les fonctions de la classe qui les définies.  
Les fonctions membres d'une classe peuvent accéder à toutes les données membres de la classe quelle que soit l'étiquette de protection de la donnée)
L'ordre d'appel des constructeurs se fait classe de base vers classe dérivée
L'ordre d'appel des destructeurs est inverse (classe dérivée vers classe de base)	

class B: [public][private][protected] A
{
  …
}

public: La protection des membres de la classe A reste inchangée au niveau de la classe B  
protected: Les membres public et protected de A sont considérés comme protected dans la classe B. Les classes dérivées de B ont accès aux membres de A  
private: Les membres public et protected de A sont considérés comme private dans la classe B. Les classes dérivées de B n'ont plus accès aux membres de A  
On ne peut qu'augmenter le niveau de sécurité (private).  
Constructeurs: A chaque création d'objet il y a appel au constructeur de la classe correspondante. Si cette classe est dérivée, le constructeur va en premier appeler le constructeur de sa classe de base. Ce dernier fera de même s'il dérive aussi d'une autre classe.  

C++11:
class GameObject
{
    public:
        virtual ~GameObject() {}
        virtual void update() {}
        virtual void draw() {}
        virtual void collide(Object objects[]) {}
};

class Visible : public GameObject
{
    public:
        virtual void draw() override { /* draw model at position of this object */ };
    private:
        Model* model;
};

class Solid : public GameObject
{
    public:
        virtual void collide(GameObject objects[]) override { /* check and react to collisions with objects */ };
};

class Movable : public GameObject
{
    public:
        virtual void update() override { /* update position */ };
};


**Héritage multiple**

>class B: public A, public B, private C  
{  
  …  
}  


un objet ou une classe hérite de caractéristiques, telles que des fonctions membres ou des variables, de plus d'une classe parente. Comparez cela à l'héritage unique, où un objet ou une classe est limité à l'héritage d'un seul parent.

Bien que cette fonctionnalité soit puissante, elle peut conduire au problème des diamants.


Multiple inheritance is dangerous if not implemented carefully, as it can lead to the diamond problem...

class A
{
.....
};
class B
{
.....
};
class C : public A, public B
{
.....
};
La classe C hérite alors de A et B : une instance de la classe C poss`ede `a la fois les données et fonctionsmembres
de la classe A et celles de la classe B.
Quand un objet de la classe C ci-dessus est cré, les constructeurs des classes parentes sont appelés
: d’abord celui de A, ensuite celui de B. Quand un objet est détruit, les destructeurs des classes parentes
sont appelés, d’abord celui de B, ensuite celui de A

il peut arriver que des données ou fonctions-membres des classes A et
B aient le mˆeme nom. Pour lever l’ambigu¨ıté, on utilise l’opérateur de portée en écrivant par exemple
A :: x pour désigner la donnée-membre x héritée de la classe A, et B :: x pour désigner celle qui est
héritée de la classe B.

**The diamond/diamant problem / Classe virtuelle**
     A
     ↑
  -------  
 ↑       ↑
 B       C
  -------  
     ↑     
     D

Ambiguity when two classes B and C inherit from A, and class D inherits from both B and C. 
If there is a method in A that B and C have overridden, and D does not override it, 
then which version of the method does D inherit: that of B, or that of C ?

C++ by default follows each inheritance path separately, so a D object would actually 
contain two separate A objects, and uses of A's members have to be properly qualified. 
If the inheritance from A to B and the inheritance from A to C are both 
marked "virtual" (**virtual Class**, for example, "class B : virtual public A"), 
C++ takes special care to only create one A object, and uses of A's members work correctly. 
If virtual inheritance and nonvirtual inheritance are mixed, there is a single virtual A 
and a nonvirtual A for each nonvirtual inheritance path to A. 

C++ requires stating explicitly which parent class the feature to be used is invoked from i.e. "Worker::Human.Age". C++ does not support explicit repeated inheritance since there would be no way to qualify which superclass to use (i.e. having a class appear more than once in a single derivation list [class Dog : public Animal, Animal]). C++ also allows a single instance of the multiple class to be created via the virtual inheritance mechanism (i.e. "Worker::Human" and "Musician::Human" will reference the same object).

LANGUAGES THAT ALLOW ONLY SINGLE INHERITANCE, WHERE A CLASS CAN ONLY DERIVE FROM ONE BASE CLASS, DO NOT HAVE THE DIAMOND PROBLEM. The reason for this is that such languages have at most one implementation of any method at any level in the inheritance chain regardless of the repetition or placement of methods. Typically these languages allow classes to implement multiple protocols, called interfaces in Java. These protocols define methods but do not provide concrete implementations. This strategy has been used by ActionScript, C#, D, Java, Nemerle, Object Pascal (Delphi), Objective-C, Smalltalk, Swift and PHP




Pensez à la classe supérieure : "A", qui comporte deux sous-classes "B1" et "B2". Chacune des classes enfantines hérite séparément de la classe mère, "A". C'est lorsqu'un troisième niveau, "C", est ajouté que le problème peut se poser. Il ne peut se produire que si la sous-classe "C" hérite à la fois de "B1" et de "B2".

En outre, elle n'aura lieu que s'il existe une méthode définie dans "A" qui est remplacée à la fois dans "B1" et "B2", mais qui n'est pas remplacée dans "C". Si cette méthode est invoquée par "C", il existe alors une ambiguïté quant à la méthode à utiliser.

Il n'est pas important de savoir comment ce problème est résolu en C++. Il faut plutôt reconnaître que le problème existe et doit être pris en compte lors de la conception d'une hiérarchie de classes.



**Classe virtuelle**  
C++ solves the diamond problem of multiple inheritance by allowing virtual inheritance.

Si 2 classes B et C dérivent d'une même classe A et si la classe D dérive de B et C, alors D possède 2 objets A : Membres ambigus: lequel utiliser ?  
On déclare alors la dérivation en "virtual": Il n'existera alors qu'un seul objet A pour chaque objet D.  
class A{…}      
class B: **virtual** public A { … }      
class C: **virtual** public A { … }         
class D: public B, public C   { … }
D::D(int bb, int cc, int dd):A(0):B(bb):C(cc,4) { … }

sample: https://www.geekboots.com/cpp/virtual-inheritance

#include<iostream>
using namespace std;

/* Grandparent, Abstract class */
class person {
  protected:
    string name, gender;
    int age;

  public:
    void get_person() {
      cout << "Enter details:" << endl;
      cout << "Name:" << endl;
      cin >> name;
      cout << "Age:" << endl;
      cin >> age;
      cout << "Gender:" << endl;
      cin >> gender;
    }
  
    void display() {
      cout << "\nInformation: "<< endl;
      cout << "Name: " << name << endl;
      cout << "Age: " << age << endl;
      cout << "Gender: " << gender << endl;
    }
};

/* Inherit grandparent class as virtual */
class income : virtual public person {
  protected:
    string source;
    float amount;

  public:
    void get_income() {
      cout << "Source of Income:" << endl;
      cin >> source;
      cout << "Amount:" << endl;
      cin >> amount;
    }
  
    void display() {
      cout << "Income from: " << source << endl;
      cout << "Amount: " << amount << endl;
    }
};

/* Inherit grandparent class as virtual */
class expenses : virtual public person {
  protected:
    string purpose;
    float amount;

  public:
    void get_expenses() {
      cout << "Purpose of Expenses:" << endl;
      cin >> purpose;
      cout << "Amount:" << endl;
      cin >> amount;
    }
    void display() {
      cout << "Expenses for: " << purpose << endl;
      cout << "Amount: " << amount << endl;
    }
};

/* Inherit two parent class into one child class */
class programmer : public income, public expenses {
  float net_saving;

  public:
    void display() {
      net_saving = income :: amount - expenses :: amount;
      person :: display();
      income :: display();
      expenses :: display();
      cout << "Net Saving: " << net_saving << endl;
    }
};

int main() {
  programmer p1 = programmer();

  /* Call member functions from grandparent and parent classes */
  p1.get_person();
  p1.get_income();
  p1.get_expenses();

  /* Call display() from derived class 'programmer' */
  p1.display();
  return 0;
}

/****** Output ******/
          
Enter details:
Name: Jonh
Age: 24
Gender: Male

Source of Income:
 Programming Amount: 10000
 Purpose of Expenses: Food
 Amount: 8000

Information:
Name: Jonh 
Age: 24
Gender: Male

Income from: Programming
Amount: 10000
Expenses for: Food
Amount: 8000
Net Saving: 18000

## Polymorphism

Un pointeur du type de la classe de base peut stocker l'adresse de n'importe quel objet dérivé
Le compilateur appelle alors les fonctions selon le type de pointeur 
Une fonction virtuelle (polymorphe) est appelée en fonction du type d'objet et non pas du type de pointeur utilisé.  
Ainsi 2 classes peuvent réagir différemment au même appel de fonction.  
Si la fonction virtuelle appelée n'est pas dans la classe, C++ remonte la hiérarchie des classes jusqu'à la trouver.    
Pour choisir la méthode adéquate par rapport au type d'objet, C++ gère le tableau V-table (adresses de toutes les fonctions virtuelles)  
Les fonctions virtuelles ne peuvent pas être utilisées dans le corps des constructeurs  

**Fonctions virtuelles pures**  
(oblige les classes dérivées à redéfinir les fonctions virtuelles pures)
virtual void Utilise( ) = 0 ; 
Une fonction purement virtuelle n’a pas de définition dans la classe. Elle ne peut qu’ˆetre surchargée dans
les classes dérivées.
Une classe contenant une fonction virtuelle pure est abstraite (on ne peut créer d'instance d'objet)  
Si les classes dérivées d'une classe abstraite ne redéfinissent pas les fonctions virtuelles, elles	deviennent aussi abstraites.  	
C'est une sécurité par rapport au polymorphisme pour éviter l'appel à la fonction de la classe de base.




// Example program
#include <iostream>
#include <string>

class Abstract
{
public:
  virtual void foo() = 0;
};

class Implementation : public Abstract
{
public:
  void foo() { std::cout << "Foo!" << std::endl; }
};

void call_foo(Abstract& obj) { obj.foo(); } 


int main()
{
    Abstract *bar = new Implementation();

  call_foo(*bar);

  delete bar;
  
  std::string name;
  std::cout << "What is your name? ";
  getline (std::cin, name);
  std::cout << "Hello, " << name << "!\n";
}



// Example program
#include <iostream>
#include <string>

class Abstract
{
public:
  virtual void foo() = 0;
};

class Implementation : public Abstract
{
public: 
    void foo();
};

void Implementation::foo()
{
  std::cout << "Foo 2 !" << std::endl;
}

void call_foo(Abstract& obj) { obj.foo(); } 


int main()
{
    Abstract *bar = new Implementation();

  call_foo(*bar);

  delete bar;
  
  std::string name;
  std::cout << "What is your name? ";
  getline (std::cin, name);
  std::cout << "Hello, " << name << "!\n";
}

 
**Classes abstraites**  
Aucune instance d’une classe abstraite ne peut ˆetre crée.
L’intérˆet d’une classe abstraite est uniquement de servir de “canevas” `a ses classes dérivées, en déclarant
l’interface minimale commune `a tous ses descendants.

Classe qui ne peut pas être instanciée (on ne peut pas créer d'objet à partir d'elle).  
Une classe devient abstraite si elle a au moins une fonction virtuelle pure.
An abstract base class cannot be instantiated, i. e. you cannot declare an object of class A. You can only derive classes from A, `BUT ANY DERIVED CLASS THAT DOES NOT PROVIDE AN IMPLEMENTATION of foo() WILL ALSO BE ABSTRACT`. In order to stop being abstract, a derived class must provide implementations for all pure virtual functions it inherits.


**Conversion de pointeurs d'objets**   
On a vu que le pointeur de la classe de base peut stocker l'adresse d'objets dérivés. Mais avec un pointeur sur la classe de base on ne peut pas appeler une fonction d'une classe dérivée qui n'est pas virtuelle.
Avant d'appeler la fonction d'une classe dérivée avec un pointeur sur la classe de base, convertir le pointeur:  
pMic = (Micro *)pMat;
Mais cela convertit toujours, même de Mat vers Modem ! il faut un "cast" intelligent

**RTTI (Run-Time Type Identification)**
  
  Permet de convertir proprement les pointeurs d'objets    
  
  dynamic_cast convertit un pointeur d'une classe de base vers un pointeur d'une classe dérivée.     
  PointeurDérivé = dynamic_cast<Classe_Dérivée*>(PointeurAConvertir)    
  *	Renvoi l'adresse de l'objet convertit  
  *	Renvoi NULL si échec    
  La classe de base doit obligatoirement avoir une fonction virtuelle pour utiliser dynamic_cast  

    struct Event { virtual ~Event() {} };
    struct MouseEvent : Event { int x, y; };
    struct KeyboardEvent : Event { int key; };

    void log(Event *event) {
      if (MouseEvent *mouse = dynamic_cast<MouseEvent *>(event))
        std::cout << "MouseEvent " << mouse->x << " " << mouse->y << std::endl;
      else if (KeyboardEvent *keyboard = dynamic_cast<KeyboardEvent *>(event))
        std::cout << "KeyboardEvent " << keyboard->key << std::endl;
      else
        std::cout << "Event" << std::endl;
    }

    dynamic_cast 
        est utilisé uniquement dans le contexte d'une hiérarchie de classes. 
        Il peut être utilisé pour lancer le pointeur d'une classe dans l'une de ses sous-classes. 
        Il est également capable de lancer des références de classe de la même manière.
        Contrôle de sécurité du type au moment de l'exécution pour valider l'opération. Si les pointeurs ou les références ne sont pas du même type (comme le permet ce cast), le cast échoue.
    
    reinterpret_cast 
        considéré comme dangereux 
        le compilateur part du principe que le programmeur sait exactement à quoi s'attendre. 
        Aucun contrôle de validité n'est effectué à la compilation ou à l'exécution. 
        Cette méthode est similaire à celle du casting original de style C.


**Surcharge d'opérateurs** 
En C++, on peut surcharger la plupart des opérateurs usuels du langage, c’est-`a-dire les reprogrammer
pour que, dans un certain contexte, ils fassent autre chose que ce qu’ils font d’habitude
+ for complex number
Les opérateurs d’entrées-sorties << et >> sont en réalité les surcharges de deux opérateurs de décalages de bits (appelés respectivement “shift left” et “shift right”).



```c++
int operator + (Nombre a , Nombre b)
  {
     return a+b;
  };
```
En général on redéfinit 2 surcharges: par pointeur et par référence pour tenir compte de tous les types d'argument possibles.

* opérateur unaire
// Complexe nimber opposite
Complexe Complexe::operator-()
{
   return Complexe(-re, -im);
}

*opérateur binaire
Complexe Complexe::operator-(Complexe u)
{
  return Complexe(re - u.re, im - u.im);
}
// z1 - z2
// z1.operator-(z2)

#Namespaces
Permet d'éviter les conflits de noms: on a plusieurs espaces de noms (namespace) dans une même application.
Cela permet d'avoir des variables et des fonctions ayant le même nom.

```c++
namespace Facturation
{
   float Taux = 0.206;
   void AfficheTaux() { cout << "Taux=" << Taux;}
} // pas de ;
 
namespace RemiseClient
{
   float Taux = 0.20;
   void AfficheTaux() { cout << "Remise=" << Taux;}
} // pas de ;

Usage:
  Facturation::Taux=0.055;	Facturation::AfficheTaux();
  RemiseClient::Taux=0.30;	RemiseClient::AfficheTaux();
or
using namespace Facturation;
  Taux=0.055;
  AfficheTaux();
```

# virtual inheritance 

#include <iostream>

class D {
    public: void foo() { std::cout << "Foooooo" << std::endl; }
};

class C: public D {};
class B: public D {};
class A: public B, public C {};

int main(int argc, const char * argv[]) {
    A a;
    a.foo();
}

   A
 /   \
C     B 
 \   /
   D

If you don’t use virtual inheritance in this case, you will get two copies of D in class A: 
one from B and one from C. 
  In function 'int main(int, const char**)':
  15:7: error: request for member 'foo' is ambiguous
  6:18: note: candidates are: void D::foo()
  6:18: note:                 void D::foo()

To fix this you need to change the declarations of classes C and B to be virtual:

class C: virtual public D {};
class B: virtual public D {};



## virtual methods

essential part of designing a class hierarchy and subclassing classes
Specifically it determines the behavior of overridden methods in certain contexts.
virtual before a method declaration it says that when referring to an instance of 
a superclass by a pointer or reference to a base class that the correct implementation 
should be resolved at run time and that the "highest level" implementation should be used.

  class Foo
  {
     public:
     void f() { std::cout << "Foo::f()" << std::endl; }
     virtual void g() { std::cout << "Foo::g()" << std::endl; }
   };

   class Bar : public Foo
   {
     public:
     void f() { std::cout << "Bar::f()" << std::endl; }
     virtual void g() { std::cout << "Bar::g()" << std::endl; }
   };

   int main()
   {
      Foo foo;
      Bar bar;
      
      // Trivial
      foo.f(); // "Foo::f()"
      foo.g(); // "Foo::g()"

      bar.f(); // "Bar::f()"
      bar.g(); // "Bar::g()"

      // So far everything we would expect...
      Foo *foob = &bar;
      Bar *barbar = &bar;
      foob->f();    // "Foo::f()"
      foob->g();    // "Bar::g()"
      barbar->f();  // "Bar::f()"
      barbar->g();  // "Bar::g()"
      
      return 0;
}


##CLASSES TEMPLATES - PATRONS

classes paramétrées avec des types. Eg: utiliser soit des entiers ou des réels ou des string



template <class T>
Tableau<T>::Tableau(short dim)
{
   taille = dim;
   ptab = new T [taille];
};
template <class T>
Tableau<T>::~Tableau()
{
  delete [] ptab; // libération-mémoire pour un tableau dynamique
};
template <class T>
T &Tableau<T>::operator[](short index)
{
  if (index < 0 || index > taille)
  {
  cout << "\nindice hors du rang...";
  exit(1); // interrompt l’exécution
  }
  return ptab[index];
};

Tableau<int> t(10); // déclare un tableau t contenant 10 entiers
int z;
z = t[1]; // ici, l’indice est automatiquement contr^olé
t[0] = 1; // possible car la surcharge de [] est déclarée de type T&

Tableau<float> u(3); // déclare un tableau u contenant 3 réels

typedef char Mot [20];
Tableau<Mot> t(100); // déclare un tableau t contenant 100 mots


```C++
template <class T >
T Max(T a, T b)
{ return (a>b ) ? a : b ; } 

	bool operator > (Voiture a, Voiture b)
	{
	  long pa = atol(a.Prix) ; 	  long pb = atol(b.Prix) ;
	  return (pa>pb) : true , false ;
}

ostream& operator << (ostream& out, Voiture v)	
{
  cout << v.Marque << v.Prix << endl ;
  return out ;
}

	Voiture V1(« Lotus », « 300000 ») ;
	Voiture V2(« Ford », « 400000 ») ;
	cout << ’’ voiture la plus chère :’’ << Max(V1,V2) ;

```




// Un exemple de définition de classe modèle.

template <class T> class Vector
{
   T *data;
   int size;
public:
   Vector(int);
   ~Vector( ) { delete[ ] data; }
   T& operator[](int i) { return data[i]; }
};

// Notez la syntaxe des définitions hors-lignes.

template <class T> Vector<T>::Vector(int n)
{
   data = new T[n];
   size = n;
};



int main()
{
   Vector<int> x(5);   // Génère un vecteur pour stocker cinq entiers
   for (int i = 0; i < 5; ++i)
      x[i] = i;              //  Initialise le vecteur.

   return 0;
}




// Déclare une fonction modèle avec son corps
template<class T> void sort (T* array, int size)
{
   // Corps de la fonction modèle.
}




template <class T> class B 

{
  // déclarations de classe
};

template <class T> 
class D : public B<T>
{
   // déclarations de classe
};

template <class T> void func(B <T> *b)
{
   // corps de fonction
}
// Ceci est illégal sous ANSI C++: func( int ) non résolu
// Borland C++ appelle func( B<int> * ).

func( new D<int> );











#**EXCEPTIONS - try / catch / Finally**
permet d’intercepter les erreurs et de les gérer
An exception is a mechanism for handling runtime errors in a program
To allow the possibility of performing cleanup operations or ensuring certain code is executed regardless of whether an exception is thrown: __finally

1.	Définir une classe d’exception (fournie des informations sur une erreur)
2.	Lancer l’exception
3.	Intercepter l’exception

```c++
class Erreur
{ 
  // Ajouter des données et fonctions membres pour définir une gestion d’erreur appropriée
} ;

void Positive(int v)
{
   if (v<0)
     {
       Erreur Exec ;        	// construit un objet statique en lui donnant un nom et la possibilité d’utiliser ses membres.
        throw Exec ;	  ces 2 lignes seront simplifiées en throw Erreur() ;
     }
    cout <<  ’’Valeur  Positive’’ << endl ;
}



try
{
  // Code that may throw an exception
}
catch(exception1& e)
{
  // Handler code for exception1 type exceptions
}
catch(exception2& e)
{
  // Handler code for exception2 type exceptions
}
catch(...)
{
  // Handler code for any exception not already caught
}
__finally
{
  // Code here is always executed, even if an exception is thrown in the preceding
  // try block
}

```

**throw**  
Il lance une exception.  
Il est suivi par un objet créé à partir d’une classe d’exception.  
Il permet de quitter la fonction qui l’utilise (les instructions qui le suivent ne seront pas exécutées) et informe la fonction appelante qu’une exception est générée.  
	throw Erreur() ;	// Dans ce cas, on n’attribue pas de nom à l’objet exception. On ne pourra utiliser ses membres.  

This program will terminate abnormally. 
#include <iostream>

class A {
public:
    A() {}
    ~A() {
        throw 42;       //  A destructor will throw 2nd exception during the exception handling, which will cause program to crash
    }
};

int main(int argc, const char * argv[]) {
    try {
        A a;
        throw 32;              // will start unwinding the stack and destroy class A
    } catch(int a) {
        std::cout << a;
    }
}


**Spécification d’exception**    
On peut spécifier les exceptions pouvant être lancées par une fonction :   
Le compilateur contrôlera alors les exceptions envoyées par la fonction.  
Si la fonction ne doit générer aucune exception, on mettra throw ( )  
```c++
void Controle(int v) 	throw( Erreur, Invalide)
{
}

Interception d’une exception : Rien n’oblige à les intercepter.	
try
{
  // Appels de fonctions pouvant générer des exceptions  
}
catch(ClasseException ex)
{
  // Bloc exécuté pour une exception de type ClasseException
  // Permet de récupérer une copie de l’objet envoyé avec throw
}
catch(…)
{
  // Ce bloc s’exécute pour toutes les exceptions en dehors de ClasseException
  // Equivalent au default du switch
}
```

Si une des fonctions du bloc try déclenche une exception :
Tous les objets créés dans le bloc try sont détruits  
Sortie du bloc try au retour de la fonction qui a déclenché l’exception  
Exécution des catch correspondants à l’exception. Sinon sortie du programme  
Si un des blocs catch est utilisé, le programme continue à exécuter les instructions situées après ce bloc s’il y en a.

Après un bloc catch on peut mettre :  
Arrêter le programme avec ou sans message utilisateur.  
Corriger le problème avec ou sans message utilisateur.  
Uniquement informer l’utilisateur.  
Lancer une impression ,un fax, un mail, écrire dans un fichier d’alerte (log).  

```c++
class Erreur
{
   public :
virtual void AfficheMessage() =0;
} ;

class ErreurPositive : public Erreur
{
   public :
virtual void AfficheMessage() ;
} ;

ErreurPositive : :AfficheMessage()
{cout << ‘’Erreur : Valeur négative’’ << endl ;}


class ErreurInf : public Erreur
{
   int Max ;
   public :
virtual void AfficheMessage() ;
ErreurInf(int max) ;
} ;

ErreurInf : :ErreurInf(int max)
{Max=max ;}

ErreurInf : :AfficheMessage()
{   cout << ‘’Erreur : valeur supérieure à ‘’ << Max << endl ;  }

class ErreurSup : public Erreur
{
   int Min;
   public :
virtual void AfficheMessage() ;
ErreurSup(int max) ;
} ;

ErreurSup : :ErreurSup(int min)
{Min=min;}

ErreurSup : :AfficheMessage()
{   cout << ‘’Erreur : valeur inférieure à ‘’ << Min << endl ;  }

```

throw std::invalid_argument("Invalid vector index");



# DEBU

### **MEASURING TIME**
------------
```c++
#include <ctime>
class Timer {
    public:
        Timer(): start(std::clock()) {}

        operator double() const 
                { return (std::clock() - start) / static_cast<double>(CLOCKS_PER_SEC); }

        void reset() { start = std::clock(); }

    private:
        std::clock_t start;
};
```

And here's a test program to time one push_back call on a large, full vector of Widgets (a memory-hogging class):
```
#include <iostream>
#include <exception>
#include <vector>
#include "Widget2.h"
#include "Timer.h"   // for Timer class

int main()
{
    using namespace std;

    vector<Widget> vw(500000);
    while (vw.size() < vw.capacity())
        vw.push_back(Widget());

    cout << "Size of vw: " << vw.size() << endl;

    Timer t;    // initialize timer to current clock time
    vw.push_back(Widget());
    cout << "Time for one push_back on full vector: " << t << endl;
}
```


## ASSER
---------
/*===========================================================================
 * assert
 * If the assertion is non-zero (i.e. true), then it returns.
 * If the assertion is zero (i.e. false), then it display the string and
 * aborts the program.
 * This is ment to act like Python's assert keyword.
 *=========================================================================*/
void assert(int assertion, char* message) {
    if (assertion == 0) {
        fprintf(stderr, "%s\n", message);
        exit(1);
    }
}

If not debugging, assert does nothing, see assert.h:
#define assert(x) ((void)0)


#include <cassert>  idem #include <assert.h>
vector<int> vector1(5);
for (int i=0; i < 5; ++i)
    vector1[i] = i;
random_shuffle(vector1.begin(), vector1.end());
// Sort vector1 using push_heap and pop_heap:
for (int i = 2; i < 5; ++i)    
  push_heap(vector1.begin(), vector1.begin() + i);
for (int i = 5; i >= 2; --i)
  pop_heap(vector1.begin(), vector1.begin() + i);
// Verify that the array is sorted:
for (i = 0; i < 5; ++i)   
assert (vector1[i] == i); // if false, stop program
assert(scan_test != EOF, "Failed to read from file. File is incomplete."); // if false, stop program and print the string

 








### Read File in C++
https://www.geekboots.com/cpp/copy-file
https://visualstudiomagazine.com/articles/2017/01/25/4-ways-transform-file-windows-via-cpp.aspx

stdio.h. It gives low-level access to a file, both in binary or text mode.


#include<iostream>
#include<fstream>
using namespace std;

int main() {
  int item_no;
  string item_name;
  float price;

  /* Connect 'data.txt' to 'wfile' */
  ifstream rfile("data.txt");
  cout << "Read data from file" << endl;

  /* Read Integer */
  rfile >> item_no;

  /* Read string */
  rfile >> item_name;

  /* Read float */
  rfile >> price;
  
  cout << "Item No: " << item_no << endl;
  cout << "Item Name: " << item_name << endl;
  cout << "Price: " << price << endl;

  /* Disconnect 'data.txt' from 'wfile' */
  rfile.close();
  return 0;
}

/****** Output ******/
Read data from file
Item no: 50
Item name: Book
Price: 20.12















### Map - Hash map

https://www.geekboots.com/cpp/map

A map (also called 'hash map' or 'associative array') provides a mapping from keys to their associated values.

ERY FAST LOOK UP in near constant time: O(1) in N elements. Replace 2 nested 'for loops' 
But look up in hash table should be amortized O(1) time as long as the hash function was chosen carefully. 


#include<iostream>
#include<map>
using namespace std;

int main() {

  /* Declare map */
  map <string, float> item;

  /* Map iterator */
  map <string, float> :: iterator p;

  /* Initialize map */
  item["Eraser"] = 0.50;

  /* Insert data */
  item.insert(pair<string, float>("Pen", 2.50));
  item.insert(pair<string, float>("Book", 200.55));
  item.insert(pair<string, float>("Pencil", 1.00));
  item.insert(pair<string, float>("Ex-Book", 250.10));

  string srch = "Book";

  /* Search data */
  p = item.find(srch);
  if(p != item.end())
    cout << "Price of the " << srch << " is " << p->second << endl;
  else
    cout << "Item not found!" << endl;

  /* Erase data */
  item.erase("Pencil");
  cout << "Item Deleted!" << endl;

  /* Display all elements */
  for (p = item.begin(); p != item.end(); p++) 
    cout << "Item: " << p->first << "\t"<< "Price: " << p->second << endl;

  return 0;
}

/****** Output ******/          
Price of the Book is 200.55
Item Deleted!
Item: Book  Price: 200.55
Item: Eraser  Price: 0.5
Item: Ex-Book Price: 250.1
Item: Pen Price: 2.5


// http://www.cplusplus.com/reference/map/map/find/
// map::find
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;
  std::map<char,int>::iterator it;

  mymap['a']=50;
  mymap['b']=100;
  mymap['c']=150;
  mymap['d']=200;

  it = mymap.find('b');
  if (it != mymap.end())
    mymap.erase (it);

  // print content:
  std::cout << "elements in mymap:" << '\n';
  std::cout << "a => " << mymap.find('a')->second << '\n';
  std::cout << "c => " << mymap.find('c')->second << '\n';
  std::cout << "d => " << mymap.find('d')->second << '\n';

  return 0;
}



HashMap


https://leetcode.com/problems/two-sum/solution/
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}


public int[] twoSum(int[] nums, int target) {
  Map<Integer, Integer> map = new HashMap<>();
  for (int i = 0; i < nums.length; i++) {
      int complement = target - nums[i];
      if (map.containsKey(complement)) {
          return new int[] { map.get(complement), i };
      }
      map.put(nums[i], i);
  }
  throw new IllegalArgumentException("No two sum solution");
}



## C++ const keywords

**const Variables**
indicating that you don't intend to change their value after they're initialized. 
const local variables are often used in conjunction with const return values

const int i = 10;
i = 3; // ERROR - we can't change "i"
int &j = i; // ERROR - we promised not to change i
const int &x = i; // fine - "x" is a reference to i

**const Function Arguments**
guarantee that a function will not modify a value that is passed in
This is really only useful for references and pointers (and not things passed by value), though there's nothing syntactically to prevent the use of const for arguments passed by value.

// try to call a non-const method on an argument passed as a const reference
void foo( const std::string &s )
{
   s.append("blah"); // ERROR — we can't modify the string
   std::cout << s.length() << std::endl; // fine
}
void bar( const Widget *w )
{
   w->rotate(); // ERROR - rotate wouldn't be const
   std::cout << w->name() << std::endl; // fine
}

**const Methods**
say that a method does not modify the member variables of a class.
by extension a const method cannot call a nonconst method (and the compiler will complain if you try).

class Foo
{
  public: 
    int value() const { return m_value; }
    void setValue( int i ) { m_value = i; }
  private:
    int m_value;
};


class Foo
{
   public:
   
   // compiler differentiates between const and non-const methods   
   Total *total();          // Modifies m_total and the user may modify the returned widget.
   Total *total() const;    // Does not modify m_total but the user may modify the returned total.
   
   // RETURN VALUES: 
   // compiler doesn't differentiates between const and non-const methods   
   const Total *cTotal();          // Modifies m_total, but the user may not modify the returned total.
   const Total *cTotal() const;    // Does not modify m_total and the user may not modify the returned total.
   
   private:
     Total *m_total;
};

int main()
{
   Foo f;
   Total *w1 = f.total();        // fine
   Total *w2 = f.cTotal();       // ERROR - "cTotal()" returns a const value and "w2" is not const
   const Total *w3 = f.cTotal(); // fine
   return 0;
}


http://www.learncpp.com/cpp-tutorial/812-static-member-functions/

c++ int to string
http://stackoverflow.com/questions/5590381/easiest-way-to-convert-int-to-string-in-c
http://stackoverflow.com/questions/2125880/converting-a-float-to-stdstring-in-c

c++ call base class virtual function


idee vtent
idee monaco, pce, cache muse





http://stackoverflow.com/questions/1986418/typeid-versus-typeof-in-c?bcsi-ac-f36447ef44bbdc17=25D45D2F00000303YjgPtkzBDOcSs5Gsi7E4jaXrlJi0BAAAAwMAAGOGRgAIBwAABAAAAOHxDwA=
typeof is a compile time construct and returns the type as defined at compile time
typeid is a runtime construct and hence gives information about the runtime type of the value.
typeof Refenence: http://www.delorie.com/gnu/docs/gcc/gcc_36.html
typeid Rfeerence: http://en.wikipedia.org/wiki/Typeid
#include <iostream> 
#include <typeinfo>  //for 'typeid' to work 
 
class Person { 
    public:
    // ... Person members ... 
    virtual ~Person() {} 
}; 
 
class Employee : public Person { 
    // ... Employee members ... 
}; 
 
int main () { 
    Person person; 
    Employee employee; 
    Person *ptr = &employee; 
    int t = 3; 
 
    std::cout << typeid(t).name() << std::endl; 
    std::cout << typeid(person).name() << std::endl;   // Person (statically known at compile-time)  
    std::cout << typeid(employee).name() << std::endl; // Employee (statically known at compile-time) 
    std::cout << typeid(ptr).name() << std::endl;      // Person * (statically known at compile-time) 
    std::cout << typeid(*ptr).name() << std::endl;     // Employee (looked up dynamically at run-time 
                                                       // because it is the dereference of a pointer
                                                       // to a polymorphic class) 
 } 
 
 
 
 
 
 
 
 
 


http://stackoverflow.com/questions/25831622/initialize-enum-c
I create an enum called Types:

enum  Types {Int,Double,String};  
"Error: type name is not allowed" When I create an object and initialize it with one of the enum allowed values
Types ty = Types.Double; 

enum Colours { red, green, blue }; or enum Weekdays { monday, tuesday, wednesday, thursday, friday }; 

Your enumeration is unscoped, therefore it suffices to write

Types ty = Double;
For scoped enumerations, as the name suggests, the enumerators are declared in the enumeration scope and have to be qualified with the enumeration-name:

enum class ScopedTypes {Int,Double,String}; enum UnscopedTypes {Int,Double,String}; ScopedTypes a = ScopedTypes::Double; //ScopedTypes b = Double; // error UnscopedTypes c = UnscopedTypes::Double; UnscopedTypes d = Double;
Types ty = Types::Double





# MATRIX

  A matrix is actually an array of arrays.

  int rows = ..., cols = ...;
  int** matrix = new int*[rows];
  for (int i = 0; i < rows; ++i)
      matrix[i] = new int[cols];
  Of course, to delete the matrix, you should do the following:

  for (int i = 0; i < rows; ++i)
      delete [] matrix[i];
  delete [] matrix;



  RETURNING AN ARRAY:

  int *fillarr( int arr[] ) { // arr "decays" to type int *
      return arr;



  ### Matrix Multiplication in C++

  #include<iostream>
  using namespace std;

  class matrix {

    /* Declaration of two dimensional array */
    int a[3][3], b[3][3], ans[3][3];

    public:
      matrix() {
        cout << "Enter data for first array:" << endl;
        for(int i = 0; i < 3; i++)
          for(int j = 0; j < 3; j++)
            cin >> a[i][j];
        cout << "Enter data for second array:" << endl;
        for(int i = 0; i < 3; i++)
          for(int j = 0; j < 3; j++)
            cin >> b[i][j];
      }

      void multiplication() {
        cout << "After matrix multiplication" << endl;
        for(int i = 0; i < 3; i++) {
          for (int j = 0; j < 3; j++) {
            ans[i][j] = 0;
            for(int k = 0; k < 3; k++)
              ans[i][j] += a[i][k] * b[k][j];
            cout << ans[i][j] << "\t";
          }
          cout << endl;
        }
      }
  };

  int main() {
    cout << "Program for calculation of Matrix Multiplication" << endl;
    matrix mtMul = matrix();
    mtMul.multiplication();
    return 0;
  }

  /****** Output ******/
            
  Enter data for first array:
  1 2 3 4 5 6 7 8 9

  Enter data for second array:
  4 4 4 4 4 4 4 4 4

  After matrix multiplication
  24 24 24
  60 60 60
  96 96 96
                      
                  

          
        
switch is only for integral types, if you want to branch depending on a string you need to use if/else.           
C++ switches only work on integer types.  
Switch expressions must evaluate to an integral type

The most trivial way to implement such thing is then to have is a sequence of ifs:

if( str == "foo" ) ... else if( str == "bar" ) ... else







**constructeur avec liste d’initialisation**  
class A
{
public:
  A(){}
  A(int a, int b){}
  int a, b;
};

class B : public A
{
  B(){}
  B(int _a, int _b) : A(_a, _b)
  {
    a = 10;   
  }
};




class z
{
  public:
  z(){}
};

class A : public z
{
public:
  A():z()
  {}
  A(int a, int b):z()
  {}
  int a, b;
};

class B : public A
{
  int c;
  B(){}
  B(int _a, int _b, int _c) : A(_a, _b), c(_c)
  {
    a = 10;   
  }
};








http://www.cplusplus.com/reference/algorithm/max_element/
Define a functor instead:

struct is_invalid
{
    is_invalid(const std::string& a_wanted) : wanted(a_wanted) {}
    std::string wanted;
    bool operator()(const std::string& str)
    {
        return str.compare(wanted) != 0;
    }
};

std::remove_copy_if(first.begin(),
                    first.end(),
                    second.begin(),
                    is_invalid("abc"));
or if C++11 use a lambda:

std::string wanted("abc");
std::remove_copy_if(first.begin(), first.end(), second.begin(), 
    [&wanted](const std::string& str)
    {
        return str.compare(wanted) != 0;
    });







http://www.java2s.com/Code/Cpp/Vector/Callmemberfunctionforeachelementinvector.htm
http://stackoverflow.com/questions/7667376/class-method-in-for-each

http://www.cplusplus.com/forum/beginner/57858/


http://stackoverflow.com/questions/5295616/how-to-deallocate-object-pointer-in-vector


https://www.safaribooksonline.com/library/view/c-cookbook/0596007612/ch04s07.html

http://stackoverflow.com/questions/191757/c-concatenate-string-and-int?noredirect=1&lq=1

http://stackoverflow.com/questions/5878775/how-to-find-and-replace-string
    std::string Wulfsberg_Page::stringReplace(std::string &s,
                          const std::string &toReplace,
                          const std::string &replaceWith)
    {
        std::size_t found = s.find(toReplace);
        if (found != std::string::npos)
            return(s.replace(found, toReplace.length(), replaceWith));
        else
            return s;
    }
http://stackoverflow.com/questions/5343190/how-do-i-replace-all-instances-of-a-string-with-another-string
    std::string Wulfsberg_Page::stringReplace(std::string &s,
                          const std::string &toReplace,
                          const std::string &replaceWith)
    {
        std::size_t found = 0;
        while ( (found = s.find(toReplace, found)) != std::string::npos)
        {        
            s.replace(found, toReplace.length(), replaceWith);
            found += replaceWith.length(); // if 'replaceWith' contains 'toReplace' 
        }        
        return s;
    }


http://www.cplusplus.com/reference/string/string/find/
http://stackoverflow.com/questions/7352099/stdstring-to-char


http://stackoverflow.com/questions/6679096/using-find-if-on-a-vector-of-object

http://fusharblog.com/3-ways-to-define-comparison-functions-in-cpp/

http://stackoverflow.com/questions/5914012/use-stl-find-if-to-find-a-specific-object-in-a-vector-of-object-pointers

http://stackoverflow.com/questions/13525361/can-you-pass-an-additional-parameter-to-a-predicate

http://stackoverflow.com/questions/22713278/accumulate-through-a-vector-of-pointers


 










math.h:
-------

reste = fmod( nb , diviseur) // pour pair/impair

 if (fmod( ACol,2)) // pair   // inclure math.h !!
 else // impair

#define M_E         2.71828182845904523536
#define M_LOG2E     1.44269504088896340736
#define M_LOG10E    0.434294481903251827651
#define M_LN2       0.693147180559945309417
#define M_LN10      2.30258509299404568402
#define M_PI        3.14159265358979323846
#define M_PI_2      1.57079632679489661923
#define M_PI_4      0.785398163397448309616
#define M_1_PI      0.318309886183790671538
#define M_2_PI      0.636619772367581343076
#define M_1_SQRTPI  0.564189583547756286948
#define M_2_SQRTPI  1.12837916709551257390
#define M_SQRT2     1.41421356237309504880
#define M_SQRT_2    0.707106781186547524401


double acos(double x)                     arc cosine of x (in radians)
double asin(double x)                     arc sine of x (in radians)
double atan(double x)                     arc tangent of x (in radians)
double atan2(double y, double x)          arc tangent (in radians) of y/x based on the signs of both values to determine the correct quadrant
double cos(double x)                      cosine of a radian angle x
double cosh(double x)                     hyperbolic cosine of x
double sin(double x)                      sine of a radian angle x
double sinh(double x)                     hyperbolic sine of x
double tanh(double x)                     hyperbolic tangent of x
double exp(double x)                      value of e raised to the xth power
double frexp(double x, int *exponent)     value is the mantissa and the integer pointed to by exponent is the exponent. The resultant value is x = mantissa * 2 ^ exponent
double ldexp(double x, int exponent)      multiplied by 2 raised to the power of exponent
double log(double x)                      natural logarithm (base-e logarithm) of x
double log10(double x)                    common logarithm (base-10 logarithm) of x
double modf(double x, double *integer)    value is the fraction component (part after the decimal), and sets integer to the integer component 
double pow(double x, double y)            raised to the power of y
double sqrt(double x)                     square root of x
double ceil(double x)                     smallest integer value greater than or equal to x
double fabs(double x)                     absolute value of x
double floor(double x)                    largest integer value less than or equal to x
double fmod(double x, double y)           remainder of x divided by y









# Obscure C++ Features

[] Square brakets:  ptr[3] is short for *(ptr + 3) or *(3 + ptr) or 3[ptr] which turns out to be completely valid code.
int y = 3; is equivalent to int(y) = 3

Alternate operator tokens: type operators that lack the necessary symbols
  &&      ↔    and
  &=      ↔    and_eq
  &       ↔    bitand
  |       ↔    bitor
  ~       ↔    compl
  !       ↔    not
  !=      ↔    not_eq
  ||      ↔    or
  |=      ↔    or_eq
  ^       ↔    xor
  ^=      ↔    xor_eq
  {       ↔    <%
  }       ↔    %>
  [       ↔    <:
  ]       ↔    :> 
          ...
 

Redefining keywords
  preprocessor redefining keywords is allowed (no errors). Fun bug-introducing stuff 
    #define true false
    #define else
  Legitimately useful times: 
    bypass the C++ access protection mechanism in  a large library instead of patching the 
    library you can just turn off access protection before including the headers for the library. 
    Remember to turn the protection back on afterwards!

  #define class struct
  #define private public
  #define protected public

  #include "library.h"

  #undef class
  #undef private
  #undef protected

  Note that this may not necessarily work depending on your compiler. 
  C++ only requires instance variables to be laid out sequentially when they are not 
  separated by an access specifier, so the compiler is free to change the memory layout 
  by reordering access specifier groups. For example, a compiler is allowed to move all 
  private members so they come after after all public members. Another potential problem 
  is name mangling; Microsoft's C++ compiler incorporates the access specifier into their 
  name mangling scheme so changing the access specifier will break compatibility with existing 
  compiled code.

Placement new: allocate objects sequentially for performances
 
  'new' alternate syntax that runs in place on an already allocated object, 
  which is assumed to be the correct size and have the correct alignment. 
  This involves setting up the vtable and calling the constructor.

  For performance-critical scenarios when writing custom allocators 
  Ex: A slab allocator starts with a single large chunk of memory and uses placement new
      to allocate objects sequentially within the chunk. 
      This avoids memory fragmentation and the overhead of heap traversal that malloc incurs.

  #include <iostream>
  using namespace std;

  struct Test {
    int data;
    Test() { cout << "Test::Test()" << endl; }
    ~Test() { cout << "Test::~Test()" << endl; }
  };

  int main() {
    Test *ptr = (Test *)malloc(sizeof(Test));    // Must allocate our own memory
    new (ptr) Test;  // Use placement new
    ptr->~Test();    // Must call the destructor ourselves
    free(ptr);       // Must release the memory ourselves
    return 0;
  }

Branch on variable declaration

  in the condition of 'if', 'while'
  shorthand for simultaneously declaring a variable and branching on its value
    
  struct Event { virtual ~Event() {} };
  struct MouseEvent : Event { int x, y; };
  struct KeyboardEvent : Event { int key; };

  void log(Event *event) {
    if (MouseEvent *mouse = dynamic_cast<MouseEvent *>(event))
      std::cout << "MouseEvent " << mouse->x << " " << mouse->y << std::endl;
    else if (KeyboardEvent *keyboard = dynamic_cast<KeyboardEvent *>(event))
      std::cout << "KeyboardEvent " << keyboard->key << std::endl;
    else
      std::cout << "Event" << std::endl;
  }

Ref-qualifiers on member functions (C++11) 

  Uses a ref-qualifier to overload member functions on the object's value type
  A ref-qualifier sits in the same position as a cv-qualifier and affects overload resolution depending on if the object for this is an lvalue or an rvalue:

  #include <iostream>

  struct Foo {
    void foo() & { std::cout << "lvalue" << std::endl; }
    void foo() && { std::cout << "rvalue" << std::endl; }
  };

  int main() {
    Foo foo;
    foo.foo();   // Prints "lvalue"
    Foo().foo(); // Prints "rvalue"
    return 0;
  }

Turing complete template metaprogramming
  
  C++ templates
     = compile-time metaprogramming = programs generate other programs
     Designed for simple type substitutions 
     Powerful enough to perform arbitrary calculations, albeit very awkwardly and inefficiently
     Computation is done :

    // Recursive template for general case
    template <int N>
    struct factorial { enum { value = N * factorial<N - 1>::value }; };

    // Template specialization for base case
    template <>
    struct factorial<0> { enum { value = 1 }; };

    enum { result = factorial<5>::value }; // 5 * 4 * 3 * 2 * 1 == 120

  C++ templates can be thought of as a functional programming language since they use recursion instead of iteration and contain no mutable state. You can create a variable that holds a type via typedef and a variable that holds an int via enum. Data structures are embedded in types themselves:

  // Compile-time list of integers
  template <int D, typename N>
  struct node {
    enum { data = D };
    typedef N next;
  };
  struct end {};

  // Compile-time sum function
  template <typename L>
  struct sum {
    enum { value = L::data + sum<typename L::next>::value };
  };
  template <>
  struct sum<end> {
    enum { value = 0 };
  };

  // Data structures are embedded in types
  typedef node<1, node<2, node<3, end> > > list123;
  enum { total = sum<list123>::value }; // 1 + 2 + 3 == 6
  While these examples are pretty useless, template metaprogramming enables some useful things like being able to manipulate lists of types. However, the programming language formed by C++ templates has terrible usability, so try to use it sparingly and in small amounts. Template code is hard to read, slow to compile, and very difficult to debug due to incredibly long and cryptic compiler error messages.

Pointer-to-member operators
  
  To describe a pointer to a certain member on any instance of a class. 
  There are two pointer-to-member operators
    .*  for values 
    ->* for pointers

  #include <iostream>
  using namespace std;

  struct Test {
    int num;
    void func() {}
  };

  // Extra "Test::" in the pointer type
  //      ↓                 ↓ 
  int Test::*ptr_num = &Test::num;
  void (Test::*ptr_func)() = &Test::func;

  int main() {
    Test t;
    Test *pt = new Test;

    // Call the stored member function
    (t.*ptr_func)();
    (pt->*ptr_func)();

    // Set the variable in the stored member slot
    t.*ptr_num = 1;
    pt->*ptr_num = 2;

    delete pt;
    return 0;
  }
  
  For writing libraries
  For example, Boost::Python (a library for binding C++ to Python objects) uses member pointers to easily refer to 
  members when wrapping objects:

  #include <iostream>
  #include <boost/python.hpp>
  using namespace boost::python;

  struct World {
    std::string msg;
    void greet() { std::cout << msg << std::endl; }
  };

  BOOST_PYTHON_MODULE(hello) {
    class_<World>("World")
      .def_readwrite("msg", &World::msg)
      .def("greet", &World::greet);
  }
  Keep in mind when using member function pointers that they are different from regular function pointers. 
  Casting between a member function pointer and a regular function pointer will not work. 
  For example, member functions in Microsoft's compilers use an optimized calling convention called thiscall 
  that puts the this parameter in the ecx register, while normal functions use a calling convention that passes all arguments on the stack.

  Also, member function pointers may be up to four times larger than regular pointers. The compiler may need to store the address of the function body, the offset to the correct base (multiple inheritance), the index of another offset in the vtable (virtual inheritance), and maybe even the offset of the vtable inside the object itself (for forward declared types).

  #include <iostream>

  struct A {};
  struct B : virtual A {};
  struct C {};
  struct D : A, C {};
  struct E;

  int main() {
    std::cout << sizeof(void (A::*)()) << std::endl;
    std::cout << sizeof(void (B::*)()) << std::endl;
    std::cout << sizeof(void (D::*)()) << std::endl;
    std::cout << sizeof(void (E::*)()) << std::endl;
    return 0;
  }

  // 32-bit Visual C++ 2008:  A = 4, B = 8, D = 12, E = 16
  // 32-bit GCC 4.2.1:        A = 8, B = 8, D = 8,  E = 8
  // 32-bit Digital Mars C++: A = 4, B = 4, D = 4,  E = 4
  All member function pointers in the Digital Mars compiler are the same size due to a clever design that generates "thunk" functions to apply the right offsets instead of storing the offsets in the pointer itself.

Static methods on instances

  invoke static methods from an instance in addition to invoking them from the type. 
  This lets you change an instance method to a static method without needing to update any call sites.

  struct Foo {
    static void foo() {}
  };

  // These are equivalent
  Foo::foo();
  Foo().foo();

Overloading ++ and --
  
  C++ is designed so the function name of custom operators is the operator symbol itself, which works fine in most cases. 
  For example, the unary - and binary - operators (negation and subtraction) can be distinguished by the argument count. 
  This doesn't work for the unary increment and decrement operators though since they both seem to need the exact same signature. 
  The C++ language has an ugly hack to work around this: the postfix ++ and -- operators must take a dummy int 
  argument as a flag for the compiler to know to make a postfix operator (and yes, only the type int works).

  struct Number {
    Number &operator ++ (); // Generate a prefix ++ operator
    Number operator ++ (int); // Generate a postfix ++ operator
};

Operator overloading and evaluation order
  
  Overloading the , (comma), ||, or && operators is very confusing because it destroys the normal evaluation rules. 
  Normally, the comma operator guarantees that the entire left side will be evaluated before evaluation starts on the 
  right side and the || and && operators have short-circuit behavior that only evaluates the right side when necessary. 
  However, the overloaded versions of these operators are just function calls, and function calls evaluate their 
  arguments in an unspecified order.

  Overloading these operators is just a way to abuse C++ syntax. 
  As an example, I give you a C++ implementation of a Python-style print statement that doesn't need parentheses:

  #include <iostream>

  namespace __hidden__ {
    struct print {
      bool space;
      print() : space(false) {}
      ~print() { std::cout << std::endl; }

      template <typename T>
      print &operator , (const T &t) {
        if (space) std::cout << ' ';
        else space = true;
        std::cout << t;
        return *this;
      }
    };
  }

  #define print __hidden__::print(),

  int main() {
    int a = 1, b = 2;
    print "this is a test";
    print "the sum of", a, "and", b, "is", a + b;
    return 0;
  }

Functions as template parameters

  Template parameters can be 
    . specific integers 
    . specific functions. This lets the compiler inline calls to that specific function in the instantiated template code 
                          for more efficient execution. 
                          In the example below, the function memoize takes a function as a template parameter and only calls 
                          the function for new argument values (old argument values are remembered from the cache).

  #include <map>

  template <int (*f)(int)>   // ptr on a function returning an int and accepting an int as argument
  int memoize(int x) {
    static std::map<int, int> cache;
    std::map<int, int>::iterator y = cache.find(x);
    if (y != cache.end()) return y->second;
    return cache[x] = f(x);
  }

  int fib(int n) {
    if (n < 2) return n;
    return memoize<fib>(n - 1) + memoize<fib>(n - 2);
  }

Template template parameters

  Template parameters can actually have template parameters themselves. 
  Allows to pass templated types without template parameters when instantiating a template. 

  template <typename T>
  struct Cache { ... };

  template <typename T>
  struct NetworkStore { ... };

  template <typename T>
  struct MemoryStore { ... };

  template <typename Store, typename T>
  struct CachedStore {
    Store store;
    Cache<T> cache;
  };

  CachedStore<NetworkStore<int>, int> a;
  CachedStore<MemoryStore<int>, int> b;
  CachedStore puts a cache that holds a certain data type in front of a store that stores the same data type. 
  However, we must repeat the data type (int in the code above) when instantiating a CachedStore, once for the 
  store itself and once for CachedStore, and there's no guarantee that the data types are consistent. 
  We really want to just specify the data type once so we can enforce this invariant, but leaving off the type 
  parameter list causes a compile error:

  // These do not compile because NetworkStore and MemoryStore are missing type parameters
  CachedStore<NetworkStore, int> c;
  CachedStore<MemoryStore, int> d;
  Template template parameters let us get the syntax we want. 
  Note that you need to use the class keyword for template parameters that themselves have template parameters.

  template <template <typename> class Store, typename T>
  struct CachedStore2 {
    Store<T> store;
    Cache<T> cache;
  };

  CachedStore2<NetworkStore, int> e;
  CachedStore2<MemoryStore, int> f;
  
Function try blocks

  To catch errors thrown while evaluating a constructor's initializer list. 
  You can't wrap a normal try-catch block around the initializer list because it exists outside the function body. 
  To fix this, C++ allows a try-catch block to serve as the body of a function:

  int f() { throw 0; }

  // Here there is no way to catch the error thrown by f()
  struct A {
    int a;
    A::A() : a(f()) {}
  };

  // The value thrown from f() can be caught if a try-catch block is used as
  // the function body and the initializer list is moved after the try keyword
  struct B {
    int b;
    B::B() try : b(f()) {
    } catch(int e) {
    }
  };
  Oddly enough, this syntax isn't just limited to constructors but is available for all function definitions.



name mangling
  Microsoft's C++ compiler incorporates the access specifier into names mangling scheme


# volatile 
    informs the compiler that a variable may change without the compiler knowing it. 
    Variables that are declared as volatile will not be cached by the compiler, and will thus always be read from memory.

# mutable 
    can be used for class member variables. Mutable variables are allowed to change from within const member functions of the class.

# storage class
    A class that specifies the life and scope of its variables and functions is called a storage class.
    In C++ following the storage classes are supported: auto, static, register, extern, and mutable.
    Note, however, that the keyword register was deprecated in C++11. In C++17, it was removed and reserved for future use.    


# COMPILATION BEHAVIOR ON 32/64

  #include <iostream>

  struct A
  {
      int data[2];

      A(int x, int y) : data{x, y} {}
      virtual void f() {}
  };

  int main(int argc, char **argv)
  {
      A a(22, 33);

      int *arr = (int *) &a;
      std::cout << arr[2] << std::endl;

      return 0;
  }    

  g++ question_vptr.cpp -m32 -std=c++11
  g++ question_vptr.cpp -std=c++11

  In the main function the instance of struct A is treated as an array of integer values. On 32-bit architectures the output will be 33, and on 64-bit architectures it will be 22. This is because there is virtual method f() in the struct which makes compiler insert a vptr pointer that points to vtable (a table of pointers to virtual functions of class or struct). On 32-bit architectures the vptr takes 4 bytes of the struct instance and the rest is the data array, so arr[2] represents access to second element of the data array, which holds value 33. On 64-bit architectures the vptr takes 8 bytes so arr[2] represents access to the first element of the data array, which holds 22.

  This question is testing knowledge of virtual functions internals, and knowledge of C++11-specific syntax as well, because the constructor of A uses the extended initializer list of the C++11 standard.





----

# C#
lorem.........
lorem.........

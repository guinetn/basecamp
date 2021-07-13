# C

    hello.c
        #include <stdio.h>
        #include <stdlib.h>

        int main()
        {
          printf("Hello World\n");
          return EXIT_SUCCESS;
        }


        open FOLDER! in vscode  
        F5 ... choose C++ (GDB/LLDB)...     Need to have C/C++ Extension

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
        CTRL+SHIFT+B to run


    !! !! select the .c file before doing CTRL-SHIFT-B !!!
    {
        // See https://go.microsoft.com/fwlink/?LinkId=733558
        // for the documentation about the tasks.json format
        "version": "2.0.0",
        "tasks": [
            {
                "label": "Compile C File",
                "type": "shell",
                "command": "gcc ${file} -g -o ${fileBasename}.exe",     or C:\\mingw-w64\\...\\bin\\gcc if gcc not in path
                                                                        or if a dll is needed:  command": "gcc myapp.c sqlite3.dll -o myapp.exe
                "group": {
                    "kind": "build",                                    = CTRL+SHIFT+B
                    "isDefault": true
                }
            }
        ]
    }

    Try this to log: 
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
                "args": ["c:\\out\\data\\imports\\001.sqlite3", "select name, age, email from clients"],
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


## C++

https://code.visualstudio.com/docs/languages/cpp

You need a compiler: 
- https://wikipedia.org/wiki/GNU_Compiler_Collection
- https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download

>g++ --version
>gdb --version

mkdir HelloWorld
cd HelloWorld
code .

```c++
#include <iostream>
using namespace std;
int main()
{
    cout << "Hello World" << endl;
}
```
Ctrl+Shift+B    Terminal > Run Build Task
    if MinGW → choose C/C++: g++.exe build active file
.\helloworld


## C##

Visual Studio Code uses the power of Roslyn and OmniSharp to offer an enhanced C# experience.
`OmniSharp` is a set of OSS projects that work together for bringing .NET development to any text editor. 
The base layer is a server that runs Roslyn and analyzes the files of the project that is open inside the editor. 
OmniSharp extensions have been developed for the most popular text editors on the market.

C# for Visual Studio Code (powered by OmniSharp)
- https://github.com/OmniSharp
- https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp
- https://code.visualstudio.com/docs/languages/csharp

## C## interactive mode
Right-click → Execute

## Python interactive mode

- [VSCode's Python Interactive mode](https://www.youtube.com/watch?v=lwN4-W1WR84&t=358s)
Create a xxxx.py    Type # %%   → You get a python notebook	


## JS

* QUOKKA
JavaScript and TypeScript playground in your editor.
>quokka

- https://quokkajs.com/docs/#getting-started    

    Live js scratchpad  
        Ctrl+K, release then Q → start Quokka terminal
        Ctrl+K, release then E → stop Quokka terminal

        Ctrl+Shift+P → Quokka
    new quokka file: Cmd/Ctrl + K, J for JavaScript, T for TypeScript

* wallabyjs
- https://wallabyjs.com/
runs your JavaScript tests immediately as you type and displays execution results in your code editor.

# POWERSHELL

    code --install-extension ms-vscode.powershell

    hello.ps1
        Write-Host "Hello World!"

    F5 (a folder must have been opened)    
    .vscode/launch.json 
        {
            // Use IntelliSense to learn about possible attributes.
            // Hover to view descriptions of existing attributes.
            // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "PowerShell: Launch Current File",
                    "type": "PowerShell",
                    "request": "launch",
                    "script": "${file}",
                    "cwd": "${file}"
                }
            ]
        }

# GO

{
    "version": "2.0.0",
    "tasks": [{
     "label": "cargo build",
     "type": "shell",
     "command": "cargo build",
     "args": [],
     "group": {
       "kind": "build",
       "isDefault": true
     }
    },
    {
        "label": "cargo run",
        "type": "shell",
        "command": "cargo",
        "args": [
          "run"
          // "--release",
          // "--",
          // "arg1"
        ],
        "group": {
          "kind": "build",
          "isDefault": true
        }
       }]
  }

# GULP

    https://css-tricks.com/run-gulp-as-you-open-a-vs-code-project/

    {
      "version": "2.0.0",
      "tasks": [
        {
          "label": "Run Gulp",
          "command": "gulp",
          "type": "shell",
          "runOptions": {
            "runOn": "folderOpen"
          }
        }
      ]
    }
    
# MERMAID

ext install vscode-mermaid-preview
https://marketplace.visualstudio.com/items?itemName=vstirbu.vscode-mermaid-preview
https://github.com/vstirbu/vscode-mermaid-preview
https://mermaid-js.github.io/mermaid/#/flowchart   doc

CTRL-SHIFT-P → Preview mermaid diagram

```html
<div class="mermaid">
sequenceDiagram
# A->> B: Query
# B->> C: Forward query
# Note right of C: Thinking...
# C->> B: Response
# B->> A: Forward response
</div>
```

# Typescript

```ts
{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "type": "typescript",
      "tsconfig": "tsconfig.json",
      "problemMatcher": ["$tsc"],
      "group": {
        "kind": "build",
        "isDefault": true
      }
    }
  ]
}
```

# TASKS: External Tools Integration

* Tasks
linting, building, packaging, testing, deploying… to edit, compile, test, debug  
Build systems: Make, Ant, Gulp, Jake, Rake, MSBuild  
Linters: ESLint,  TSLint 
Mostly run from the command line and automate jobs  

VSCode Tasks 
    - Can be configured to run scripts and start processes without using the manual cli
    Extensions can also contribute tasks using a Task Provider
    - Autodetection for: Gulp, Grunt, Jake, npm.
       {
        "typescript.tsc.autoDetect": "off",
        "grunt.autoDetect": "off",
        "jake.autoDetect": "off",
        "gulp.autoDetect": "off",
        "npm.autoDetect": "off"
        }

.vscode\tasks.json

    https://code.visualstudio.com/docs/editor/tasks
    Execute a task from the command palette... 

    Menu 'Terminal'
        Run Build Task
        Run Task
        Run Active file
        Run Selected Text
        Configure Tasks


    CTRL + SHIT + P → Tasks:Run Tasks       Show ALL TASKS (bring up the command palette)
    CTRL + SHIT + B → SHOW BUILD TASKS      Show BUILD TASKS (present in `group: build`)
    {
        "version": "2.0.0",
        "tasks": [{
        "label": "cargo build",
        "type": "shell",                    ←
        "command": "cargo build",
        "args": [],
        "group": {
            "kind": "build",                ←
            "isDefault": true
        }...

    Add A task
        VSCode Menu → Terminal → Configure Tasks → Select one → it is copied in tasks.json
        CTRL + SHIT + P → Tasks: Configure Tasks
                        → Configure Tasks → Select a template

## Task properties

- Label           Task's label used in the user interface.
- Type            Task's type 
    > shell    bash, cmd, PowerShell
    > process  process to execute
- Command         Actual command to execute.
- Windows         Windows specific properties, used instead of the default properties when the command is executed on the Windows.
- Group           Group the task belongs. Command Palette → 'Run group Task'
- Presentation    How to handle task output in the user interface (Integrated Terminal: a new terminal is created on every task run)
- Options         Override cwd defaults (current working directory), env (environment variables), shell (default shell). Options can be set per task but also globally or per platform. Environment variables configured here can only be referenced from within your task script or process and will not be resolved if they are part of your args, command, or other task attributes.
- RunOptions      Defines when and how a task is run.

## Configure Tasks

{
  "label": "dir",
  "type": "shell",
  "command": "dir 'folder with spaces'",
}

{
  "label": "dir",
  "type": "shell",
  "command": "dir 'folder with spaces'",
   "options": {
        "cwd": "${workspaceFolder}/client"
      }
}

Output behavior: how the Integrated Terminal panel behaves when running tasks

    reveal: whether the Integrated Terminal panel is brought to front
        always  - The panel is always brought to front. This is the default.
        never   - The user must explicitly bring the terminal panel to the front using the View > Terminal command (Ctrl+`).
        silent  - The terminal panel is brought to front only if the output is not scanned for errors and warnings.
    focus: whether the terminal is taking input focus or not. Default is false.
    echo: executed command is echoed in the terminal. Default is true.
    showReuseMessage: show the "Terminal will be reused by tasks, press any key to close it" message.
    panel: terminal instance is shared between task runs. Possible values are:
        shared: The terminal is shared and the output of other task runs are added to the same terminal.
        dedicated: The terminal is dedicated to a specific task. If that task is executed again, the terminal is reused. However, the output of a different task is presented in a different terminal.
        new: Every execution of that task is using a new clean terminal.
    clear: terminal is cleared before this task is run. Default is false.
    group: task is executed in a specific terminal group using split panes. Tasks in the same group (specified by a string value) will use split terminals to present instead of a new terminal panel.

{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "npm",
      "script": "lint",
      "problemMatcher": ["$eslint-stylish"],
      "presentation": {
        "reveal": "never"
      }
    }
  ]
}

* COMMANDS ARGS

{
  "label": "dir",
  "type": "shell",
  "command": "dir",
  "args": ["folder with spaces"]
}

{
  "label": "dir",
  "type": "shell",
  "command": "dir",
  "args": [
    {
      "value": "folder with spaces",
      "quoting": "escape"                   quote control: escape, strong ',  weak " = evaluate
    }
  ]
}

* PS Character escaping 

"tasks": [
    {
        "label": "PowerShell example 1 (unexpected escaping)",
        "type": "shell",
        "command": "Get-ChildItem \"Folder With Spaces\""
    },
    {
        "label": "PowerShell example 2 (expected escaping)",
        "type": "shell",
        "command": "Get-ChildItem",
        "args": ["Folder With Spaces"]
    },
    {
        "label": "PowerShell example 3 (manual escaping)",
        "type": "shell",
        "command": "& Get-ChildItem \\\"Folder With Spaces\\\""
    }
]

{
    "version": "0.1.0",
    "command": "explorer",    
    "windows": {
        "command": "explorer.exe"
    },
    "args": ["test.html"]   or  ["${file}"]
}

{        
    "version": "2.0.0",
    "tasks": [
        {
        "type": "npm",
        "script": "lint",
        "problemMatcher": ["$eslint-stylish"]
        }
    ]
}


{
    "version": "2.0.0",
    "tasks": [
        {

            "label": "Chrome",
            "type": "process",
            "command": "chrome.exe",
            "windows": {
                "command": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            },
            "args": [
                "${file}"
            ],
            "problemMatcher": []
        }
    ]
}


{
    "version": "2.0.0",
    "tasks": [
        {
        "label": "Run tests",
        "type": "shell",
        "command": "./scripts/test.sh",
        "windows": {
            "command": ".\\scripts\\test.cmd"
        },
        "group": "test",
        "presentation": {
            "reveal": "always",
            "panel": "new"
        }
        }
    ]
}

* BINDING KEYBOARD SHORTCUTS TO TASKS

To run a task frequently, you can define a keyboard shortcut

.vscode/keybindings.json
{
    "key": "ctrl+g",
    "command": "workbench.action.tasks.runTask",
    "args": "Chrome"
}

{
  "key": "ctrl+h",
  "command": "workbench.action.tasks.runTask",
  "args": "Run tests"
}





linux:


0.1.0 configuration:

{
  "version": "0.1.0",
  "isShellCommand": true,
  "command": "script",
  "tasks": [
    {
      "taskName": "Run tests",
      "suppressTaskName": true,
      "args": ["test"]
    }
  ]
}

The corresponding 2.0.0 configuration would look like this:

{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run tests",
      "type": "shell",
      "command": "script test"
    }
  ]
}



{
    "version": "0.1.0",                 old...
    "linux": {
        "command": "xdg-open"
    },
    "isShellCommand": true,
    "showOutput": "never",
    "args": ["${file}"]
}

mac
{
    "version": "0.1.0",
    "command": "Chrome",
    "osx": {
        "command": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    },
    "args": [
        "${file}"
    ]
}


{
    "version": "0.1.0",
    "command": "gcc",
    "args": ["-Wall", "helloWorld.c", "-o", "helloWorld"],
    "problemMatcher": {
        "owner": "cpp",
        "fileLocation": ["relative", "${workspaceRoot}"],
        "pattern": {
            "regexp": "^(.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
            "file": 1,
            "line": 2,
            "column": 3,
            "severity": 4,
            "message": 5
        }
    }
}

## VSCode internal variable - Variable substitution

VS Code supports variable substitution inside strings in the tasks.json

* VARIABLES REFERENCE
${workspaceFolder}              absolute path to project’s root directory
${file}                         active file 

```json
{
  "label": "TypeScript compile",
  "type": "shell",
  "command": "tsc ${file}",
  "problemMatcher": ["$tsc"]
}
```

* CONFIGURATION VARIABLES: ${config:NAME}
Reference project's configuration settings: prefix the name with 
${config:python.pythonPath}

-  https://code.visualstudio.com/docs/editor/variables-reference

```json
{
  "label": "autopep8 current file",
  "type": "process",
  "command": "${config:python.pythonPath}",
  "args": ["-m", "autopep8", "-i", "${file}"]
}
```

* ENVIRONMENT VARIABLES: ${env:USERNAME}

```json
{
  "type": "node",
  "request": "launch",
  "name": "Launch Program",
  "program": "${workspaceFolder}/app.js",
  "cwd": "${workspaceFolder}",
  "args": ["${env:USERNAME}"]
}
```
* INPUT VARIABLES: ${input:variableID}

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "task name",
      "command": "${input:variableID}"
      // ...
    }
  ],
  "inputs": [
    {
      "id": "variableID",
      "type": "type of input variable"
      // type specific configuration attributes
    }
  ]
}
```





```json
tasks.json
{        
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
```

## Compound tasks
compose tasks out of simpler tasks with the dependsOn property

starts both build scripts in separate terminals for client & server:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Client Build",
      "command": "gulp",
      "args": ["build"],
      "options": {
        "cwd": "${workspaceFolder}/client"
      }
    },
    {
      "label": "Server Build",
      "command": "gulp",
      "args": ["build"],
      "options": {
        "cwd": "${workspaceFolder}/server"
      }
    },
    {
      "label": "Build",
      "dependsOn": ["Client Build", "Server Build"]
    }
  ]
}
```

{
  "label": "One",
  "type": "shell",
  "command": "echo Hello ",
  "dependsOrder": "sequence",       ← task dependencies are executed in the order they are listed in dependsOn
  "dependsOn": ["Two", "Three"]
}

## Detect problems
Compilers and linting tools... produce their own style of errors and warnings 
ex: helloWorld.c:5:3: warning: implicit declaration of function ‘prinft’
A matcher that captures warning and errors
VSCode can process tasks output with problem matchers

problem matchers 'in-the-box':

```json
{
  "label": "TypeScript compile",
  "type": "shell",
  "command": "tsc ${file}",
  "problemMatcher": ["$tsc"]
}
```
your own problem matcher

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "build",
      "command": "gcc",
      "args": ["-Wall", "helloWorld.c", "-o", "helloWorld"],
      "problemMatcher": {
            // helloWorld.c:5:3: warning: implicit declaration of function ‘prinft’
            // The problem is owned by the cpp language service.
            "owner": "cpp",
            // The file name for reported problems is relative to the opened folder.
            "fileLocation": ["relative", "${workspaceFolder}"],
            // The actual pattern to match problems in the output.
            "pattern": {
                // The regular expression. Example to match: helloWorld.c:5:3: warning: implicit declaration of function ‘printf’ [-Wimplicit-function-declaration]
                "regexp": "^(.*):(\\d+):(\\d+):\\s+(warning|error):\\s+(.*)$",
                // The first match group matches the file name which is relative.
                "file": 1,
                // The second match group matches the line on which the problem occurred.
                "line": 2,
                // The third match group matches the column at which the problem occurred.
                "column": 3,
                // The fourth match group matches the problem's severity. Can be ignored. Then all problems are captured as errors.
                "severity": 4,
                // The fifth match group matches the message.
                "message": 5
            }
        }
    }
}
```





run it in multiple browsers for windows
{
    "version": "0.1.0",
    "command": "cmd",
    "args": ["/C"],                      ← Windows need to pass the '/C' arg to cmd so that the tasks arguments are run.
    "isShellCommand": true,
    "showOutput": "always",
    "suppressTaskName": true,
    "tasks": [
        {   
            "label": "Chrome",
            "args": ["start chrome -incognito \"${file}\""]
        },
        {   
            "label": "Firefox",
            "args": ["start firefox -private-window \"${file}\""]
        },
        {   
            "label": "Edge",  //  Edge is my default browser just gave it the name of the file.
            "args": ["${file}"]
        }   
    ]
}

{
"version": "0.1.0",
"command": "opera",
"windows": {
    "command": "///Program Files (x86)/Opera/launcher.exe"
},
"args": ["${file}"] }

* Sample

pre-release.sh
```bash
#!/bin/sh
date > .version
git commit --allow-empty -m "do-production-release"
```

>bash .vscode/pre-release.sh

1. Setting Tasks

.vscode/tasks.json
```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Pre-Release Setup",                               ← to identify the script in the VS Code Command Palette.
            "type": "shell",                                            ← to execute a shell script
            "command": "bash",                                          ← the command to which the arguments can be passed
            "args": ["${workspaceFolder}/.vscode/pre-release.sh"]       ← array that provides arguments to the command
        }
    ]
}
```




2. Running Tasks
Ctrl + Shift + P → type `Tasks: Run Task` → Present the list of tasks specified in the tasks.json 

* Debug .NET Core console app 

    {
        // See https://go.microsoft.com/fwlink/?LinkId=733558
        // for the documentation about the tasks.json format
        "version": "0.1.0",
        "command": "dotnet",
        "isShellCommand": true,
        "args": [],
        "tasks": [
            {
                "taskName": "build",                      //  argument le chemin vers le fichier .csproj à la tâche de build de votre projet
                "args": [],                               "args": ["${workspaceRoot}\\testapp.csproj"],   
                "isBuildCommand": true,
                "showOutput": "silent",
                "problemMatcher": "$msCompile"
            }
        ]
    }    

    {
    "version": "2.0.0",
    "tasks": [
        {
        "label": "Run tests",
        "type": "shell",
        "command": "dotnet"
        }
    ]
    }
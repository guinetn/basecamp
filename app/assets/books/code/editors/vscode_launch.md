# launch.json

.vscode\launch.json

Paramètres de configuration qui seront utilisés par Visual Studio Code pour lancer le programme qui s’occupe de la génération (msbuild) 

# DEBUG

https://code.visualstudio.com/Docs/editor/debugging

    F5 pour lancer le débogage 
    Une liste déroulante va s’afficher (environnement d’exécution de votre application). 
    Select .NET Core
    Le dossier .vscode sera créé avec les fichiers 

    CMD+SHIFT+D         Debug
    F5              continue
    F10             step over
    F11             step into
    SHIFT+F11       step out
    SHIFT+F5        stop



# .NET Core 

* Install VSCode

* In VSCode Extensions, install 'C#'' for Visual Studio Code (configurer-visual-studio-code-deboguer-application-asp-net-core/)

* Le framework .NET Core et les outils .NET Core doivent être également installés sur votre poste
  Install .Net Core SDK from the web to compile code: https://www.microsoft.com/net/download/core  
  CTRL-SHIFT-P (Palette) →  Download .NET Core Debugger  

* Créer un  projet de démarrage
    cmd.exe (ouvrez l’invite de commande dans le dossier où le projet doit être créé)
    dotnet new web -n testapp
    cd testapp
    dotnet restore    restauration des packages

    Configuration du débogage avec Visual Studio Code
    Ouvrez ensuite le projet avec Visual studio Code. 
    F5 pour lancer le débogage 
    Une liste déroulante va s’afficher (environnement d’exécution de votre application). 
    Select .NET Core
    Le dossier .vscode sera créé avec les fichiers 

    launch.json
        paramètres de configuration qui seront utilisés par Visual Studio Code pour lancer le programme qui s’occupe de la génération (msbuild) 
        les configurations pour lancer une application console et une application Web .NET Core. 

    VOUS ALLEZ SUPPRIMER LA CONFIGURATION POUR LANCER UNE APPLICATION CONSOLE.

    https://code.visualstudio.com/docs/editor/tasks
    Task.json

        autres tâches 

        {
            // See https://go.microsoft.com/fwlink/?LinkId=733558
            // for the documentation about the tasks.json format
            "version": "0.1.0",
            "command": "dotnet",
            "isShellCommand": true,
            "args": [],
            "tasks": [
                {
                    "taskName": "build",                                       //  argument le chemin vers le fichier .csproj à la tâche de build de votre projet
                    "args": [],                                                "args": ["${workspaceRoot}\\testapp.csproj"],   
                    "isBuildCommand": true,
                    "showOutput": "silent",
                    "problemMatcher": "$msCompile"
                }
            ]
        }




## SAMPLE (BUILD + DEBUG)        

        dotnet new -all
        dotnet new console -o projname
        dotnet new console      take current folder name for xxx.csproj
            Program.cs
            temp.csproj
        open folder
            .vscode

                * Add launch.json
                    {
                       // Use IntelliSense to find out which attributes exist for C# debugging
                       // Use hover for the description of the existing attributes
                       // For further information visit https://github.com/OmniSharp/omnisharp-vscode/blob/master/debugger-launchjson.md
                       "version": "0.2.0",
                       "configurations": [
                            {
                                "name": ".NET Core Launch (console)",
                                "type": "coreclr",
                                "request": "launch",
                                "preLaunchTask": "build",
                                // If you have changed target frameworks, make sure to update the program path.
                                "program": "${workspaceFolder}/bin/Debug/netcoreapp2.1/temp.dll",
                                "args": [],
                                "cwd": "${workspaceFolder}",
                                // For more information about the 'console' field, see https://github.com/OmniSharp/omnisharp-vscode/blob/master/debugger-launchjson.md#console-terminal-window
                                "console": "internalConsole",
                                "stopAtEntry": false,
                                "internalConsoleOptions": "openOnSessionStart"
                            },
                            {
                                "name": ".NET Core Attach",
                                "type": "coreclr",
                                "request": "attach",
                                "processId": "${command:pickProcess}"
                            }
                        ,]
                    }

                * Add tasks.json
                    {
                        "version": "2.0.0",
                        "tasks": [
                            {
                                "label": "build",
                                "command": "dotnet",
                                "type": "process",
                                "args": [
                                    "build",
                                    "${workspaceFolder}/temp.csproj"
                                ],
                                "problemMatcher": "$msCompile"
                            }
                        ]
                    }
        F5
        Debug with 


* Debug a node app:

        https://github.com/docker/labs/blob/master/developer-tools/nodejs-debugging/VSCode-README.md

        Left sidebar → 'Bug icon' → Click 
        Click debug → select environment: Node.js
        json file
        {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Attach",
                    "type": "node",
                    "request": "attach",
                    "port": 5858,
                    "address": "localhost",
                    "restart": true,
                    "sourceMaps": false,
                    "outDir": null,
                    "localRoot": "${workspaceRoot}",
                    "remoteRoot": "/code"
                }
            ]
        }

* Debug a .js file:
 
    If needed, start LiveServer

    Put a breakpoint (red dot)
    F5
    Choose "Launch Chrome against localhost"
        ↓
    This creates
        .vscode/lauch.json
                {                    
                    "version": "0.2.0",
                    "configurations": [
                        {
                            "type": "chrome",
                            "request": "launch",
                            "name": "Launch Chrome against localhost",
        check the port →    "url": "http://localhost:5500",
                            "webRoot": "${workspaceFolder}"
                        }
                    ]
                }
    F5 or Click |> button at top left "Launch Chrome against localhost"


    VSCode! nodejs-debugging
        https://github.com/docker/labs/blob/master/developer-tools/nodejs-debugging/VSCode-README.md
        app/.vscode/launch.json
        {
            "version": "0.2.0",
            "configurations": [
            {
                "name": "Attach",
                "type": "node",
                "request": "attach",
                "port": 5858,
                "address": "localhost",
                "restart": true,
                "sourceMaps": false,
                "outFiles": [],
                "localRoot": "${workspaceRoot}/",
                "remoteRoot": "/code"
                }
            ]
        }
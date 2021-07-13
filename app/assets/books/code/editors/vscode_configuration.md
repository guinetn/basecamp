# SETTINGS

* MACHINE LEVEL
C:\Users\nguin\AppData\Roaming\Code\User\settings.json
```json
"workbench.colorCustomizations": {
    "statusBar.background": "#000",
    "panel.background": "#000",
    ...        
    "tab.activeForeground": "#e0d03e",
    "tab.inactiveForeground": "#ada8a8",
    "activityBar.activeBackground": "#ff00ff50"
```

* PROJECT'S LEVEL
    .vscode\settings.json        Workspace Settings
    .vscode\tasks.json
    .vscode\launch.json
    .gitignore
        .vscode/

- USER SETTINGS 
    Preferences > User Settings    "files.exclude": {"node_modules/": true }
    Applied globally to any instance of VS 
    To hide all files that start with ._ such as ._.DS_Store files     "files.exclude": {"**/._*": true }

- WORKSPACE SETTINGS 
    Preferences > Workspace Settings
    Workspace settings will create a .vscode/settings.json file in your current workspace and will only be applied to that workspace.            



# show/hide certain files from the sidebar 
    You can configure patterns to hide files and folders from the explorer and searches. Open VS User Settings (Preferences > User Settings). This will open two side-by-side documents. 
    
    Add a new "files.exclude": {...} setting to the User Settings 
     "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/obj": true,
        "**/bin": true,
        "**/*.csproj": true
    }    


### VSCode Extensions

- https://github.com/Microsoft/vscode/tree/main/extensions

- https://marketplace.visualstudio.com/items?itemName=Oracle.oracledevtools
- https://code.visualstudio.com/api/extension-guides/webview
- https://github.com/microsoft/codetour: record and playback guided tours of codebases, directly within the editor.
- https://code.visualstudio.com/docs/remote/remote-overview
- https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp
- https://marketplace.visualstudio.com/items?itemName=mushan.vscode-paste-image

[ESLint] - Use ESLint with VS Code workspace.(https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

[GitLens] - A nicer version of git blame, quickly see with just a glance who wrote what and when.(https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

[TODO Highlight - Highights TODO and FIXME](https://marketplace.visualstudio.com/items?itemName=wayou.vscode-todo-highlight)
[Import Cost - Instantly see the size of the modules you're importing.](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost)
[Prettier - - VS Code implementation of opinionated code formatter. Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
[open in - Open selected file with default or alternative browser from context menu. browser](https://marketplace.visualstudio.com/items?itemName=techer.open-in-browser)
[vscode-styled - Syntax highlighting within styled-components template literals.-components](https://marketplace.visualstudio.com/items?itemName=jpoissonnier.vscode-styled-components)
[VSCode Great - Adds a bunch of great file icons (100+) to VS Code Icons](https://marketplace.visualstudio.com/items?itemName=emmanuelbeziat.vscode-great-icons)
[Bookmarks] - Add a bookmark to a line of code to quickly jump to it.(https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)
[One Monokai - VS Code custom them inspired by Monokai and One Dark. Theme](https://marketplace.visualstudio.com/items?itemName=azemoh.one-monokai)
[bracket-pair-colorizer](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer)


Ex: https://marketplace.visualstudio.com/items?itemName=rfukuma.background-image  
Download it → rfukuma.background-image-1.0.0.vsix  
Is a ".zip" file  
Rename to .zip to view inside
- extension.vsixmanifest
- [Content_Types].xml
- extension  
-> README.md  
-> package.json  
-> CHANGELOG.md  
-> out/  
    . main.js   
    . config.js  
    . ...


### VSCode Extensions: CREATE

- https://www.red-gate.com/simple-talk/dotnet/net-development/writing-vs-code-extensions-typescript
- https://blog.soat.fr/2020/04/vscode-creer-ses-propres-extensions/
- [EXTENSIONS](https://marketplace.visualstudio.com/VSCode)

    $npm install -g yo generator-code
    $yo code
             _-----_     ╭──────────────────────────╮
            |       |    │   Welcome to the Visual  │
            |--(o)--|    │   Studio Code Extension  │
           `---------´   │        generator!        │
            ( _´U`_ )    ╰──────────────────────────╯
            /___A___\   /
             |  ~  |
           __'.___.'__
         ´   `  |° ´ Y `

        ? What type of extension do you want to create? (Use arrow keys)
        > New Extension (TypeScript)
          New Extension (JavaScript)
          New Color Theme
          New Language Support
          New Code Snippets
          New Keymap
          New Extension Pack
          New Language Pack (Localization)
    cd helloWorld
    code .
    F5
    A new window VS Code is opened: "Extension Development Host"
    Exécution de la commande: Ctrl + Shift + P et lancez la commande "Hello World"
    package.json update:
        "commands": [
            {
                "command": "extension.sayHello",
                "title": "Say Good Evening"
            }
        ]
    extension.ts update:
        // Display a message box to the user
        vscode.window.showInformationMessage('Good Evening !');
    F5 pour lancer l’extension et lancez la commande "Say Good Evening".

    package.json

        activation events:  déclenchée par un événement ou un contexte particulier.

            onLanguage:${language}
            onCommand:${command}
            onDebug
            workspaceContains:${toplevelfilename}
            onFileSystem:${scheme}
            onView:${viewId}
            onUri
            onWebviewPanel:${viewType}

    extension.ts

        déclenchée via des commandes spécifiques qui seront appelées, soit par l’utilisateur, soit par d’autres extensions.
        Elles sont ensuite déclarées via un binding ou liaison dans le fichier package.json.

# IA


- https://marketplace.visualstudio.com/items?itemName=TabNine.tabnine-vscode
all-language autocomplete, use machine learning to help you write code faster.

- https://marketplace.visualstudio.com/items?itemName=ms-toolsai.vscode-ai
Azure Machine Learning for Visual Studio Code extension you can easily build, train, and deploy machine learning models to the cloud or the edge with Azure Machine Learning service from the Visual Studio Code interface. Earlier versions of this extension were released under the name Visual Studio Code Tools for AI.

With Azure Machine Learning service, you can:

Build and train machine learning models faster, and easily deploy to the cloud or the edge.
Use the latest open source technologies such as TensorFlow, PyTorch, or Jupyter.
Experiment locally and then quickly scale up or out with large GPU-enabled clusters in the cloud.
Speed up data science with automated machine learning and hyper-parameter tuning.
Track your experiments, manage models, and easily deploy with integrated CI/CD tooling.


### VS Code themes
- https://themes.vscode.one/


### keymaps 
CTRL+SHIFT+P → keymaps
CTRL-K-M 

## SNIPPETS

C:\Users\nguin\AppData\Roaming\Code\User\snippets

c.json
```conf
{
	// Place your snippets for c here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
}
```

Menu → File → Preferences -> User Snippets

    specify the scope of this configuration in the configuration file
    All we need to do is add the field "scope": "html"            

    {
     "html5 autocomplete": {
      "prefix": "html5",                ← Shortcut command we define
      "body": [                         ← When we type 'html5' in a file, VSCode automatically insert the code
       "<!DOCTYPE html>",
          "<html lang=\"en\">",
          "<head>",
          "  <title>$0</title>",    // After completion, the cursor will automatically stay at $0.
          "</head>",
          "<body>",
          "</body>",
          "</html>"
      ]
     }
    }

    {
     "for-i loop": {
        "prefix": "fori",
        "scope": "javascript, typescript",
        "body": [
          "for(let i = 0; i < $0; i++){",
          "}"
        ]
     }
    }



## MISC

upper/lower case:   Ctrl + shift + p    type >'transform' and pick upper/lower case and press enter

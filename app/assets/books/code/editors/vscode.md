# VSCode

- https://code.visualstudio.com
- https://code.visualstudio.com/docs      Docs
- https://github.com/microsoft/vscode     Source

- Microsoft open source Code Editor for Windows, Linux, macOS
- Powerful Edition: (multi-curseur, refactoring, parameters, navigation...)
- Light Visual Studio running applications in the background independently from the IDE (so it doesn't slow down)
- Supports C++, C#, Java, Python, TypeScript…
- Source Control (Git, Devops)
- Can run and deploy on Azure / Docker
- Debugging tools (breakpoints, terminal)
- Intellisense : Code-completion intelligente (variables, méthodes, modules)
- Set up the IDE for any type of project
    >tasks.json: build instructions, tell VSCode how to build (compile) a program
    >launch.json: debugger settings
- Starting VS Code in a folder 
    → that folder becomes your "workspace"
    → that workspace settings are in .vscode/settings.json (separate from user settings stored globally)
- Electron app  https://electron.atom.io/
http://www.dotnetcurry.com/visualstudio/1340/visual-studio-code-tutorial


download_page(code/editors/vscode_configuration.md)
download_page(code/editors/vscode_tasks.md)
download_page(code/editors/vscode_launch.md)
download_page(code/editors/vscode_remote.md)

## Productivity tips

https://www.youtube.com/watch?v=ifTF3ags0XI

* RELEASE THE MOUSE
    Check shortcuts

* ZOOM
    CTRL + +
    CTRL + -

* Pane Show/Hide

    CTRL+B


* VS CODE CLI

    code .                                              # open current folder in a new Visual Studio Code window
    code . -reuse                                       # open current folder in existing Visual Studio Code window
    code file.js                                        # open file
    code readme.md .gitignore package.json              # open the listed files in a new Visual Studio Code window
    code project1 project2                              # open the listed folders, each one in its own VSCode window

* REGEX    
    use $1 to replace
    Find       (zaa.*jpg)
    Replace    .pimg1{   background-image:url('../img/$1');   min-height:100%; }

* COMMAND PALETTE

    release the mouse → shortcut
    CTRL+P              show files
    CTRL+SHIFT+P        command palette
        │
		└───  Add '>' to show commands
		└───  Add '@' to show code symbols to quickly navigate to
		└───  Add '#' to find words with the first char you type

* MOVE AROUND QUICKLY
>:23
Hightlight: Shift + ←/→ 
Hightlight: Ctrl + ←/→      by words

* MULTILINE EDITING
Find matches: CTRL + D
Set multiple cursors: Alt + click    or    ALT + SHIFT + ↑ / ↓ 

* AUTO RENAME TAG
Extension to rename tag start/end

* DELETE OR MOVE A LINE
Alt + X 
Alt + ↑ / ↓         Move a line up and down

* HIGHLIGHT & COMMENT LINES
Highlight line: CTRL + L
Comment Lines: CTRL + /

* JS DOC EXTENSION

* BETTER COMMENTS

* INTEGRATED TERMINAL

CTRL + ù
CTRL + `
- powershell
- bash
- cmd
- node
- python

SETTINGS - Change Default Terminal

- Right click a terminal to change its color, icon, rename
- CTRL+P >terminal: Select Default Profile
- File -> Preferences -> Settings
  "terminal.integrated.shell.windows": "C:\\WINDOWS\\System32\\bash.exe"`
  
- File -> Preferences -> Keyboard Shortcuts
    //with this you can select what type of console you want
    {
        "key": "ctrl+shift+t",
        "command": "shellLauncher.launch"
    },

    //and this will help you quickly change console
    { 
        "key": "ctrl+shift+j", 
        "command": "workbench.action.terminal.focusNext" 
    },
    {
        "key": "ctrl+shift+k", 
        "command": "workbench.action.terminal.focusPrevious" 
    }`

[Add a terminal](https://code.visualstudio.com/docs/editor/integrated-terminal#_configuration)
    C:\WINDOWS\System32\cmd.exe     default
    C:\WINDOWS\System32\bash.exe    bash

    Left Menu Bottom → Settings (gear) → type 'Terminal'
        "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe"
        "terminal.integrated.shell.windows": "C:\\Program Files\\Git\\git-cmd.exe", "terminal.integrated.shellArgs.windows": ["--command=usr/bin/bash.exe", "-l", "-i"]

* VS CODE TASKS
json configuration files having command to run in the terminal or from command palette (>run)

* GIT SOURCE CONTROL
https://www.sqlservercentral.com/articles/basic-git-for-dbas-managing-powershell-scripts

* GIT LENS EXTENSION

* REMOTE REPOSITORIES
Normally to work on a repo on github you need to clone it to your local system
Install the extension then click the bottom left corner to open up a remote repo (log in)

* REMOTE SSH & CONTAINERS
Open any folder or repository inside a Docker container and take advantage of Visual Studio Code's. Deveop in containers instead of your local system

* CUSTOM SNIPPETS
your own or...
flutter snippet extensions

* COMMUNITY SNIPPETS

* AUTO-CREATE DIRECTORIES

* PASTE AS JSON EXTENSION
infer type with quicktype tool

* RENAME SYMBOL

                ___ F2 / Right-Click → 'Rename Symbol' function
               / 
    function foo(){
      // ...
    }
    foo();
    foo();
    foo();

CODE FOLDING
Ctrl+Shift+[ to fold
Ctrl+Shift+] to unfold from the current cursor position

Ctrl+K Ctrl+0 to fold
Ctrl+K Ctrl+J to unfold all sections

 Ctrl+K Ctrl+1 → Ctrl+K Ctrl+5 for indentation folding

Errors and warnings
F8 to sequentially navigate across underlines errors and view the detailed error message

JavaScript type checking
Visual Studio Code has a strong pull towards JavaScript and TypeScript.
//@ts-check comment on top of the file will run a TypeScript type checker 

apply the type check to the complete workspace by using the “javascript.implicitProjectConfig.checkJs” : true to the complete workspace and using //@ts-nocheckor //ts-expect-errorto individual files or lines.

Advice: Keyboard Over Mouse

Don't Use the Sidebar in VS Code
https://www.youtube.com/watch?v=s3H6PmB4SZ4
CTRL+W      Close file
CTRL+P      ...type filename
CTRL+TAB    switch between files
Extension advanced new file → ctrl+p then 'advanced..." then paths propositions



# COMPARE FILES

    http://dailydotnettips.com/2015/06/04/how-to-compare-files-in-visual-studio-code/
    Right click, Select for Compare” from the context menu.
    Right click, in the context menu, “Compare with <Previously Selected File for Compare>”
# Editing Text

    The Monaco Editor is the code editor that powers VS Code. 
    https://microsoft.github.io/monaco-editor/
    npm install monaco-editor@0.8.3

    Bracket matching (Ctrl+Shift+\)
    Code block commenting (Ctrl+K Ctrl+C) and uncommenting (Ctrl+K Ctrl+U)
    Smart selection growing (Shift+Alt+right) and shrinking (Shift+Alt+left)
    Code folding (Ctrl+Shift+[) and unfolding (Ctrl+Shift+]), including folding the full file to a specific level (Ctrl+K Ctrl+0 to Ctrl+K Ctrl+5) and unfolding the full file (Ctrl+K Ctrl+J)
    Zooming the editor in (Ctrl++) and out (Ctrl+-)
    Find (Ctrl+F in file, Ctrl+Shift+F in workspace) and replace (Ctrl+H in file, Ctrl+Shift+H in workspace) with regular expression support (including referencing matched groups with $1, $2… when replacing) and filtering files by filename when searching in workspace (Ctrl+Shift+J when Search side bar is opened)
    Multi cursor editing with block selection (Ctrl+Shift+Alt+cursor or Shift+Alt+click), custom adding of cursors (Alt+click) and adding find results to selection (Ctrl+D)
    For programming languages with language server support (built-in or extension-based), there are additional functionalities:

    IntelliSense code suggestions (automatically as you type and manually invoked with Ctrl+Space)
    Method parameter hints (automatically when you open parenthesis and manually invoked with Ctrl+Shift+Space)
    Go to symbol definition (F12, opens a new file or moves cursor in same file) and peek symbol definition (Alt+F12, opens inline view with full editing support, Esc closes it)
    Find all references (Shift+F12 opens inline view with full editing support, Esc closes it)
    Rename symbol (F2)
    Code formatting (Shift+Alt+F to format the full file, Ctrl+K Ctrl+F to format the current selection only)



## VSCODE INTERACTIVE

It is recommended to create separate environment for each project to avoid version conflicts and keep packages for each project separate. You have to activate the virtual environment that has packages installed. Initial environment in conda is named 'base'. 

Using windows powershell as your terminal run these commands to activate your conda environment.
>conda init powershell
>activate base
>activate <YOUR_ENVIRONMENT_NAME>

Using bash in windows environment
>conda init bash
>source activate <YOUR_ENVIRONMENT_NAME>

To execute imported modules in Jupyter notebook in VSCode, we need to install them in the selected environment (upper right corner of Jupyter).

>conda list | find "matplotlib"
>conda search <package>
>conda --info

## Notebook
- https://code.visualstudio.com/docs/datascience/jupyter-notebooks

## Python Interactive window
- https://code.visualstudio.com/docs/python/jupyter-support-py

To work with Jupyter notebooks, you must activate an Anaconda environment in VS Code, or another Python environment in which you've installed the Jupyter package. To select an environment, use the Python: Select Interpreter command from the Command Palette (Ctrl+Shift+P).
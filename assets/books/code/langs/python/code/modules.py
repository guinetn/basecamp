# Modules
A module is a file consisting of Python code. 
Any Python file can be referenced as a module, for example: file_name.py, is called a module, and its name would be file_name

#
to use the functionality present in any module, you have to import it. When Python interpreter comes across a import statement, it imports the module to your current program. You can use the functions inside a module by using a dot(.) operator along with the module name.
import configparser
import sqlite3
import requests

# from Statement
In some cases, you might not want to import all functions which are part of your module. You may be looking for specific functions. In that case from statment comes to rescue.
from flask import Flask, render_template, request
from werkzeug.exceptions import abort
from config import Config
from calculation import *
Importing a module increases the execution time of programs.


# __init__.py
The __init__.py file makes Python treat directories containing it as modules. 
This file is used to mark the directory on disk as Python package directories.

app/mod1/__init__.py
app/mod1/appmodule.py
import mod1.appmodule
---- or -----
from mod1 import appmodule
Python 3.3+ has Implicit Namespace Packages that allow it to create packages without an __init__.py file.
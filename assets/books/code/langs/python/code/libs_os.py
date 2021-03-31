import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH')) # Added PYTHONPATH in "Env Var system"
print("PATH:", os.environ.get('PATH'))

import os
print(os.getcwd())

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
# Environnements virtuels

	concept of creating environments so as to isolate different libraries and versions

	outil pour garder les dépendances requises par différents projets dans des emplacements séparés, en créant des environnements 
	virtuels Python pour eux. 
	Il résout le dilemme “le projet X dépend de la version 1.x mais le projet Y nécessite la 4.x”, et garde votre répertoire 
	site-packages global propre et gérable.

	http://pypi.python.org/pypi/virtualenv
	https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html

# virtualenv crée un dossier qui contient tous les exécutables nécessaires pour utiliser les paquets qu’un projet Python pourrait nécessiter.

	1. Install virtualenv
	$ pip install virtualenv

	2. Créer un environnement virtuel pour un projet:
	$ md my_project_folder
	$ cd my_project_folder
	$ virtualenv venv

	Supprimer une environnement virtuel
		supprimez juste son dossier
		rm -rf venv

# virtualenvwrapper
	
	jeu de commandes qui permet le travail avec des environnements virtuels beaucoup plus agréable
	Il place également tous vos environnements virtuels dans un seul endroit.

	$ pip install virtualenvwrapper
	$ export WORKON_HOME=~/Envs
	$ source /usr/local/bin/virtualenvwrapper.sh


https://medium.com/pankajmathur/what-is-anaconda-and-why-should-i-bother-about-it-4744915bf3e6	



python3 -m venv env   # Creating virtual environment in Mac/Linux
py -m venv env        # Creating virtual environment in Windows
# Projet 4 OpenClassrooms - Développez un programme logiciel en Python

## Présentation du projet 
Application permettant la gestion de tournoi d'échecs avec plusieurs fonctionnalités comme :
- la création de joueurs
- la création de tournois
- la génération de rapport 

## Menu
 -- Menu navigation --

1. Menu joueur
- 1.1 Créer un joueur
- 1.2 Afficher tous les joueurs
- 1.3 Supprimer un joueur
- 1.4 Quitter le menu joueur
2. Menu tournoi
- 2.1 Ajouter un tournoi
- 2.2 Voir la liste des tournois
- 2.3 Commencer un tournoi
- 2.4 Supprimer un tournoi
- 2.5 Quitter le menu tournoi
3. Menu rapport
- 3.1 Liste des joueurs
- 3.2 Liste des tournois
- 3.3 Info et date d'un tournoi
- 3.4 Liste des joueurs d'un tournoi
- 3.5 Rapport d'un tournoi
- 3.6 Quitte le menu rapport

## Mise en place du projet 
Pour ce projet, vous avez besoin d'avoir Python :snake: d'installer sur votre ordinateur.
Vous pouvez le télécharger depuis le [site officiel de Python](https://www.python.org/) .

### Telecharger le repo
Créez un nouveau dossier sur votre bureau avec le nom que vous souhaitez
 	
 - Télécharger le fichier zip du projet ou clonez le avec le lien suivant :
  
``` 
[https://github.com/nefalis/projet-4-chess-tournament.git]
``` 

- Accédez au répertoire du script 
``` 
cd projet-4-chess-tournament
 ```

### Packages

 si vous avez python 3.x, il est recommandé d'utiliser pip3 pour éviter toute confusion avec les installations de Python 2.x qui utilisent simplement pip

Installer les modules nécessaires :
``` 
pip3 -r requirements.txt
 ```
### Création de l'environnement virtuel
``` 
python -m venv env
 ```
### Installation de la librairie Rich
Permet de mettre des couleurs dans le terminal et de faire les tableaux des rapports
``` 
pip install rich
 ```

### Exécution
Veuillez exécuter le fichier `main.py` avec la commande suivante :
``` 
python main.py
```

## Génération rapport Flake8

### Installation de Flake8

``` 
pip intall flake8-html
 ```

 ### Génération du dossier contenant le rapport
Le rapport sera généré dans le dossier Flake8

``` 
flake8 --format=html --htmldir=flake-report
 ```



## Auteur
Charron Emilie

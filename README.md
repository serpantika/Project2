# Comment créer un environnement virtuel (Powershell, Windows)
## - prérequis :
* PowerShell
* Python (3.3 minimum)

## - Installation de Virtualenv
En premier, il vous faut ouvrir Powershell. Vous aurez besoin d'avoir PIP à jour. Pour s'en assurer vous pouvez vérifier sa version avec :  
> py -m pip --version  

Pour mettre à jour pip :  
>py -m pip install --upgrade pip

Une fois pip à jour, nous pouvons maintenant installer virtualenv qui nous servira à créer notre environnement virtuel
en utilisant :
>py -m pip install --user virtualenv  
 
(***pour MacOS et Linux remplacer py par python3***)
## - Création de l'environnement virtuel

Choisir l'emplacement où vous voulez créer votre environnement virtuel grace à la commande **cd** plus le chemin
de destination. Puis entrez la commande suivante, vous pouvez changer env par le 
nom que vous voulez donner à votre dossier.  
>py -m venv env

Pour lancer l'environnement:
>.\env\Scripts\activate  
 
(***Pour MacOS et Linux :***)
>source env/bin/activate

Pour éteindre l'environnement:
>deactivate

## - Lancement du programme  
* télécharger en format ZIP sur Github le projet 2 puis le dézipper à l'endroit souhaité
  

* après ouverture de l'environnement spécifié le chemin d'accès du projet sur powershell  
  


* installer les paquets python nécessaire au programme dans l'environnement virtuel :
>pip install -r requirements.txt

* lancer le programme avec:
>py main.py








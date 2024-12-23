# Gestion d'Inventaire Automatisée

## Description
Ce projet propose une solution en ligne de commande pour gérer un inventaire à partir de fichiers CSV. Il permet d'importer et de fusionner des données, d'effectuer des recherches, et de générer des rapports.

## Fonctionnalités
- Importation et fusion automatique des fichiers CSV.
- Recherche par nom, catégorie, et prix.
- Génération de statistiques globales et de graphiques.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone <votre-lien-depot>

2. Installer les dépendances pandas et matplotlib: 
pip install pandas matplotlib FPDF

3. Lancer le programme :
python main.py

4. Executez les tests unitaires avec :
python -m unittest discover src/tests


## Commandes exemple argparse:

python mainArgparse.py --importer <chemin_du_dossier>
python mainArgparse.py --importer ./data

python mainArgparse.py --rechercher <nom> <categorie> <prix_min> <prix_max>
python mainArgparse.py --rechercher "nom_produit" "categorie" 10 50

python mainArgparse.py --rapport <chemin_graphique> <chemin_pdf>
python mainArgparse.py --rapport "graphique" "rapport"


## User Stories:

## Importer et consolider les fichiers CSV

En tant qu'utilisateur,
Je souhaite importer plusieurs fichiers CSV représentant différentes catégories ou départements,
Afin de fusionner les données en une base unique et centralisée, facilitant leur consultation et leur traitement.

Valeur pour le client
Permettre à l'utilisateur de regrouper automatiquement des informations provenant de différentes sources dans un format cohérent, réduisant ainsi les efforts manuels et le risque d'erreurs.

Description
Une fonctionnalité d'importation permettra à l'utilisateur de :

Sélectionner plusieurs fichiers CSV à partir de leur ordinateur.
Fusionner les données dans une base centralisée tout en éliminant les doublons.
Afficher un résumé des données consolidées pour validation.



## Rechercher des informations sur les produits

En tant qu'utilisateur,
Je souhaite rechercher des produits par nom, catégorie ou plage de prix,
Afin de localiser rapidement des informations spécifiques sans devoir parcourir manuellement toute la base de données.

Valeur pour le client
Offrir une méthode rapide et efficace pour accéder à des données clés, réduisant le temps passé à chercher des informations et améliorant la réactivité face aux besoins.

Description
Un champ de recherche avancé sera disponible avec des filtres permettant :

De rechercher un produit par son nom ou mots-clés.
De filtrer les résultats par catégorie.
De définir une plage de prix pour les produits affichés.
Les résultats seront affichés dans une liste détaillée.



## Générer des rapports récapitulatifs

En tant qu'utilisateur,
Je souhaite générer un rapport PDF contenant des statistiques et des graphiques illustrant la répartition des produits par catégorie,
Afin d’avoir une vue d’ensemble exportable et claire de mes stocks, utile pour la gestion et la communication.

Valeur pour le client
Faciliter l'accès à des données consolidées et prêtes à partager, tout en améliorant la prise de décision grâce à des rapports visuels et informatifs.

Description
Une fonction de génération de rapports inclura :

Des statistiques clés comme le total des produits en stock et la valeur de l'inventaire.
Un graphique visuel montrant la répartition des produits par catégorie.
La possibilité d'exporter le rapport sous forme de fichier PDF, prêt à être imprimé ou partagé avec les parties prenantes.



## Créer un graphique illustrant les données

En tant qu'utilisateur,
Je souhaite créer un graphique montrant la quantité de produits par catégorie,
Afin de visualiser les données d'une manière claire et intuitive, facilitant l'analyse et la communication.

Valeur pour le client
Offrir une représentation visuelle des données qui simplifie l'analyse et met en évidence des tendances ou déséquilibres éventuels dans les stocks.

Description
Un générateur de graphique permettra :

De sélectionner les catégories et données à inclure dans le graphique.
De visualiser la répartition des quantités sous forme de diagramme en barres ou en secteurs.

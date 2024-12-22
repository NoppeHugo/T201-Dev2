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


##Commandes exemple argparse:

python mainArgparse.py --importer <chemin_du_dossier>
python mainArgparse.py --importer ./data

python mainArgparse.py --rechercher <nom> <categorie> <prix_min> <prix_max>
python mainArgparse.py --rechercher "nom_produit" "categorie" 10 50

python mainArgparse.py --rapport <chemin_graphique> <chemin_pdf>
python mainArgparse.py --rapport "graphique" "rapport"


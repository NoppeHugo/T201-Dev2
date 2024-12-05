# **Comment utiliser l'application**

Lors du lancement de l'application, vous serez présenté avec un menu interactif en ligne de commande. Voici les différentes options disponibles :

## **1. Importer et fusionner les fichiers CSV**
- Cette option permet d'importer tous les fichiers CSV présents dans le dossier `./data`.
- Les fichiers sont fusionnés en un seul tableau (DataFrame) pour une gestion centralisée.
- Exemple de colonnes attendues dans les fichiers CSV :
  - `Nom`
  - `Quantité`
  - `Prix Unitaire (€)`
  - `Catégorie`
- Si les fichiers sont importés avec succès, leurs colonnes seront affichées pour confirmation.

## **2. Rechercher un produit**
- Cette option permet de rechercher des produits spécifiques dans l'inventaire.
- Critères disponibles pour la recherche :
  - **Nom** : Entrez tout ou partie du nom du produit.
  - **Catégorie** : Spécifiez une catégorie (ex. "Électronique").
  - **Plage de prix** : Indiquez un prix minimum et/ou maximum.
- Les résultats de la recherche sont affichés sous forme de tableau.

## **3. Générer un rapport**
- Crée un rapport détaillé comprenant :
  - Les statistiques globales (valeur totale de l'inventaire, nombre total d'articles).
  - Un graphique illustrant la répartition des quantités par catégorie.
  - Les données originales exportées dans un fichier Excel.
- Le programme vous demandera d'entrer un chemin où sauvegarder le fichier (ex. `rapport.xlsx`).
- Le fichier Excel inclura :
  - Une feuille "Statistiques" avec les calculs globaux.
  - Une feuille "Données" contenant toutes les informations fusionnées.
  - Une feuille "Graphique" avec l'image générée.

## **4. Quitter**
- Cette option permet de quitter l'application proprement.

---

## **Structure des fichiers**
```plaintext
inventaire/
├── data/                       # Contient les fichiers CSV d'entrée
│   ├── produits_alimentaires.csv
│   ├── produits_electroniques.csv
├── src/                        # Contient le code source
│   ├── __init__.py
│   ├── importer.py             # Module pour importer les fichiers CSV
│   ├── rechercher.py           # Module pour effectuer des recherches
│   ├── rapport.py              # Module pour générer des rapports
│   └── tests/                  # Contient les tests unitaires
│       ├── test_importer.py
│       ├── test_rechercher.py
│       └── test_rapport.py
├── main.py                     # Point d'entrée principal du programme
├── README.md                   # Ce fichier
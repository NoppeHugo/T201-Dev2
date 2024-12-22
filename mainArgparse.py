import os
import pandas as pd
import argparse
from src.rapport import generer_statistiques, generer_graphique, generer_rapport_pdf, ajouter_extension_si_absente
from src.rechercher import rechercher_produit
from src.importer import importer_csv

def main(args):
    df = None

    if args.importer:
        dossier = args.importer
        if os.path.exists(dossier):
            df = importer_csv(dossier)
            print("Fichiers importés et fusionnés avec succès !")
            print("Colonnes du DataFrame:", df.columns)
        else:
            print("Le dossier spécifié n'existe pas.")

    if args.rechercher:
        if df is not None:
            nom, categorie, prix_min, prix_max = args.rechercher
            prix_min = float(prix_min) if prix_min else None
            prix_max = float(prix_max) if prix_max else None
            resultats = rechercher_produit(df, nom, categorie, prix_min, prix_max)
            print(resultats)
        else:
            print("Veuillez d'abord importer les fichiers CSV.")

    if args.rapport:
        if df is not None:
            chemin_graphique, chemin_pdf = args.rapport
            chemin_graphique = ajouter_extension_si_absente(chemin_graphique, ".png")
            chemin_pdf = ajouter_extension_si_absente(chemin_pdf, ".pdf")
            try:
                generer_graphique(df, chemin_graphique)
                generer_rapport_pdf(df, chemin_pdf, chemin_graphique)
                print(f"Rapport PDF généré : {os.path.abspath(chemin_pdf)}")
            except (ValueError, FileNotFoundError) as e:
                print(e)
        else:
            print("Veuillez d'abord importer les fichiers CSV.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gestion d'Inventaire")
    parser.add_argument('--importer', type=str, help="Dossier contenant les fichiers CSV à importer")
    parser.add_argument('--rechercher', nargs=4, metavar=('nom', 'categorie', 'prix_min', 'prix_max'), help="Rechercher un produit")
    parser.add_argument('--rapport', nargs=2, metavar=('chemin_graphique', 'chemin_pdf'), help="Générer un rapport PDF")
    args = parser.parse_args()
    main(args)
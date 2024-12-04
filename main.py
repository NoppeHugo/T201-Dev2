import os
from src.importer import importer_csv
from src.rechercher import rechercher_produit
from src.rapport import generer_statistiques, generer_graphique

def afficher_menu():
    print("""
    ===== Menu Gestion d'Inventaire =====
    1. Importer et fusionner les fichiers CSV
    2. Rechercher un produit
    3. Générer un rapport
    4. Quitter
    """)

def main():
    df = None

    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")

        if choix == "1":
            dossier = "./data"
            if os.path.exists(dossier):
                df = importer_csv(dossier)
                print("Fichiers importés et fusionnés avec succès !")
            else:
                print("Le dossier spécifié n'existe pas.")

        elif choix == "2":
            if df is not None:
                nom = input("Rechercher par nom (laisser vide pour ignorer) : ")
                categorie = input("Rechercher par catégorie (laisser vide pour ignorer) : ")
                prix_min = input("Prix minimum (laisser vide pour ignorer) : ")
                prix_max = input("Prix maximum (laisser vide pour ignorer) : ")

                prix_min = float(prix_min) if prix_min else None
                prix_max = float(prix_max) if prix_max else None

                resultats = rechercher_produit(df, nom, categorie, prix_min, prix_max)
                print("Résultats de la recherche :")
                print(resultats)
            else:
                print("Veuillez d'abord importer les fichiers CSV.")

        elif choix == "3":
            if df is not None:
                stats = generer_statistiques(df)
                print("Statistiques globales :")
                for k, v in stats.items():
                    print(f"{k}: {v}")
                chemin_graphique = input("Entrez le chemin pour sauvegarder le graphique (ex: graphique.png) : ")
                generer_graphique(df, chemin_graphique)
                print(f"Graphique sauvegardé sous {chemin_graphique}.")
            else:
                print("Veuillez d'abord importer les fichiers CSV.")

        elif choix == "4":
            print("Merci d'avoir utilisé la gestion d'inventaire. À bientôt !")
            break

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

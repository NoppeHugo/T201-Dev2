import os
import pandas as pd

def afficher_menu():
    print("""
    ===== Menu Gestion d'Inventaire =====
    1. Importer et fusionner les fichiers CSV
    2. Rechercher un produit
    3. Générer un rapport
    4. Quitter
    """)

def importer_csv(dossier):
    all_files = [os.path.join(dossier, f) for f in os.listdir(dossier) if f.endswith('.csv')]
    df_list = [pd.read_csv(file) for file in all_files]
    df = pd.concat(df_list, ignore_index=True)
    return df

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
                print("Colonnes du DataFrame:", df.columns)  # Debug print to check columns
            else:
                print("Le dossier spécifié n'existe pas.")
        elif choix == "2":
            if df is not None:
                nom = input("Entrez le nom du produit : ")
                categorie = input("Entrez la catégorie du produit : ")
                prix_min = float(input("Entrez le prix minimum : "))
                prix_max = float(input("Entrez le prix maximum : "))
                resultats = rechercher_produit(df, nom, categorie, prix_min, prix_max)
                print(resultats)
            else:
                print("Veuillez d'abord importer les fichiers CSV.")
        elif choix == "3":
            if df is not None:
                stats = generer_statistiques(df)
                print(stats)
            else:
                print("Veuillez d'abord importer les fichiers CSV.")
        elif choix == "4":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

def rechercher_produit(df, nom, categorie, prix_min, prix_max):
    filtre = pd.Series([True] * len(df))
    if nom:
        filtre &= df['Nom'].str.contains(nom, case=False, na=False)
    if categorie:
        filtre &= df['Catégorie'].str.contains(categorie, case=False, na=False)
    if prix_min is not None:
        filtre &= df['Prix Unitaire (€)'] >= prix_min
    if prix_max is not None:
        filtre &= df['Prix Unitaire (€)'] <= prix_max
    return df[filtre]

def generer_statistiques(df):
    valeur_totale = (df['Quantité'] * df['Prix Unitaire (€)']).sum()
    return f"Valeur totale de l'inventaire: {valeur_totale} €"

if __name__ == "__main__":
    main()
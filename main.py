import pandas as pd
import matplotlib.pyplot as plt

# Consolidation des fichiers CSV en une base unique

# Chemins des fichiers
files = ["electronique.csv", "alimentation.csv", "vetements.csv"]
base_path = ""

# Lecture et fusion des fichiers
dataframes = [pd.read_csv(base_path + file) for file in files]
df_consolidated = pd.concat(dataframes, ignore_index=True)

# Sauvegarde de la base consolidée
consolidated_file = base_path + "base_consolidee.csv"
df_consolidated.to_csv(consolidated_file, index=False)

df_consolidated

# Ajout de fonctionnalités de recherche rapide
# Fonction pour rechercher des produits par différents critères

def search_inventory(dataframe, criteria):
    """
    Recherche dans l'inventaire selon des critères donnés.
    
    Args:
        dataframe (pd.DataFrame): La base consolidée.
        criteria (dict): Dictionnaire contenant les filtres (colonne et valeur).
        
    Returns:
        pd.DataFrame: Résultats filtrés.
    """
    filtered_df = dataframe
    for column, value in criteria.items():
        if column in dataframe.columns:
            if isinstance(value, (int, float)):
                filtered_df = filtered_df[filtered_df[column] == value]
            elif isinstance(value, str):
                filtered_df = filtered_df[dataframe[column].str.contains(value, case=False)]
    return filtered_df


# Exemple d'utilisation : rechercher tous les produits de la catégorie "Électronique"
criteria_example = {"Catégorie": "Électronique"}
search_results = search_inventory(df_consolidated, criteria_example)
print(search_results)


# Génération de rapports
def generate_report(dataframe, output_path):
    """
    Génère un rapport récapitulatif de l'inventaire et l'exporte en CSV et en graphique.
    
    Args:
        dataframe (pd.DataFrame): La base consolidée.
        output_path (str): Chemin de sortie pour les fichiers générés.
        
    Returns:
        str: Message de confirmation.
    """
    # Calcul des statistiques globales
    total_value = (dataframe["Quantité"] * dataframe["Prix Unitaire (€)"]).sum()
    total_products = dataframe["Quantité"].sum()
    category_summary = dataframe.groupby("Catégorie").agg(
        Total_Produits=("Quantité", "sum"),
        Valeur_Totale=("Prix Unitaire (€)", lambda x: (x * dataframe["Quantité"]).sum())
    )

    # Sauvegarde du rapport en CSV
    report_csv_path = output_path + "rapport_inventaire.csv"
    category_summary.to_csv(report_csv_path)

    # Création d'un graphique des stocks par catégorie
    plt.figure(figsize=(8, 6))
    category_summary["Total_Produits"].plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Nombre de produits par catégorie", fontsize=14)
    plt.ylabel("Nombre total de produits")
    plt.xlabel("Catégorie")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Sauvegarde du graphique
    graph_path = output_path + "graphique_inventaire.png"
    plt.savefig(graph_path)
    plt.close()

    return f"Rapport généré avec succès ! CSV : {report_csv_path}, Graphique : {graph_path}"


# Génération du rapport
output_path = ""
report_message = generate_report(df_consolidated, output_path)
print(report_message)


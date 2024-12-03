import pandas as pd
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


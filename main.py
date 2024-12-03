# Consolidation des fichiers CSV en une base unique

# Chemins des fichiers
files = ["electronique.csv", "alimentation.csv", "vetements.csv"]
base_path = "/mnt/data/"

# Lecture et fusion des fichiers
dataframes = [pd.read_csv(base_path + file) for file in files]
df_consolidated = pd.concat(dataframes, ignore_index=True)

# Sauvegarde de la base consolidée
consolidated_file = base_path + "base_consolidee.csv"
df_consolidated.to_csv(consolidated_file, index=False)

df_consolidated

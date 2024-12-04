import pandas as pd
import os

def importer_csv(dossier: str) -> pd.DataFrame:
    fichiers = [os.path.join(dossier, f) for f in os.listdir(dossier) if f.endswith('.csv')]
    dataframes = [pd.read_csv(f) for f in fichiers]
    return pd.concat(dataframes, ignore_index=True)

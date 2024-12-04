import pandas as pd

def rechercher_produit(df: pd.DataFrame, nom: str = None, categorie: str = None, prix_min: float = None, prix_max: float = None) -> pd.DataFrame:
    filtre = pd.Series([True] * len(df))
    if nom:
        filtre &= df['Nom'].str.contains(nom, case=False, na=False)
    if categorie:
        filtre &= df['Catégorie'].str.contains(categorie, case=False, na=False)
    if prix_min is not None:
        filtre &= df['Prix'] >= prix_min
    if prix_max is not None:
        filtre &= df['Prix'] <= prix_max
    return df[filtre]

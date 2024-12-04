import pandas as pd
import matplotlib.pyplot as plt

def generer_statistiques(df: pd.DataFrame) -> dict:
    valeur_totale = (df['Quantité'] * df['Prix']).sum()
    articles_totaux = df['Quantité'].sum()
    return {"Valeur Totale": valeur_totale, "Articles Totaux": articles_totaux}

def generer_graphique(df: pd.DataFrame, chemin: str) -> None:
    stats = df.groupby('Catégorie')['Quantité'].sum()
    stats.plot(kind='bar', title='Quantité par Catégorie')
    plt.xlabel('Catégorie')
    plt.ylabel('Quantité')
    plt.savefig(chemin)
    plt.close()

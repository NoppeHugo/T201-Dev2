import pandas as pd
import matplotlib.pyplot as plt
from pandas import ExcelWriter
import os
from fpdf import FPDF

def generer_statistiques(df: pd.DataFrame) -> dict:
    valeur_totale = (df['Quantité'] * df['Prix Unitaire (€)']).sum()
    articles_totaux = df['Quantité'].sum()
    return {"Valeur Totale": valeur_totale, "Articles Totaux": articles_totaux}

def generer_graphique(df: pd.DataFrame, chemin: str) -> None:
    if not chemin.lower().endswith(('.png', '.jpg', '.jpeg')):
        raise ValueError("Le chemin de l'image doit avoir une extension valide (.png, .jpg, .jpeg)")
    
    stats = df.groupby('Catégorie')['Quantité'].sum()
    stats.plot(kind='bar', title='Quantité par Catégorie')
    plt.xlabel('Catégorie')
    plt.ylabel('Quantité')
    plt.savefig(chemin)
    plt.close()

def generer_rapport_pdf(df: pd.DataFrame, chemin_pdf: str, chemin_graphique: str) -> None:
    if not os.path.exists(chemin_graphique):
        raise FileNotFoundError(f"L'image spécifiée n'existe pas : {chemin_graphique}")
    
    pdf = FPDF()
    pdf.add_page()
    
    # Utilisation de la police Arial avec encodage UTF-8
    pdf.set_font("Arial", size=12)
    
    # Titre
    pdf.cell(200, 10, txt="Rapport d'Inventaire", ln=True, align='C')
    
    # Statistiques
    stats = generer_statistiques(df)
    pdf.set_font("Arial", size=10)
    for k, v in stats.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
    
    # Détails des articles
    pdf.set_font("Arial", size=8)
    for index, row in df.iterrows():
        pdf.cell(200, 10, txt=f"Article: {row['Nom']} | Catégorie: {row['Catégorie']} | Quantité: {row['Quantité']} | Prix Unitaire (€): {row['Prix Unitaire (€)']}", ln=True)
    
    # Graphique
    pdf.add_page()
    pdf.image(chemin_graphique, x=10, y=10, w=190)
    
    # Sauvegarde du PDF
    pdf.output(chemin_pdf)

def ajouter_extension_si_absente(nom_fichier, extension):
    if not nom_fichier.lower().endswith(extension):
        nom_fichier += extension
    return nom_fichier
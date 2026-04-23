import pandas as pd
import matplotlib.pyplot as plt

# Données d'exemple selon l'énoncé
donnees = {
    'ID': [101, 102, 103, 104, 105 ],
    'Prix': [15.0, 25.0, 10.0,50.0, 30.0],
    'Quantite': [3, 2, 5,1, 4],
    'Remise': [10, 5, 0, 15, 20]
}

# Création du DataFrame et export en CSV
df = pd.DataFrame(donnees)
df.to_csv('ventes.csv', index=False, sep=';', encoding='utf-8-sig')
print("Fichier ventes.csv généré avec succès.")
# Lecture du fichier
df_analyse = pd.read_csv('ventes.csv', sep=';')

# Calculs
df_analyse['CA Brut'] = df_analyse['Prix'] * df_analyse['Quantite']
df_analyse['CA Net'] = df_analyse['CA Brut'] * (1 - df_analyse['Remise'] / 100)
df_analyse['TVA'] = df_analyse['CA Net'] * 0.20
# CA Total de l'entreprise
ca_total = df_analyse['CA Net'].sum()
print(f"Le Chiffre d'Affaires Total est de : {ca_total} DT")

# Produit avec le plus gros bénéfice (basé sur le CA Net ici)
id_max = df_analyse.loc[df_analyse['CA Net'].idxmax(), 'ID']
print(f"Le produit ayant généré le plus gros bénéfice est l'ID : {id_max}")
# Utilise sep=';' pour que le fichier s'ouvre directement en colonnes dans Excel
df_analyse.to_csv('resultats_final.csv', index=False, sep=';', encoding='utf-8-sig')
print("Analyse terminée. Consultez 'resultats_final.csv'.")


colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Création d'une figure avec deux zones de dessin (1 ligne, 2 colonnes)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# --- GRAPHIQUE 1 : BAR CHART (Détails des montants) ---
bars = ax1.bar(df_analyse['ID'].astype(str), df_analyse['CA Net'], color=colors[:len(df_analyse)])
ax1.set_title('Chiffre d\'Affaires Net par Produit', fontsize=14, fontweight='bold')
ax1.set_ylabel('Montant en DT')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Ajout des étiquettes de données (CA Net + TVA)
for i, bar in enumerate(bars):
    height = bar.get_height()
    tva_val = df_analyse.iloc[i]['TVA']
    ax1.text(bar.get_x() + bar.get_width()/2, height, 
             f'CA: {height}DT\n(TVA: {tva_val}DT)', 
             ha='center', va='bottom', fontsize=9, fontweight='bold')

# --- GRAPHIQUE 2 : PIE CHART (Répartition en %) ---
ax2.pie(df_analyse['CA Net'], 
        labels=[f'Prod {id}' for id in df_analyse['ID']], 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors,
        explode=[0.05] * len(df_analyse), # Détache légèrement les parts
        shadow=True)
ax2.set_title('Répartition du CA Total (%)', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.show()
import sys
from collections import Counter
import re

def charger_texte(nom_fichier):
    """
✅ Fonction à compléter :
- Ouvrir le fichier en mode lecture (encoding='utf-8')
- Lire tout le contenu et le convertir en minuscules
- Utiliser une expression régulière pour extraire tous les mots (ex : \b\w+\b)
- Retourner une liste de mots

📌 En cas d'erreur (ex : fichier introuvable), afficher un message et quitter le programme avec sys.exit(1)
    """
    pass  # À remplacer par ton code

def afficher_mots_frequents(mots, top=10):
    """
✅ Fonction à compléter :
- Utiliser collections.Counter pour compter la fréquence de chaque mot
- Afficher les 'top' mots les plus fréquents avec leur nombre d'apparitions

📌 Utilise .most_common(top) pour trier
📌 Formate l'affichage pour que ce soit lisible (ex : f"{mot:>10} → {nb} fois")
    """
    pass  # À remplacer par ton code

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ Utilisation : python analyseur.py fichier.txt")
        sys.exit(1)

    fichier = sys.argv[1]
    mots = charger_texte(fichier)
    print(f"🔍 Analyse du fichier '{fichier}' :")
    afficher_mots_frequents(mots)


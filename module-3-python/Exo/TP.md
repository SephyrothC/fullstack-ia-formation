# 🧪 TP Final : Calculateur d'heures de travail avancé

## 🎯 Objectif

Créer un script Python interactif en ligne de commande qui permet :

- ✅ D’entrer une liste d'heures travaillées pour chaque jour de la semaine (via input ou via un fichier `.txt`)
- ✅ De définir un taux horaire
- ✅ De calculer :
  - Le total d’heures travaillées
  - Le salaire brut total
  - Le salaire après impôts (avec une déduction fixe ou en pourcentage)
  - Le jour le plus travaillé
- ✅ De gérer les cas d’erreurs :
  - Valeurs non numériques
  - Heures négatives
  - Plus de 24h/jour
- ✅ De sauvegarder un rapport (`rapport.txt`)

---

## 📋 Spécifications techniques

### 📥 Entrées :

- Liste d'heures par jour (7 jours, sous forme : `[8, 7.5, 6, 8, 5, 0, 0]`)
- Taux horaire (ex. 12.50 €/h)
- Taux de prélèvement (par défaut 20%, personnalisable)

### 📤 Sorties :

- Heures totales travaillées
- Salaire brut
- Salaire net
- Jour le plus travaillé
- Un fichier `rapport.txt` généré automatiquement

---

## 🧠 Contraintes

- Utiliser des **fonctions** pour séparer les étapes
- Gérer les **exceptions** (`try/except`) et la **validation des données**
- Ajouter au moins **un test unitaire** dans un fichier `test_calculateur.py` avec `assert`
- Organiser ton code avec `if __name__ == "__main__":`

---

## 📂 Livrables attendus

- `calculateur.py`
- `README.md` avec explications d’utilisation
- `rapport.txt` (exemple)
- `test_calculateur.py` avec au moins un test
- 1 ou 2 screenshots du script en exécution

---

## 🧪 Bonus possible

- Ajouter une option d’import des heures depuis un fichier `heures.txt`
- Ajouter une visualisation ASCII ou texte (barres d’heures par jour)
- Exporter le rapport au format `.csv`

---

## ✅ Exemple de rendu attendu (console)

```bash
Entrez les heures travaillées pour chaque jour (lundi à dimanche) :
> 8 8 7.5 6 5 0 0
Entrez le taux horaire :
> 13.5
Entrez le taux de prélèvement (en %) [20 par défaut] :
> 

--- Résultat ---
Total heures : 34.5
Salaire brut : 465.75 €
Salaire net (après 20%) : 372.60 €
Jour le plus chargé : lundi
Rapport sauvegardé dans "rapport.txt"

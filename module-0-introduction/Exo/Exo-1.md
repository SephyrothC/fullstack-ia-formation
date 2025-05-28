# 🧪 Exercice Guidé 01 – Ton premier projet Hello World (JS + Python)

## 🎯 Objectifs

- Créer un projet local structuré
- Lancer un script en Python
- Utiliser Git pour versionner ton travail
- Publier ton premier dépôt sur GitHub

---

## 🧰 Prérequis

Assure-toi d’avoir installé :

- VS Code
- Python 3
- Git
- Un compte GitHub (créé sur [github.com](https://github.com))

---

## 🔨 Étapes

### 🟢 1. Créer ton dossier de projet

Ouvre ton terminal et entre :

```bash
mkdir hello-world
cd hello-world
code .
```
Cela crée le dossier `hello-world` et l’ouvre dans VS Code.

---

### 📄 2. Créer les deux fichiers

Dans VS Code, crée deux fichiers :

- `hello.py`


**Contenu du fichier `hello.py` :**
```python
print("Hello World from Python!")
```

---

### ▶️ 3. Lancer les scripts

Dans le terminal intégré de VS Code :

```bash
python hello.py
```
Tu devrais voir les deux messages s’afficher dans la console.

---

### 🌐 4. Initialiser un dépôt Git local

Toujours dans le terminal :

```bash
git init
git add .
git commit -m "Mon premier projet Hello World en Python"
```

---

### 🚀 5. Publier sur GitHub

1. Crée un nouveau dépôt vide sur [github.com](https://github.com)
   - **Nom du dépôt :** `hello-world-python`
2. Associe-le à ton projet local :

```bash
git remote add origin https://github.com/<ton-pseudo>/hello-world-python.git
git branch -M main
git push -u origin main
```
Remplace `<ton-pseudo>` par ton pseudo GitHub.

---

## ✅ 6. Livrables à valider

| Livrable                | Description                                      |
|-------------------------|--------------------------------------------------|
| ✅ Script JS et Python  | Fichiers `hello.js` et `hello.py` créés et testés|
| ✅ Screenshot console   | Capture d’écran de l'exécution des deux scripts  |
| ✅ Dépôt GitHub en ligne| Contient le code + `README.md`                   |
| ✅ Commit clair         | Le message de commit reflète bien ton travail     |

---

## 🎁 Bonus : Ajoute un README.md

Ajoute un fichier `README.md` à la racine :

```markdown
# Hello World JS & Python 👋

Ce dépôt contient deux scripts simples pour afficher "Hello World", un en JavaScript et un en Python.  
C’est mon tout premier projet de développeur fullstack IA 🚀
```
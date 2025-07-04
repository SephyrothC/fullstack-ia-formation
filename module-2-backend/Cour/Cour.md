# 🌐 Cours : Introduction au développement Back-End

## 🚀 Prérequis

- Avoir Node.js installé localement (ou utiliser Replit/Glitch)
- Connaître les bases de JavaScript

---

## 📦 1. Node.js et NPM

- Node.js permet d'exécuter du JavaScript côté serveur.
- NPM est le gestionnaire de paquets officiel de Node.

```bash
npm init -y
npm install express
```

## 🧱 2. Express : le framework minimaliste
```js

Copy
Edit
const express = require('express');
const app = express();

app.get('/', (req, res) => res.send('Hello World!'));

app.listen(3000, () => console.log('Serveur lancé sur le port 3000'));
```
## 🛠 3. Middleware
```js
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path}`);
  next();
});
📮 4. Les routes GET et POST
js
Copy
Edit
app.get('/api/data', (req, res) => {
  res.json({ message: "GET OK" });
});

app.post('/api/data', express.json(), (req, res) => {
  res.json({ message: "POST OK", data: req.body });
});
```
## 🗃 5. MongoDB + Mongoose
```bash
npm install mongoose
js
Copy
Edit
const mongoose = require('mongoose');
mongoose.connect(process.env.MONGO_URI);

const Cat = mongoose.model('Cat', { name: String });
const kitty = new Cat({ name: 'Zelda' });
kitty.save().then(() => console.log('meow'));
```
## 📌 À faire maintenant
Reproduis chaque exemple en local ou sur Replit

Comprends le fonctionnement de chaque brique avant de commencer la certification

### 🧪 `Module-2_Backend/tp-project-backend.md`

```markdown
# 🧪 TP : Création d'une API d'Horloge Mondiale

## 🎯 Objectif

Créer une API REST simple permettant de :

- Recevoir une date (optionnelle)
- Retourner l'heure UTC et l'heure locale correspondante
- Gérer les erreurs (date invalide)

---

## 📥 Exemple de route

### ✅ Entrée

GET /api/2023-01-01

### ✅ Réponse

{
  "unix": 1672531200000,
  "utc": "Sun, 01 Jan 2023 00:00:00 GMT"
}


🧪 Tests complémentaires
GET /api/hello renvoie { "greeting": "hello API" }

GET /api renvoie l'heure actuelle au moment de la requête
```
## 🧠 Contraintes
Utiliser Express.js

Ajouter des commentaires dans le code


## 📝 À rendre
✅ Lien vers l'application déployée

✅ Code source complet (GitHub ou archive zip)

✅ Réponses aux tests dans un fichier tests.txt

---

# AI Blog Generator for Youtube Videos

Application web Django qui transforme automatiquement une vidéo YouTube en article de blog rédigé par une IA.
Lien du projet https://bp-genai-e781afd10fd5.herokuapp.com/

## Comment ça marche ?

1. L'utilisateur se connecte (ou crée un compte) et colle un lien YouTube.
2. **YouTube oEmbed API** récupère le titre de la vidéo.
3. **youtube-transcript-api** extrait les sous-titres directement depuis YouTube (sans téléchargement audio).
4. **Mistral AI** rédige un article de blog structuré, engageant et optimisé SEO à partir de la transcription.
5. L'article est sauvegardé en base de données et consultable à tout moment.

> ⚠️ La vidéo doit avoir des sous-titres disponibles (générés automatiquement ou manuels). La quasi-totalité des vidéos populaires en disposent.

## Fonctionnalités

- Authentification (inscription / connexion / déconnexion)
- Génération d'article depuis un lien YouTube
- Détection des doublons (même vidéo déjà générée)
- Liste de tous ses articles
- Consultation et suppression d'un article

## Stack technique

| Couche | Technologie |
|---|---|
| Backend | Django 6 |
| Base de données | SQLite (dev) / PostgreSQL (prod via Heroku) |
| Titre de la vidéo | YouTube oEmbed API |
| Transcription | youtube-transcript-api |
| Génération de texte | Mistral AI (`mistral-small`) |
| Serveur de production | Gunicorn + Whitenoise |

## Installation (développement)

```bash
pip install -r requirements.txt
```

Créer un fichier `.env` à la racine :

```env
SECRET_KEY=your_django_secret_key
DATABASE_URL=sqlite:///db.sqlite3
MISTRAL_API_key=your_mistral_key
DEBUG=True
```

```bash
python manage.py migrate
python manage.py runserver
```

## Déploiement sur Heroku

```bash
# Configurer les variables d'environnement
heroku config:set SECRET_KEY=your_secret_key
heroku config:set MISTRAL_API_key=your_mistral_key
heroku config:set DEBUG=False

# Déployer
git push heroku main
heroku run python manage.py migrate
```

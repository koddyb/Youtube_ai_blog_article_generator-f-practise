# AI Blog Generator for Youtube Videos

Application web Django qui transforme automatiquement une vidéo YouTube en article de blog rédigé par une IA.

## Comment ça marche ?

1. **L'utilisateur** se connecte (ou crée un compte) et colle un lien YouTube.
2. **yt-dlp** télécharge la piste audio de la vidéo.
3. **AssemblyAI** transcrit l'audio en texte.
4. **Mistral AI** rédige un article de blog structuré et optimisé SEO à partir de la transcription.
5. L'article est sauvegardé en base de données et consultable à tout moment.

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
| Base de données | SQLite (dev) / PostgreSQL (prod) |
| Téléchargement audio | yt-dlp |
| Transcription | AssemblyAI |
| Génération de texte | Mistral AI (`mistral-small`) |

## Installation

```bash
pip install -r requirements.txt
```

Créer un fichier `.env` à la racine avec :

```env
ASSEMBLYAI_API_KEY=your_assemblyai_key
MISTRAL_API_key=your_mistral_key
```

```bash
python manage.py migrate
python manage.py runserver
```

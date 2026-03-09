import logging
import os

from mistralai import Mistral

logger = logging.getLogger(__name__)


def generate_blog_from_transcription(transcription: str) -> str | None:
    """Génère un article de blog à partir d'une transcription via Mistral AI."""
    api_key = os.getenv("MISTRAL_API_key")
    if not api_key:
        logger.error("MISTRAL_API_key non définie dans l'environnement")
        return None

    client = Mistral(api_key=api_key)

    prompt = f"""
    Tu es un rédacteur web expert. À partir de la transcription suivante, 
    rédige un article de blog structuré, engageant et optimisé pour le SEO.
    
    Instructions :
    1. Donne un titre accrocheur.
    2. Ajoute une introduction brève.
    3. Utilise des sous-titres (H2, H3) pour structurer le contenu.
    4. Nettoie les tics de langage et les répétitions de la transcription.
    5. Utilise des listes à puces si nécessaire.
    6. Ajoute une conclusion avec un appel à l'action.

    Transcription : {transcription}
    """

    try:
        chat_response = client.chat.complete(
            model="mistral-small",
            messages=[{"role": "user", "content": prompt}],
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        logger.error(f"[Mistral] Erreur de génération: {type(e).__name__}: {e}")
        return None

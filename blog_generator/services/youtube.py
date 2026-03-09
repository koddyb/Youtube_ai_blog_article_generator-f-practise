import logging
import os
import re

import requests

from django.conf import settings

logger = logging.getLogger(__name__)

# Patterns pour extraire l'ID YouTube depuis n'importe quel format d'URL
_VIDEO_ID_PATTERNS = [
    re.compile(r'(?:v=|\/)([0-9A-Za-z_-]{11})'),
    re.compile(r'youtu\.be\/([0-9A-Za-z_-]{11})'),
]


def extract_video_id(url: str) -> str | None:
    """Extrait l'ID YouTube depuis n'importe quel format d'URL."""
    for pattern in _VIDEO_ID_PATTERNS:
        match = pattern.search(url)
        if match:
            return match.group(1)
    return None


def get_title(link: str) -> str:
    """Récupère le titre via l'API oEmbed YouTube (sans yt-dlp, sans auth)."""
    try:
        r = requests.get(
            'https://www.youtube.com/oembed',
            params={'url': link, 'format': 'json'},
            timeout=5,
        )
        if r.status_code == 200:
            return r.json().get('title', 'YouTube Video')
    except Exception:
        logger.warning(f"[YouTube] Impossible de récupérer le titre pour {link}")
    video_id = extract_video_id(link)
    return f"YouTube Video ({video_id})" if video_id else "YouTube Video"


def get_cookies_path() -> str | None:
    """Retourne le chemin du fichier cookies si disponible."""
    cookies_path = os.path.join(settings.BASE_DIR, 'temp_cookies.txt')
    cookies_content = os.getenv('YT_COOKIES_CONTENT')

    if cookies_content:
        with open(cookies_path, 'w') as f:
            f.write(cookies_content)

    return cookies_path if os.path.exists(cookies_path) else None

"""Utilitaires partagés par les scripts de validation."""

import sys


def utf8_stdio() -> None:
    """Force la sortie en UTF-8.

    Sous Windows, une sortie redirigée (pipe, fichier) est encodée en cp1252 :
    un caractère hors de ce jeu fait planter le script au milieu d'un message
    d'erreur, et le détail utile est perdu.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

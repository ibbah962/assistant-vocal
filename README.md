# Assistant vocal

Application de bureau en Python qui reconnaît des commandes vocales en français, répond par synthèse vocale et peut rechercher une vidéo sur YouTube.

## Fonctionnalités

- Reconnaissance vocale en français via le service Google (connexion Internet requise).
- Recherche d'une vidéo YouTube avec la commande « joue » suivie d'un titre.
- Synthèse vocale des réponses.
- Interface graphique avec CustomTkinter.

Un microphone fonctionnel est nécessaire pour utiliser la reconnaissance vocale.

## Prérequis

- Python 3.
- Ubuntu ou une distribution Linux compatible.
- Microphone et connexion Internet.

Tkinter et PyAudio nécessitent des dépendances système. Sur Ubuntu, installe-les avec :

```bash
sudo apt update
sudo apt install python3-venv python3-dev python3-tk portaudio19-dev build-essential
```

Si tu utilises une version de Python différente de celle fournie par Ubuntu, installe aussi les fichiers d'en-tête correspondant exactement à cette version (par exemple `python3.14-dev`).

## Installation

Depuis le dossier du projet :

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Lancement

```bash
source .venv/bin/activate
python main.py
```

Clique sur le bouton d'écoute et dis une commande, par exemple « joue [titre] » ou « ferme ».

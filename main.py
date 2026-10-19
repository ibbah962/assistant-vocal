import customtkinter as ctk
import speech_recognition as sr
import pyttsx3
from pyttsx3 import speak
from youtube_search import YoutubeSearch
import webbrowser

# Initialiser la reconnaissance vocale et la sythese vocale
recognizer = sr.Recognizer() # Reconnaissance vocale
engine = pyttsx3.init() # Synthese vocale

# Fonction pour parler (Synthese vocale)
def parler(texte):
    engine.say(texte)
    engine.runAndWait()

# Fonction pour ecouter et reconnaitre la voix
def reconnaitre_voix():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Ecoute...")
        try:
            audio = recognizer.listen(source)
            commande = recognizer.recognize_google(audio, language="fr-FR")
            print(f"Vous avez dit: {commande}")
            return commande.lower()
        except sr.UnknownValueError:
            parler("Je n'ai pas compris. Veuillez répéter.")
            return ""
        except sr.RequestError:
            parler("Erreur de service. Veuillez vérifier votre connexion Internet.")
            return ""

# Fonction pour executer les commandes vocales
def execute_commmande():
    command = reconnaitre_voix()
    if "joue" in command:
        song_name = command.replace("joue", "").strip()
        parler(f"Recherche de {song_name} sur Youtube")

        # Recherche sur Youtube
        results = YoutubeSearch(song_name, max_results=1).to_dict()
        if results:
            video_url = f"https://www.youtube.com/watch?v={results[0]['id']}"
            parler(f"Lecture de {results[0]['title']}")
            webbrowser.open(video_url)
        else:
            parler("Aucune vidéo trouvée.")
    elif "Ouvre Youtube" in command:
        parler("Ouverture de Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "ferme" in command:
        parler("Fermeture de l'application")
        app.quit()
    else:
        parler("Commande non reconnue. Veuillez réessayer.")

# Initialiser l'application
app = ctk.CTk()
app.title("Assistant Vocal")
app.geometry("1000x500")

# Apparence de l'application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Label d'instructions
label = ctk.CTkLabel(app, text="Cliquez sur le bouton pour ecouter une commande", font=("Helvetica", 16))
label.pack(pady=30)

# Bouton pour activer la reconnaissance vocale
ecoute_bouton = ctk.CTkButton(app, text="ecouter", command=execute_commmande, font=("Helvetica", 15), height=50, width=200)
ecoute_bouton.pack(pady=20)

# Bouton pour quitter l'application
quitter_bouton = ctk.CTkButton(app, text="Quitter", command=app.quit, font=("Helvetica", 15), height=50, width=200, fg_color="red")
quitter_bouton.pack(pady=20)

app.mainloop()

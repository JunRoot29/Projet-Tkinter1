from tkinter import *
from tkinter import ttk
from .modules import compterVoyelles, compterlettre, compter_occurrences, palindrome

def configurer_style():
    style = ttk.Style()
    style.configure("Rounded.TButton",
                    foreground="#3C3C3C",
                    background="#C7C3BB",
                    font=("Century Gothic", 14),
                    relief="flat")
    return style

def lancer_compt_voy(parent):
    page = Toplevel(parent)
    page.configure(bg="#F5F0E6")
    page.geometry("600x500")
    page.title("Compteur de voyelles")
    style = configurer_style()

    label1 = Label(page, text="Entrez votre texte !", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    entre1 = Text(page, height=10, width=60, font=("Century Gothic", 12))
    entre1.pack(pady=10)

    result_label = Label(page, text="Résultat :", font=("Century Gothic", 14), bg="#F5F0E6")
    result_label.pack(pady=10)

    def test_voyelle():
        texte = entre1.get("1.0", "end").strip()
        if texte:
            try:
                resultat = compterVoyelles(texte)
                result_label.config(text=f"Résultat : {resultat}")
            except Exception as e:
                result_label.config(text=f"Erreur : {str(e)}")
        else:
            result_label.config(text="Veuillez entrer du texte.")

    button1 = ttk.Button(page, text="Testez", style="Rounded.TButton", command=test_voyelle)
    button1.pack(pady=10)

def lancer_compt_lettre():
    page = Toplevel()
    page.configure(bg="#F5F0E6")
    page.geometry("800x600")
    page.title("Compteur de lettres")
    style = configurer_style()

    label1 = Label(page, text="Entrez votre texte \nCette Interface trouve les lettres, pas les mots !", 
                  font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    entre1 = Text(page, height=10, width=60, font=("Century Gothic", 12))
    entre1.pack(pady=10)

    label2 = Label(page, text="Entrez la lettre à compter", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    entre2 = Text(page, height=1, width=10, font=("Century Gothic", 12))
    entre2.pack(pady=10)

    result_label = Label(page, text="Résultat :", font=("Century Gothic", 14), bg="#F5F0E6")
    result_label.pack(pady=10)

    def test_lettre():
        texte1 = entre1.get("1.0", "end").strip()
        texte2 = entre2.get("1.0", "end").strip()
        
        if not texte1 or not texte2:
            result_label.config(text="Veuillez entrer du texte et une lettre.")
            return
        
        if len(texte2) != 1:
            result_label.config(text="Veuillez entrer une seule lettre.")
            return
        
        try:
            resultat = compterlettre(texte1, texte2)
            result_label.config(text=f"Résultat : {resultat}")
        except Exception as e:
            result_label.config(text=f"Erreur : {str(e)}")

    button1 = ttk.Button(page, text="Testez", style="Rounded.TButton", command=test_lettre)
    button1.pack(pady=10)

def lancer_rech_mot():
    page = Toplevel()
    page.configure(bg="#F5F0E6")
    page.geometry("800x600")
    page.title("Recherche de mot")
    style = configurer_style()

    label1 = Label(page, text="Entrez votre texte \nCette Interface trouve le mot à rechercher, pas les lettres !", 
                  font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    entre1 = Text(page, height=10, width=60, font=("Century Gothic", 12))
    entre1.pack(pady=10)

    label2 = Label(page, text="Entrez le mot à compter", font=("Century Gothic", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    entre2 = Text(page, height=1, width=20, font=("Century Gothic", 12))
    entre2.pack(pady=10)

    result_label = Label(page, text="Résultat :", font=("Century Gothic", 14), bg="#F5F0E6")
    result_label.pack(pady=10)

    def test_mot():
        texte1 = entre1.get("1.0", "end").strip()
        texte2 = entre2.get("1.0", "end").strip()
        
        if not texte1 or not texte2:
            result_label.config(text="Veuillez entrer du texte et un mot.")
            return
        
        try:
            resultat = compter_occurrences(texte1, texte2)
            result_label.config(text=f"Résultat : {resultat}")
        except Exception as e:
            result_label.config(text=f"Erreur : {str(e)}")

    button1 = ttk.Button(page, text="Testez", style="Rounded.TButton", command=test_mot)
    button1.pack(pady=10)

def lancer_palindrome():
    page = Toplevel()
    page.configure(bg="#F5F0E6")
    page.geometry("600x500")
    page.title("Palindrome")
    style = configurer_style()

    label1 = Label(page, text="Entrez votre mot !", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    entre1 = Text(page, height=10, width=60, font=("Century Gothic", 12))
    entre1.pack(pady=10)

    result_label = Label(page, text="Résultat :", font=("Century Gothic", 14), bg="#F5F0E6")
    result_label.pack(pady=10)

    def test_palindrome():
        texte = entre1.get("1.0", "end").strip()
        if texte:
            try:
                resultat = palindrome(texte)
                result_label.config(text=f"Résultat : {resultat}")
            except Exception as e:
                result_label.config(text=f"Erreur : {str(e)}")
        else:
            result_label.config(text="Veuillez entrer du texte.")

    button1 = ttk.Button(page, text="Testez", style="Rounded.TButton", command=test_palindrome)
    button1.pack(pady=10)

def lancer_chaine():
    chaine = Toplevel()
    chaine.configure(bg="#F5F0E6")
    chaine.geometry("500x600")
    chaine.title("Opérations sur les chaînes de caractères")

    # Créer le frame pour les boutons
    frame_boutons = Frame(chaine, bg="#F5F0E6")
    frame_boutons.pack(pady=10, padx=20, fill=BOTH, expand=True)

    # Placer le label dans le frame
    label1 = Label(frame_boutons, text="Choisissez une opération", font=("Century Gothic", 14), bg="#F5F0E6")
    label1.pack(pady=20)

    style = configurer_style()
    
    button1 = ttk.Button(frame_boutons, text="Comptage de voyelles dans une phrase", 
                        style="Rounded.TButton", command=lancer_compt_voy)
    button1.pack(pady=10, fill=X)

    button2 = ttk.Button(frame_boutons, text="Comptage d'une lettre dans une chaîne", 
                        style="Rounded.TButton", command=lancer_compt_lettre)
    button2.pack(pady=10, fill=X)

    button3 = ttk.Button(frame_boutons, text="Comptage d'un mot dans une chaîne", 
                        style="Rounded.TButton", command=lancer_rech_mot)
    button3.pack(pady=10, fill=X)

    button4 = ttk.Button(frame_boutons, text="Test Palindrome", 
                        style="Rounded.TButton", command=lancer_palindrome)
    button4.pack(pady=10, fill=X)

    # Bouton pour quitter - utiliser destroy() pour fermer la fenêtre Toplevel
    quit_button = ttk.Button(frame_boutons, text="Quitter", style="Rounded.TButton", 
                           command=chaine.destroy)
    quit_button.pack(pady=20, fill=X)
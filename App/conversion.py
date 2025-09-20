import math
from tkinter import *
from tkinter import ttk
import scipy as sci

# Style global pour les boutons arrondis
style = ttk.Style()
style.configure("Rounded.TButton",
                foreground="#3C3C3C",        # Couleur du texte
                background="#C7C3BB",        # Couleur de fond
                font=("Poppins", 14),        # Police et taille
                padding=15,                  # Espacement interne
                relief="flat",               # Style de bordure (plat)
                width=40)                    # Largeur des boutons

def launch_conversion():
    """
    Fonction principale pour lancer la fenêtre de conversion
    Crée une fenêtre secondaire avec les options de conversion disponibles
    """
    conversion = Toplevel()  # Crée une fenêtre secondaire
    conversion.title("Conversion")  # Définit le titre
    conversion.geometry("600x700")  # Définit la taille
    conversion.configure(bg="#F5F0E6")  # Définit la couleur de fond

    Label(conversion,text="Conversion",font=("Poppins", 24, "bold")).pack()
    Label(conversion,text="Et si on s'amusait à convertir ? \n Choisi ton Opération!",font=("Poppins", 14)).pack()

    options = ["Longueur 📏","Masse et Poids 🏋️","Température🌡️","Vitesse 🏃🏾","Angles 📐","Données 🖲️"]

    combo = ttk.Combobox(conversion,values=options,font=("Poppins", 14))
    combo.pack()


def lancer_longueur():
    """
    Fonction pour lancer l'interface de conversion de longueur
    Affiche un message d'en développement et un clavier numérique
    """
    fenetre = Toplevel()  # Crée une nouvelle fenêtre
    fenetre.title("Longueur")  # Titre de la fenêtre
    fenetre.geometry("600x700")  # Taille de la fenêtre
    fenetre.configure(bg="#F5F0E6")  # Couleur de fond
    
    # Message d'indisponibilité
    Label(fenetre, text="Oups ❌, cette partie est en développement.\n Repasser plus tard.", 
          font=("Poppins", 16), bg="#F5F0E6").pack()
    
    # Création d'un cadre principal pour tous les boutons (clavier numérique)
    main_frame = Frame(fenetre, bg="#F5F0E6")
    main_frame.pack(pady=5)

    # Ligne 1 du clavier (boutons 1, 2, 3)
    ligne1_frame = Frame(main_frame, bg="#F5F0E6")
    ligne1_frame.pack(pady=2)

    btn1 = ttk.Button(ligne1_frame, text="1", style="Rounded.TButton", width=5)
    btn2 = ttk.Button(ligne1_frame, text="2", style="Rounded.TButton", width=5)
    btn3 = ttk.Button(ligne1_frame, text="3", style="Rounded.TButton", width=5)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)

    # Ligne 2 du clavier (boutons 4, 5, 6)
    ligne2_frame = Frame(main_frame, bg="#F5F0E6")
    ligne2_frame.pack(pady=2)

    btn4 = ttk.Button(ligne2_frame, text="4", style="Rounded.TButton", width=5)
    btn5 = ttk.Button(ligne2_frame, text="5", style="Rounded.TButton", width=5)
    btn6 = ttk.Button(ligne2_frame, text="6", style="Rounded.TButton", width=5)

    btn4.pack(side="left", padx=2)
    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)

    # Ligne 3 du clavier (boutons 7, 8, 9)
    ligne3_frame = Frame(main_frame, bg="#F5F0E6")
    ligne3_frame.pack(pady=2)

    btn7 = ttk.Button(ligne3_frame, text="7", style="Rounded.TButton", width=5)
    btn8 = ttk.Button(ligne3_frame, text="8", style="Rounded.TButton", width=5)
    btn9 = ttk.Button(ligne3_frame, text="9", style="Rounded.TButton", width=5)

    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn9.pack(side="left", padx=2)

    # Ligne 4 du clavier (boutons 0, point décimal, escape)
    ligne4_frame = Frame(main_frame, bg="#F5F0E6")
    ligne4_frame.pack(pady=2)

    btn10 = ttk.Button(ligne4_frame, text="0", style="Rounded.TButton", width=5)
    btn11 = ttk.Button(ligne4_frame, text=".", style="Rounded.TButton", width=5)
    btn12 = ttk.Button(ligne4_frame, text="esc", style="Rounded.TButton", width=5)

    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)

def lancer_masse_poids():
    """Fonction pour lancer l'interface de conversion de masse et poids"""
    fenetre = Toplevel()
    fenetre.title("Masse et Poids")
    fenetre.geometry("600x700")
    fenetre.configure(bg="#F5F0E6")
    Label(fenetre, text="Oups ❌, cette partie est en développement.\n Repasser plus tard.", font=("Poppins", 16), bg="#F5F0E6").pack()

    # Création d'un cadre principal pour tous les boutons
    main_frame = Frame(fenetre, bg="#F5F0E6")
    main_frame.pack(pady=5)

    # Ligne 1 
    ligne1_frame = Frame(main_frame, bg="#F5F0E6")
    ligne1_frame.pack(pady=2)

    btn1 = ttk.Button(ligne1_frame, text="1", style="Rounded.TButton", width=5)
    btn2 = ttk.Button(ligne1_frame, text="2", style="Rounded.TButton", width=5)
    btn3 = ttk.Button(ligne1_frame, text="3", style="Rounded.TButton", width=5)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)

    # Ligne 2
    ligne2_frame = Frame(main_frame, bg="#F5F0E6")
    ligne2_frame.pack(pady=2)

    btn4 = ttk.Button(ligne2_frame, text="4", style="Rounded.TButton", width=5)
    btn5 = ttk.Button(ligne2_frame, text="5", style="Rounded.TButton", width=5)
    btn6 = ttk.Button(ligne2_frame, text="6", style="Rounded.TButton", width=5)

    btn4.pack(side="left", padx=2)
    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)

    # Ligne 3
    ligne3_frame = Frame(main_frame, bg="#F5F0E6")
    ligne3_frame.pack(pady=2)

    btn7 = ttk.Button(ligne3_frame, text="7", style="Rounded.TButton", width=5)
    btn8 = ttk.Button(ligne3_frame, text="8", style="Rounded.TButton", width=5)
    btn9 = ttk.Button(ligne3_frame, text="9", style="Rounded.TButton", width=5)

    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn9.pack(side="left", padx=2)

    # Ligne 4
    ligne4_frame = Frame(main_frame, bg="#F5F0E6")
    ligne4_frame.pack(pady=2)

    btn10 = ttk.Button(ligne4_frame, text="0", style="Rounded.TButton", width=5)
    btn11 = ttk.Button(ligne4_frame, text=".", style="Rounded.TButton", width=5)
    btn12 = ttk.Button(ligne4_frame, text="esc", style="Rounded.TButton", width=5)

    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)

def lancer_temperature():
    """Fonction pour lancer l'interface de conversion de température"""
    fenetre = Toplevel()
    fenetre.title("Température")
    fenetre.geometry("600x700")
    fenetre.configure(bg="#F5F0E6")
    Label(fenetre, text="Oups ❌, cette partie est en développement.\n Repasser plus tard.", font=("Poppins", 16), bg="#F5F0E6").pack()

    # Création d'un cadre principal pour tous les boutons
    main_frame = Frame(fenetre, bg="#F5F0E6")
    main_frame.pack(pady=5)

    # Ligne 1 
    ligne1_frame = Frame(main_frame, bg="#F5F0E6")
    ligne1_frame.pack(pady=2)

    btn1 = ttk.Button(ligne1_frame, text="1", style="Rounded.TButton", width=5)
    btn2 = ttk.Button(ligne1_frame, text="2", style="Rounded.TButton", width=5)
    btn3 = ttk.Button(ligne1_frame, text="3", style="Rounded.TButton", width=5)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)

    # Ligne 2
    ligne2_frame = Frame(main_frame, bg="#F5F0E6")
    ligne2_frame.pack(pady=2)

    btn4 = ttk.Button(ligne2_frame, text="4", style="Rounded.TButton", width=5)
    btn5 = ttk.Button(ligne2_frame, text="5", style="Rounded.TButton", width=5)
    btn6 = ttk.Button(ligne2_frame, text="6", style="Rounded.TButton", width=5)

    btn4.pack(side="left", padx=2)
    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)

    # Ligne 3
    ligne3_frame = Frame(main_frame, bg="#F5F0E6")
    ligne3_frame.pack(pady=2)

    btn7 = ttk.Button(ligne3_frame, text="7", style="Rounded.TButton", width=5)
    btn8 = ttk.Button(ligne3_frame, text="8", style="Rounded.TButton", width=5)
    btn9 = ttk.Button(ligne3_frame, text="9", style="Rounded.TButton", width=5)

    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn9.pack(side="left", padx=2)

    # Ligne 4
    ligne4_frame = Frame(main_frame, bg="#F5F0E6")
    ligne4_frame.pack(pady=2)

    btn10 = ttk.Button(ligne4_frame, text="0", style="Rounded.TButton", width=5)
    btn11 = ttk.Button(ligne4_frame, text=".", style="Rounded.TButton", width=5)
    btn12 = ttk.Button(ligne4_frame, text="esc", style="Rounded.TButton", width=5)

    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)

def lancer_vitesse():
    """Fonction pour lancer l'interface de conversion de vitesse"""
    fenetre = Toplevel()
    fenetre.title("Vitesse")
    fenetre.geometry("600x700")
    fenetre.configure(bg="#F5F0E6")
    Label(fenetre, text="Oups ❌, cette partie est en développement.\n Repasser plus tard.", font=("Poppins", 16), bg="#F5F0E6").pack()
    
    # Création d'un cadre principal pour tous les boutons
    main_frame = Frame(fenetre, bg="#F5F0E6")
    main_frame.pack(pady=5)

    # Ligne 1 
    ligne1_frame = Frame(main_frame, bg="#F5F0E6")
    ligne1_frame.pack(pady=2)

    btn1 = ttk.Button(ligne1_frame, text="1", style="Rounded.TButton", width=5)
    btn2 = ttk.Button(ligne1_frame, text="2", style="Rounded.TButton", width=5)
    btn3 = ttk.Button(ligne1_frame, text="3", style="Rounded.TButton", width=5)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)

    # Ligne 2
    ligne2_frame = Frame(main_frame, bg="#F5F0E6")
    ligne2_frame.pack(pady=2)

    btn4 = ttk.Button(ligne2_frame, text="4", style="Rounded.TButton", width=5)
    btn5 = ttk.Button(ligne2_frame, text="5", style="Rounded.TButton", width=5)
    btn6 = ttk.Button(ligne2_frame, text="6", style="Rounded.TButton", width=5)

    btn4.pack(side="left", padx=2)
    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)

    # Ligne 3
    ligne3_frame = Frame(main_frame, bg="#F5F0E6")
    ligne3_frame.pack(pady=2)

    btn7 = ttk.Button(ligne3_frame, text="7", style="Rounded.TButton", width=5)
    btn8 = ttk.Button(ligne3_frame, text="8", style="Rounded.TButton", width=5)
    btn9 = ttk.Button(ligne3_frame, text="9", style="Rounded.TButton", width=5)

    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn9.pack(side="left", padx=2)

    # Ligne 4
    ligne4_frame = Frame(main_frame, bg="#F5F0E6")
    ligne4_frame.pack(pady=2)

    btn10 = ttk.Button(ligne4_frame, text="0", style="Rounded.TButton", width=5)
    btn11 = ttk.Button(ligne4_frame, text=".", style="Rounded.TButton", width=5)
    btn12 = ttk.Button(ligne4_frame, text="esc", style="Rounded.TButton", width=5)

    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)

def lancer_angles():
    """Fonction pour lancer l'interface de conversion d'angles"""
    fenetre = Toplevel()
    fenetre.title("Angles")
    fenetre.geometry("600x700")
    fenetre.configure(bg="#F5F0E6")
    Label(fenetre, text="Oups ❌, cette partie est en développement.\n Repasser plus tard.", font=("Poppins", 16), bg="#F5F0E6").pack()
    
    # Création d'un cadre principal pour tous les boutons
    main_frame = Frame(fenetre, bg="#F5F0E6")
    main_frame.pack(pady=5)

    # Ligne 1 
    ligne1_frame = Frame(main_frame, bg="#F5F0E6")
    ligne1_frame.pack(pady=2)

    btn1 = ttk.Button(ligne1_frame, text="1", style="Rounded.TButton", width=5)
    btn2 = ttk.Button(ligne1_frame, text="2", style="Rounded.TButton", width=5)
    btn3 = ttk.Button(ligne1_frame, text="3", style="Rounded.TButton", width=5)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)

    # Ligne 2
    ligne2_frame = Frame(main_frame, bg="#F5F0E6")
    ligne2_frame.pack(pady=2)

    btn4 = ttk.Button(ligne2_frame, text="4", style="Rounded.TButton", width=5)
    btn5 = ttk.Button(ligne2_frame, text="5", style="Rounded.TButton", width=5)
    btn6 = ttk.Button(ligne2_frame, text="6", style="Rounded.TButton", width=5)

    btn4.pack(side="left", padx=2)
    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)

    # Ligne 3
    ligne3_frame = Frame(main_frame, bg="#F5F0E6")
    ligne3_frame.pack(pady=2)

    btn7 = ttk.Button(ligne3_frame, text="7", style="Rounded.TButton", width=5)
    btn8 = ttk.Button(ligne3_frame, text="8", style="Rounded.TButton", width=5)
    btn9 = ttk.Button(ligne3_frame, text="9", style="Rounded.TButton", width=5)

    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn9.pack(side="left", padx=2)

    # Ligne 4
    ligne4_frame = Frame(main_frame, bg="#F5F0E6")
    ligne4_frame.pack(pady=2)

    btn10 = ttk.Button(ligne4_frame, text="0", style="Rounded.TButton", width=5)
    btn11 = ttk.Button(ligne4_frame, text=".", style="Rounded.TButton", width=5)
    btn12 = ttk.Button(ligne4_frame, text="esc", style="Rounded.TButton", width=5)

    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)

def lancer_donnees():
    """Fonction pour lancer l'interface de conversion de données"""
    fenetre = Toplevel()
    fenetre.title("Données")
    fenetre.geometry("600x700")
    fenetre.configure(bg="#F5F0E6")
    Label(fenetre, text="Oups ❌, cette partie est en développement.\n Repasser plus tard.", font=("Poppins", 16), bg="#F5F0E6").pack()
    
    # Création d'un cadre principal pour tous les boutons
    main_frame = Frame(fenetre, bg="#F5F0E6")
    main_frame.pack(pady=5)

    # Ligne 1 
    ligne1_frame = Frame(main_frame, bg="#F5F0E6")
    ligne1_frame.pack(pady=2)

    btn1 = ttk.Button(ligne1_frame, text="1", style="Rounded.TButton", width=5)
    btn2 = ttk.Button(ligne1_frame, text="2", style="Rounded.TButton", width=5)
    btn3 = ttk.Button(ligne1_frame, text="3", style="Rounded.TButton", width=5)

    btn1.pack(side="left", padx=2)
    btn2.pack(side="left", padx=2)
    btn3.pack(side="left", padx=2)

    # Ligne 2
    ligne2_frame = Frame(main_frame, bg="#F5F0E6")
    ligne2_frame.pack(pady=2)

    btn4 = ttk.Button(ligne2_frame, text="4", style="Rounded.TButton", width=5)
    btn5 = ttk.Button(ligne2_frame, text="5", style="Rounded.TButton", width=5)
    btn6 = ttk.Button(ligne2_frame, text="6", style="Rounded.TButton", width=5)

    btn4.pack(side="left", padx=2)
    btn5.pack(side="left", padx=2)
    btn6.pack(side="left", padx=2)

    # Ligne 3
    ligne3_frame = Frame(main_frame, bg="#F5F0E6")
    ligne3_frame.pack(pady=2)

    btn7 = ttk.Button(ligne3_frame, text="7", style="Rounded.TButton", width=5)
    btn8 = ttk.Button(ligne3_frame, text="8", style="Rounded.TButton", width=5)
    btn9 = ttk.Button(ligne3_frame, text="9", style="Rounded.TButton", width=5)

    btn7.pack(side="left", padx=2)
    btn8.pack(side="left", padx=2)
    btn9.pack(side="left", padx=2)

    # Ligne 4
    ligne4_frame = Frame(main_frame, bg="#F5F0E6")
    ligne4_frame.pack(pady=2)

    btn10 = ttk.Button(ligne4_frame, text="0", style="Rounded.TButton", width=5)
    btn11 = ttk.Button(ligne4_frame, text=".", style="Rounded.TButton", width=5)
    btn12 = ttk.Button(ligne4_frame, text="esc", style="Rounded.TButton", width=5)

    btn10.pack(side="left", padx=2)
    btn11.pack(side="left", padx=2)
    btn12.pack(side="left", padx=2)
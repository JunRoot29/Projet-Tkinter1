from tkinter import *
from tkinter import ttk
from .modules import nbr_distinct
from .modules import nbr_parfait
from .modules import nb_premier
from .modules import catalan
from .modules import pgcdrec
from .modules import ppcm

# Définition du style global pour les boutons arrondis
def configurer_style():
    style = ttk.Style()
    style.configure("Rounded.TButton",
                    foreground="#3C3C3C",  
                    background="#C7C3BB",  
                    font=("Poppins", 14),  
                    padding=(20, 10),  # Uniformiser le padding
                    relief="flat",
                    width=60)  # Définir une largeur uniforme
    return style


# Fonction pour lancer la fenêtre "Nombre parfait"
def lancer_nombre_parfait():
    nbr = Toplevel() 
    nbr.title("Nombre Parfait") 
    nbr.configure(bg="#F5F0E6")  # Couleur de fond
    nbr.geometry("600x500")  # Taille de la fenêtre

    label = Label(nbr, text="VERIFICATION NOMBRE PARFAIT", font=("Poppins", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Poppins", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    # Configuration du style
    style = configurer_style()
    
    # Textbox    
    entre = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre.pack(pady=10)

    # Fonction de test
    def test_parfait():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nbr_parfait(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    # Remise à blanc
    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    # Création d'un bouton pour tester
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Tester", command=test_parfait)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Poppins", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)
 

# Fonction pour lancer la fenêtre "Nombre distinct"
def lancer_nombre_distinct():
    nbr = Toplevel() 
    nbr.title("Nombre distinct") 
    nbr.configure(bg="#F5F0E6")  # Couleur de fond
    nbr.geometry("600x500")  # Taille de la fenêtre
    
    label = Label(nbr, text="VERIFICATION NOMBRE DISTINCT", font=("Poppins", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Poppins", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    # Configuration du style
    style = configurer_style()
    
    # Textbox    
    entre = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre.pack(pady=10)

    # Fonction de test
    def test_distinct():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nbr_distinct(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    # Remise à blanc
    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    # Création d'un bouton pour tester
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Tester", command=test_distinct)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Poppins", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

# Fonction pour lancer la fenêtre "Nombre premier"
def lancer_nombre_premier():
    nbr = Toplevel() 
    nbr.title("Nombre Premier") 
    nbr.configure(bg="#F5F0E6")  # Couleur de fond
    nbr.geometry("600x500")  # Taille de la fenêtre
    
    label = Label(nbr, text="TEST DE PRIMALITÉ (Nombre Premier)", font=("Poppins", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre à tester", font=("Poppins", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    # Configuration du style
    style = configurer_style()
    
    # Textbox    
    entre = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre.pack(pady=10)

    # Fonction de test
    def test_premier():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = nb_premier(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    # Remise à blanc
    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    # Création d'un bouton pour tester
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Tester", command=test_premier)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Poppins", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)


# Fonction pour lancer le PGCD
def lancer_pgcd():
    nbr = Toplevel() 
    nbr.title("PGCD") 
    nbr.configure(bg="#F5F0E6")  # Couleur de fond
    nbr.geometry("600x550")  # Taille de la fenêtre

    label = Label(nbr, text="CALCUL PGCD", font=("Poppins", 16), bg="#F5F0E6")
    label.pack(pady=20)

    # Saisie du premier nombre par l'utilisateur
    label1 = Label(nbr, text="Entrez le premier nombre", font=("Poppins", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    # Configuration du style
    style = configurer_style()
    
    # Textbox nombre 1   
    entre1 = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre1.pack(pady=10)

    # Saisie du deuxième nombre par l'utilisateur
    label2 = Label(nbr, text="Entrez le deuxième nombre", font=("Poppins", 14), bg="#F5F0E6")
    label2.pack(pady=10)
    
    entre2 = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre2.pack(pady=10)

    # Fonction de test
    def test_pgcd():
        try:
            valeur1 = int(entre1.get("1.0", "end").strip())
            valeur2 = int(entre2.get("1.0", "end").strip())
            resultat = pgcdrec(valeur1, valeur2)
            label_resultat.config(text=f"Résultat : {resultat}")
        except:
            label_resultat.config(text="Réessayer : Opération Impossible")

    # Remise à blanc
    def remise_a_blanc():
        label_resultat.configure(text="Résultat : ")
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")

    # Création d'un bouton pour tester
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Calculer", command=test_pgcd)
    bouton1.pack(pady=10) 
    
    label_resultat = Label(nbr, text="Résultat : ", font=("Poppins", 14), bg="#F5F0E6")
    label_resultat.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)


# Fonction pour lancer le PPCM
def lancer_ppcm():
    nbr = Toplevel() 
    nbr.title("PPCM") 
    nbr.configure(bg="#F5F0E6")  # Couleur de fond
    nbr.geometry("600x550")  # Taille de la fenêtre

    label = Label(nbr, text="CALCUL PPCM", font=("Poppins", 16), bg="#F5F0E6")
    label.pack(pady=20)

    # Saisie du premier nombre par l'utilisateur
    label1 = Label(nbr, text="Entrez le premier nombre", font=("Poppins", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    # Configuration du style
    style = configurer_style()
    
    # Textbox nombre 1   
    entre1 = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre1.pack(pady=10)

    # Saisie du deuxième nombre par l'utilisateur
    label2 = Label(nbr, text="Entrez le deuxième nombre", font=("Poppins", 14), bg="#F5F0E6")
    label2.pack(pady=10)
    
    entre2 = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre2.pack(pady=10)

    # Fonction de test
    def test_ppcm():
        try:
            valeur1 = int(entre1.get("1.0", "end").strip())
            valeur2 = int(entre2.get("1.0", "end").strip())
            resultat = ppcm(valeur1, valeur2)
            label_resultat.config(text=f"Résultat : {resultat}")
        except:
            label_resultat.config(text="Réessayer : Opération Impossible")

    # Remise à blanc
    def remise_a_blanc():
        label_resultat.configure(text="Résultat : ")
        entre1.delete("1.0", "end")
        entre2.delete("1.0", "end")

    # Création d'un bouton pour tester
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Calculer", command=test_ppcm)
    bouton1.pack(pady=10) 
    
    label_resultat = Label(nbr, text="Résultat : ", font=("Poppins", 14), bg="#F5F0E6")
    label_resultat.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)

# Fonction pour lancer la fenêtre "Nombre Catalan"
def lancer_nombre_catalan():
    nbr = Toplevel() 
    nbr.title("Nombres Catalans") 
    nbr.configure(bg="#F5F0E6")  # Couleur de fond
    nbr.geometry("600x500")  # Taille de la fenêtre

    label = Label(nbr, text="CALCUL DU NOMBRE CATALAN", font=("Poppins", 16), bg="#F5F0E6")
    label.pack(pady=20)

    label1 = Label(nbr, text="Entrez le nombre", font=("Poppins", 14), bg="#F5F0E6")
    label1.pack(pady=10)

    # Configuration du style
    style = configurer_style()
    
    # Textbox    
    entre = Text(nbr, height=2, width=40, font=("Poppins", 12))
    entre.pack(pady=10)

    # Fonction de test
    def test_catalan():
        try:
            valeur = int(entre.get("1.0", "end").strip())
            resultat = catalan(valeur)
            label2.config(text=f"Résultat : {resultat}")
        except:
            label2.config(text="Réessayer : Opération Impossible")

    # Remise à blanc
    def remise_a_blanc():
        label2.configure(text="Résultat : ")
        entre.delete("1.0", "end")

    # Création d'un bouton pour tester
    bouton1 = ttk.Button(nbr, style="Rounded.TButton", text="Calculer", command=test_catalan)
    bouton1.pack(pady=10) 
    
    label2 = Label(nbr, text="Résultat : ", font=("Poppins", 14), bg="#F5F0E6")
    label2.pack(pady=10)

    bouton2 = ttk.Button(nbr, style="Rounded.TButton", text="Remise à blanc", command=remise_a_blanc)
    bouton2.pack(pady=10)


# Fonction principale pour lancer le module "Théorie des nombres"
def lancer_theorie(parent=None):
    th = Toplevel(parent)  # Création de la fenêtre principale
    th.title("Théorie des nombres")  # Titre
    th.configure(bg="#F5F0E6")  # Couleur de fond
    th.geometry("500x700")  # Taille de la fenêtre

    # Label d'introduction
    label1 = Label(th, text="Choisissez votre test", font=("Poppins", 16, "bold"), bg="#F5F0E6")
    label1.pack(pady=20)

    # Configuration du style
    style = configurer_style()

    # Cadre pour contenir les boutons
    frame_boutons = Frame(th, bg="#F5F0E6")
    frame_boutons.pack(pady=10, padx=20, fill=BOTH, expand=True)

    # Boutons pour chaque test, avec appel à la fonction correspondante
    bouton1 = ttk.Button(frame_boutons, text="Nombre parfait", style="Rounded.TButton", command=lancer_nombre_parfait)
    bouton1.pack(pady=10, fill=X, padx=50)

    bouton2 = ttk.Button(frame_boutons, text="Nombre distinct", style="Rounded.TButton", command=lancer_nombre_distinct)
    bouton2.pack(pady=10, fill=X, padx=50)

    bouton3 = ttk.Button(frame_boutons, text="Nombre premier", style="Rounded.TButton", command=lancer_nombre_premier)
    bouton3.pack(pady=10, fill=X, padx=50)

    bouton4 = ttk.Button(frame_boutons, text="PGCD", style="Rounded.TButton", command=lancer_pgcd)
    bouton4.pack(pady=10, fill=X, padx=50)

    bouton5 = ttk.Button(frame_boutons, text="PPCM", style="Rounded.TButton", command=lancer_ppcm)
    bouton5.pack(pady=10, fill=X, padx=50)

    bouton6 = ttk.Button(frame_boutons, text="Nombres Catalans", style="Rounded.TButton", command=lancer_nombre_catalan)
    bouton6.pack(pady=10, fill=X, padx=50)

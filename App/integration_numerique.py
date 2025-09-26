from tkinter import *
from App import modules as modu
from tkinter import ttk
donnees = ["Rectangle Retrograde","Rectangle progressif","Rectangle Centré","Trapèzes Composite","Trapèzes Simples","Simpson Simple","Simpson Composite"]

style = ttk.Style()
style.configure("Custom.TButton",
                foreground="#3C3C3C",
                background="#C7C3BB",
                font=("Poppins", 12),
                padding=8,
                relief="flat")

"""AJOUT DE VALEURS AUX ENTRY"""
var_a = StringVar()
var_b = StringVar()
var_n = StringVar()
var_f = StringVar()
    

def lancer_integration_numerique(parent = None):
    fenetre_integration = Toplevel(parent)
    fenetre_integration.configure(bg="#F5F0E6")
    fenetre_integration.geometry("600x800")
    fenetre_integration.title("Intégration Numérique")
    Label(fenetre_integration,text="Des Intégration Numérique ?😏📈",font=("Poppins", 24,"bold"),fg="#2C3E50",bg="#F5F0E6").pack()
    Label(fenetre_integration,text="Alors quel Opération?😊",font=("Poppins", 14),fg="#2C3E50",bg="#F5F0E6").pack()

    combo = ttk.Combobox(fenetre_integration,font=("Poppins", 14),values=donnees,state="readonly")
    combo.pack(pady=20)

    frame_contenu = Frame(fenetre_integration)
    frame_contenu.pack()

    Label(frame_contenu,text="Entrez Les valeurs d'Intégration",font=("Poppins", 16)).pack(pady=20)
    Label(frame_contenu,text="Entrez La Fonction à Intégrer",font=("Poppins", 14)).pack()
    entree_f = Entry(frame_contenu,font=("Poppins", 14),textvariable=var_f)
    entree_f.pack(padx=20)

    frame_a = Frame(frame_contenu)
    frame_b = Frame(frame_contenu)
    frame_n = Frame(frame_contenu)
    frame_a.pack()
    frame_b.pack()
    frame_n.pack()

    Label(frame_a,text="Entrez a (Debut) : ",font=("Poppins", 14)).pack(side="left")
    entree_a = Entry(frame_a,font=("Poppins", 14),textvariable=var_a)
    entree_a.pack(side="left")

    Label(frame_b,text="Entrez b (Fin) : ",font=("Poppins", 14)).pack(side="left")
    entree_b = Entry(frame_b,font=("Poppins", 14),textvariable=var_b)
    entree_b.pack(side="left")

    Label(frame_n,text="Entrez n (la subdivision) : ",font=("Poppins", 14)).pack(side="left")
    entree_n = Entry(frame_n,font=("Poppins", 14),textvariable=var_n)
    entree_n.pack(side="left")

    frame_bouton = Frame(frame_contenu)
    frame_bouton.pack()
    ligne1 = Frame(frame_bouton)
    ligne2 = Frame(frame_bouton)
    ligne3 = Frame(frame_bouton)
    ligne1.pack()
    ligne2.pack()
    ligne3.pack()

    Button1 = ttk.Button(ligne1,text="x",style="Custom.TButton")
    Button2 = ttk.Button(ligne1,text="(",style="Custom.TButton")
    Button3 = ttk.Button(ligne1,text=")",style="Custom.TButton")
    Button4 = ttk.Button(ligne2,text="√",style="Custom.TButton")
    Button5 = ttk.Button(ligne2,text="tan",style="Custom.TButton")
    Button6 = ttk.Button(ligne2,text="cos",style="Custom.TButton")
    Button7 = ttk.Button(ligne3,text="sin",style="Custom.TButton")
    Button8 = ttk.Button(ligne3,text="π",style="Custom.TButton")
    Button9 = ttk.Button(ligne3,text="<--",style="Custom.TButton")

    Button1.pack(side="left")
    Button2.pack(side="left")
    Button3.pack(side="left")
    Button4.pack(side="left")
    Button5.pack(side="left")
    Button6.pack(side="left")
    Button7.pack(side="left")
    Button8.pack(side="left")
    Button9.pack(side="left")

    Resultat = Label(frame_contenu,text="Resultat : ",font=("Poppins", 14))
    Resultat.pack()
    
    

    

    
    

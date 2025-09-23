import math
from tkinter import *
from tkinter import ttk
from .modules import polynome1,polynome2

def style_configure():
    style = ttk.Style()
    style.configure("Rounded.TButton",
                foreground="#3C3C3C",
                background="#C7C3BB",
                font=("poppins", 14),
                relief="flat")

style = style_configure()

# ------------------ Polynôme de degré 1 ------------------
def lancer_polynome1():
    fenetre_polynome1 = Toplevel()
    fenetre_polynome1.configure(bg="#F5F0E6")
    fenetre_polynome1.title("Polynome dégré 1")
    fenetre_polynome1.geometry("500x700")

    def recherche_resultat():
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        
        if nombre1 and nombre2:
            try:
                resultat = polynome1(nombre1, nombre2)
                result_label.config(text=f"Résultat : {resultat}")
            except Exception as e:
                result_label.config(text=f"Erreur : {e}")
        else:
            result_label.config(text="Entrez des valeurs correctes")

    label1 = Label(fenetre_polynome1, text="RESOLUTION DES POLYNOMES DE DEGRE 1",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14), justify="center")
    label1.pack(pady=10)

    label2 = Label(fenetre_polynome1, text="Entrez la valeur de a",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome1, height=1, width=40, font=("Poppins", 14))
    entre1.pack()

    label3 = Label(fenetre_polynome1, text="Entrez la valeur de b",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome1, height=1, width=40, font=("Poppins", 14))
    entre2.pack()

    result_label = Label(fenetre_polynome1, text="Résultat :", font=("Poppins", 14), bg="#F5F0E6")
    result_label.pack(pady=10)

    button = ttk.Button(fenetre_polynome1, style="Rounded.TButton", text="Calculez", command=recherche_resultat)
    button.pack(pady=20)

# ------------------ Polynôme de degré 2 ------------------
def lancer_polynome2():
    fenetre_polynome2 = Toplevel()
    fenetre_polynome2.configure(bg="#F5F0E6")
    fenetre_polynome2.title("Polynome dégré 2")
    fenetre_polynome2.geometry("500x700")

    def recherche_resultat():
        nombre1 = entre1.get("1.0", "end").strip()
        nombre2 = entre2.get("1.0", "end").strip()
        nombre3 = entre3.get("1.0", "end").strip()

        if nombre1 and nombre2 and nombre3:
            try:
                resultat = polynome2(nombre1, nombre2, nombre3)
                result_label.config(text=f"Résultat : {resultat}")
            except Exception as e:
                result_label.config(text=f"Erreur : {e}")
        else:
            result_label.config(text="Entrez des valeurs correctes")

    label1 = Label(fenetre_polynome2, text="RESOLUTION DES POLYNOMES DE DEGRE 2",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14), justify="center")
    label1.pack(pady=10)

    label2 = Label(fenetre_polynome2, text="Entrez la valeur de a",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14), justify="center")
    label2.pack(pady=10)

    entre1 = Text(fenetre_polynome2, height=1, width=40, font=("Poppins", 14))
    entre1.pack()

    label3 = Label(fenetre_polynome2, text="Entrez la valeur de b",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14), justify="center")
    label3.pack(pady=10)

    entre2 = Text(fenetre_polynome2, height=1, width=40, font=("Poppins", 14))
    entre2.pack()

    label4 = Label(fenetre_polynome2, text="Entrez la valeur de c",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14), justify="center")
    label4.pack(pady=10)

    entre3 = Text(fenetre_polynome2, height=1, width=40, font=("Poppins", 14))
    entre3.pack()

    result_label = Label(fenetre_polynome2, text="Résultat :", font=("Poppins", 14), bg="#F5F0E6")
    result_label.pack(pady=10)

    button = ttk.Button(fenetre_polynome2, style="Rounded.TButton", text="Calculez", command=recherche_resultat)
    button.pack(pady=20)

# ------------------ Menu principal ------------------
def lancer_polynome(parent = None):
    fenetre_polynome = Toplevel(parent)
    fenetre_polynome.configure(bg="#F5F0E6")
    fenetre_polynome.title("Polynome")
    fenetre_polynome.geometry("500x700")

    label1 = Label(fenetre_polynome, text="Choisi le polynome approprié!",
                   fg="#3C3C3C", bg="#F5F0E6", font=("poppins", 14, "bold"), justify="center")
    label1.pack(pady=10)

    button1 = ttk.Button(fenetre_polynome,
                         text="Polynome de dégré 1  (ax+b=0)",
                         style="Rounded.TButton",
                         command=lancer_polynome1)

    button2 = ttk.Button(fenetre_polynome,
                         text="Polynome de dégré 2(ax²+bx+c=0)",
                         style="Rounded.TButton",
                         command=lancer_polynome2)

    button3 = ttk.Button(fenetre_polynome,
                         text="Quitter",
                         style="Rounded.TButton",
                         compound=LEFT,
                         command=fenetre_polynome.destroy)

    button1.pack(pady=20, fill=X)
    button2.pack(pady=20, fill=X)
    button3.pack(pady=20, fill=X)

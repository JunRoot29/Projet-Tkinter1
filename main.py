from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from App import polynome as poly
from App import operation_de_base as op
from App import theorie_des_nombres as theorie
from App import conversion as conv
from App import chaine_de_caractere as ch

# Fenetre principal
fenetre = Tk()
fenetre.title("MathsCraft")
fenetre.geometry("1000x1200")  # Taille personnalisée
fenetre.configure(bg="#F5F0E6")  # Couleur de fond douce


# Configuration du style pour les boutons
style = ttk.Style()
style.configure("Custom.TButton",
                foreground="#3C3C3C",
                background="#C7C3BB",
                font=("Poppins", 14),
                padding=15,
                relief="flat",
                width=40)  # Largeur uniforme pour tous les boutons

#---------------------------Cette partie est généré par DeepSeek-----------------------------
#Je n'en suis pas fière mais boff...

# Cadre pour contenir les boutons avec défilement si nécessaire
frame = Frame(fenetre, bg="#F5F0E6")
frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

# --- AJOUTER CES LIGNES POUR LA SCROLLBAR ---
# Créer un Canvas avec une Scrollbar
canvas = Canvas(frame, bg="#F5F0E6", highlightthickness=0)
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#F5F0E6")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Permettre le défilement avec la molette de la souris
def _on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
# ----------------------------------------------------------------------------------------------



# Phrase de bienvenue
label1 = Label(
    scrollable_frame,
    text="MathCrafts",
    font=("Poppins", 24, "bold"),
    fg="#2C3E50",
    bg="#F5F0E6"
)
label1.pack()

labels = Label(
    scrollable_frame,
    text="Un espace malin, Calculer et s'amuser avec les maths. 🧠✨",
    font=("Poppins", 14),
    fg="#2C3E50",
    bg="#F5F0E6"
)
labels.pack(pady=20)

# Instruction
label2 = Label(
    scrollable_frame,
    text="Choisis ton opération !",
    fg="black",
    bg="#F5F0E6",
    font=("Poppins", 14),
    justify="center"
)
label2.pack(pady=10)

# Boutons pour les Modules
bouton1 = ttk.Button(
    scrollable_frame,
    text="Module 1 : Opération de Base",
    style="Custom.TButton",
    compound=LEFT,
    command=op.launch_operation,
)

bouton2 = ttk.Button(
    scrollable_frame,
    text="Module 2 : Théorie des nombres",
    style="Custom.TButton",
    compound=LEFT,
    command=theorie.lancer_theorie,
)

bouton3 = ttk.Button(
    scrollable_frame,
    text="Module 3 : Conversion",
    style="Custom.TButton",
    compound=LEFT,
    command=conv.launch_conversion
)

bouton4 = ttk.Button(
    scrollable_frame,
    text="Module 4 : Explorateur de Concepts",
    style="Custom.TButton",
    compound=LEFT,
)


bouton6 = ttk.Button(
    scrollable_frame,
    text="Module 5 : Polynomes & Equations",
    style="Custom.TButton",
    compound=LEFT,
    command=poly.lancer_polynome)

bouton8 = ttk.Button(
    scrollable_frame,
    text="Module 6 : Opération sur les chaines de caractère",
    style="Custom.TButton",
    compound=LEFT,
    command = ch.lancer_chaine
)


bouton9= ttk.Button(
    scrollable_frame,
    text="Quitter",
    style="Custom.TButton",
    compound=LEFT,
    command = fenetre.destroy
)

# Placement des boutons avec un espacement uniforme
bouton1.pack(pady=10, fill=X)
bouton2.pack(pady=10, fill=X)
bouton3.pack(pady=10, fill=X)
bouton4.pack(pady=10, fill=X)
bouton6.pack(pady=10, fill=X)
bouton8.pack(pady=10, fill=X)
bouton9.pack(pady=10, fill=X)

fenetre.mainloop()
from tkinter import *

def action() :
    lignes = int(input("Nombre de lignes :"))
    table = int(input("Table de :"))

    grille = []
    for i in range ((lignes*2)**2) :
        grille += [0]

    nb = 1
    pos = lignes*(lignes*2)+lignes-1
    l = 1
    if 1 % table == 0 :
        grille[pos] = 1
    while l <= lignes*2-4+(l%2) :
        for i in range (l) :
            pos -= lignes * 2
            nb += 1
            if nb % table == 0 :
                grille[pos] = 1

        for i in range (l) :
            pos += 1
            nb += 1
            if nb % table == 0 :
                grille[pos] = 1

        for i in range (l+1) :
            pos += lignes * 2
            nb += 1
            if nb % table == 0 :
                grille[pos] = 1

        for i in range (l+1) :
            pos -= 1
            nb += 1
            if nb % table == 0 :
                grille[pos] = 1

        l += 2

    for i in range (l) :
        pos -= lignes * 2
        nb += 1
        if nb % table == 0 :
            grille[pos] = 1

    for i in range (l) :
        pos += 1
        nb += 1
        if nb % table == 0 :
            grille[pos] = 1

    for i in range (l) :
        pos += lignes * 2
        nb += 1
        if nb % table == 0 :
            grille[pos] = 1

    for i in range (lignes*2) :
        for j in range (lignes*2) :
            if grille[i*(lignes*2)+j] == 1 :
                rec = canvas.create_rectangle(j*(500/(lignes*2)),i*(500/(lignes*2)),(j+1)*(500/(lignes*2)),(i+1)*(500/(lignes*2)),fill="black")

fenetre = Tk()

canvas = Canvas(fenetre,width=500,height=500,bg="white")
canvas.pack()

action()
b = 1
while b == 1 :
    a = 3
    while not a == 1 and not a == 2 :
        a = int(input("1) Recommencer avec d'autres valeurs 2) Quitter"))
    if a == 1 :
        print()
        canvas.delete('all')
        action()
    else :
        b = 0

fenetre.mainloop()
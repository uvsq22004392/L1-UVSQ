import tkinter as tk

global color

color = []
racine = tk.Tk()
canevas = tk.Canvas(racine, bg="white", height=600, width=600)
bouton = tk.Button(racine, text="Annuler", command=lambda:undo())

def undo():
    if canevas.type(color[-1]) == "oval": 
        canevas.delete(color[-1]) 
        del(color[-1]) 

def clique(event):
    if event.x < 50 and event.y < 50:
        cercle = canevas.create_oval((200, 300), (300, 400), fill="green")
        color.append(cercle)
    elif event.x > 50 and event.x <= 100 and event.y > 50 and event.y <= 100:
        cercle = canevas.create_oval((200, 300), (300, 400), fill="red")
        color.append(cercle)
    elif event.x > 100 and event.x <= 150 and event.y > 100 and event.y <= 150:
        cercle = canevas.create_oval((200, 300), (300, 400), fill="white")
        color.append(cercle)

    else:
        cercle = canevas.create_oval((200, 300), (300, 400), fill="red")
        color.append(cercle)



carre = canevas.create_rectangle(0, 0, 50, 50, fill="green")
carre1 = canevas.create_rectangle(50, 50, 100, 100, fill="red")
carre2 = canevas.create_rectangle(100, 100, 150, 150, fill="white")
cercle = canevas.create_oval((200, 300), (300, 400), fill="red")
canevas.bind("<Button-1>", clique)




canevas.grid(column = 1, row = 1)
bouton.grid(column = 0, row = 0)



racine.mainloop()
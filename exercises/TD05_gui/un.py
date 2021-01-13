import tkinter as tk

root = tk.Tk()
root.title("canevas")

canvas = tk.Canvas(root, bg="black", height=550, width=550)
canvas.grid(column=0, row=0)

restart_botton = tk.Button(root, text="Redemarrer", bd= 1, command=lambda: effacer())
restart_botton.grid(column=0, row=2)

canvas.create_line((0, 183,550,183), fill="white", width=5)
canvas.create_line(0,366,550,366 ,fill="white", width=5 )


def Clic (event):
    canvas.create_rectangle(event.x, event.y, event.x, event.y, fill = "red", outline = "red")

canvas = tk.Canvas(root, bg="red", bd = 5, height=0, width=0)
canvas.grid(column = 0, row = 0)
canvas.bind("<Button-1>", Clic) 
root.mainloop()
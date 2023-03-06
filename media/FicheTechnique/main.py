from tkinter import *
from PILOW import Image, ImageTk

class MainWindow:
    def __init__(self):
        self.page = Tk()
        self.page.title("Jeu  MemoryGame")
        self.page.geometry( '800x600' )
        self.page.configure(background="pink")
        image1 = Image.open("aline.jpg")
        test = ImageTk.PhotoImage(image1)
        self.label = Label(self.page,image=test,width=20,height=3, text="Memory Game", font=("Arial Bold", 30), fg='white', bg='pink')
        self.label.pack()
        self.label.place(x=180,y=50)

        self.bouton = Button(self.page,width=20,height=2, text="Play", bg="blue", fg="pink")
        self.bouton.pack()
        self.bouton.place(x=320,y=400)





m = MainWindow()
m.page.mainloop()
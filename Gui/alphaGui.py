import tkinter as tk
from PIL import Image, ImageTk
from tkinter.messagebox import showerror
import alpha

class alphaGui:

    def __init__(self):
        self.tag = ""
        self.win = tk.Tk()
        self.win.title("WallHaven Scrapper")

        inp = tk.Frame(master=self.win, highlightthickness=2, highlightbackground="black")
        tk.Label(master=inp, text="Enter tag to search").grid(row=0, column=0)
        self.btn = tk.Entry(master=inp, width=30)
        self.btn.grid(row=0, column=1)
        tk.Button(master=inp, bg="black", fg="white", text="Get It", command=self.get_tag).grid(row=0, column=2)
        inp.pack()

        self.main = tk.Frame(master=self.win)
        tk.Label(master=self.main, height=20, width=80, image=None).grid(row=0, column=0)
        self.main.pack()
        self.img = ""

        footer = tk.Frame(master=self.win)
        self.nxt = tk.Button(master=footer, bg="black", fg="white", text="Next Image", state="disabled", command=self.randomize_pic)
        self.nxt.grid(row=0, column=0)
        tk.Button(master=footer, bg="black", fg="white", text="Save and Exit", command=self.save_exit).grid(row=0, column=1)
        footer.pack()

        
        self.Obj = alpha.alpha()

        self.win.mainloop()
    

    def get_tag(self):
        self.tag = self.btn.get().replace(" ","+").lower()
        self.nxt['state'] = "normal"
        self.Obj.get_all_img(self.tag)
        self.randomize_pic()

    def randomize_pic(self):
        target = self.Obj.randomize_pic()
        if target == -1:
            showerror("WallHaven Scrapper","Error : Tag Not Found")
        else:
            self.Obj.get_img(target, self.tag)
            self.show_img()
    
    def show_img(self):
        path = self.tag + ".jpg"
        wall = Image.open(path).resize((600,400))
        self.img = ImageTk.PhotoImage(wall)
        tk.Label(master=self.main, image=self.img).grid(row=0, column=0)
    
    def save_exit(self):
        self.win.destroy()
        
myGui = alphaGui()
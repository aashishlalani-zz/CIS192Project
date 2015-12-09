from Tkinter import Tk, BOTH, StringVar
from ttk import Frame, Button, Style, Label, Entry
from send_emails import send_email

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("One Time Pad Generator")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        keyButton = Button(self, text="Generate Key",
            command=self.generateKey)
        keyButton.place(x=240, y=240)
      
        
    def generateKey(self):
        l1 = Label(self, text = "1249098")
        l1.place(x=10, y=10)
        entryfield = Entry(self, width=7, textvariable=StringVar())
        entryfield.place(x=100, y=300)

        quitButton = Button(self, text="Email",
        command=send_email)
        quitButton.place(x=50, y=50)

def main():
  
    root = Tk()
    root.geometry("500x500+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
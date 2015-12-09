import Tkinter 
from ttk import Frame, Button, Style, Label, Entry
from send_emails import send_email
import Cryptography
from Tkinter import StringVar
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, padding=(3,3,12,12))   
         
        self.parent = parent
        
        self.initUI()
        
    encrypted =""
    key = {}
    to = ""
    
    def initUI(self):
        self.parent.title("One Time Pad Generator")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=Tkinter.BOTH, expand=1)
        key = Label(self).place(x=0, y=40)
        encrypt = Label(self).place(x=0, y=150)
        keyButton = Button(self, text="Generate Key",
            command=self.createKey)
        keyButton.place(x=0, y=0)
        e = Entry(self)
        e.pack()

        e.delete(0, Tkinter.END)
        e.insert(0, "Send it via email")
        
        encode = Entry(self)
        encode.pack()

        encode.delete(0, Tkinter.END)
        encode.insert(0, "text you want to encrypt")
       
         
        encodeButt = Button(self, text="Encrypt",
            command=lambda: self.encrypt(encode.get()))
        encodeButt.place(x=0, y=100)
        email = Button(self, text="Send Email",command=lambda:self.sendmail(e.get()))
        email.place(x = 0, y = 80)
       
        
    def createKey(self):
        self.key = Cryptography.GenerateKey()
        print self.key[12]
        Label(self, text = self.key).place(x=0, y=40)
      
    def sendmail(self, to):
        key = "anvita here you go" + self.key.__str__()+ "heres encryption" + self.encrypted.__str__()
        command=send_email(key,to)
        
    def encrypt(self, string):
        self.encrypted = Cryptography.Encrypt(string, self.key)
        Label(self, text = self.encrypted).place(x=0, y=100)

def main():
  
    root = Tkinter.Tk()
    root.geometry("500x500+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
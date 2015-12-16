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
    decrypted = ""
    pad = ""
    
    def initUI(self):
        self.parent.title("One Time Pad Generator")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=Tkinter.BOTH, expand=1)
        key = Label(self).place(x=0, y=40)
        e = Entry(self)
        e.pack()

        e.delete(0, Tkinter.END)
        e.insert(0, "Send it via email")
        
        encode = Entry(self)
        encode.pack()

        encode.delete(0, Tkinter.END)
        encode.insert(0, "text you want to encrypt")
       
         
        encodeButton = Button(self, text="Encrypt",
            command=lambda: self.encrypt(encode.get()))
        encodeButton.place(x=0, y=100)
        email = Button(self, text="Send Email",command=lambda:self.sendmail(e.get()))
        email.place(x = 0, y = 80)

        decode = Entry(self)
        decode.pack()

        decode.delete(0, Tkinter.END)
        decode.insert(0, "text you want to decrypt")

        pad = Entry(self)
        pad.pack()

        pad.delete(0, Tkinter.END)
        pad.insert(0, "pad of text you want to decrypt")
       
         
        decodeButton = Button(self, text="decrypt",
            command=lambda: self.decrypt(decode.get(), pad.get()))
        decodeButton.place(x=0, y=130)

       
        

       
      
    def sendmail(self, to):
        key = "anvita here you go" + self.key.__str__()+ "heres encryption" + self.encrypted.__str__()
        command=send_email(key,to)
        
    def encrypt(self, string):
        self.key = Cryptography.GenerateKey(string)
        Label(self, text = self.key).place(x=0, y=40)
        self.encrypted = Cryptography.Encrypt(string, self.key)
        Label(self, text = self.encrypted).place(x=0, y=100)

    def decrypt(self, string, pad):
        self.decrypted = Cryptography.Decrypt(string, pad)
        Label(self, text = self.decrypt).place(x=0, y=150)

def main():
  
    root = Tkinter.Tk()
    root.geometry("500x500+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
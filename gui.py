import Tkinter 
from ttk import Frame, Button, Style, Label, Entry
from send_emails import send_email
import Cryptography
from Tkinter import Scrollbar
from matplotlib.sankey import RIGHT
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, padding=(3,3,12,12))   
        self.parent = parent
        self.encrypted=["", 0]
        self.initUI()
        self.T


    def initUI(self):
        self.parent.title("One Time Pad Generator")
        self.style = Style()
        self.style.theme_use("default")
        self.grid()
        
        #string
        text_to_encrypt = Entry(self)
        text_to_encrypt.grid(row=0, column=0)
        text_to_encrypt.delete(0, Tkinter.END)
        text_to_encrypt.insert(0, "text you want to encrypt or decrypt")
        
        #pad
        encrypt_pad = Entry(self)
        encrypt_pad.grid(row=0, column=1)
        encrypt_pad.delete(0, Tkinter.END)
        encrypt_pad.insert(0, "padOutput")
        
        #start
        start_encrypt = Entry(self)
        start_encrypt.grid(row=0, column=2)
        start_encrypt.delete(0, Tkinter.END)
        start_encrypt.insert(0, 0)
        
        
        
        
        #encrypt button
        encodeButton = Button(self, text="Encrypt",
            command=lambda: self.encrypt(text_to_encrypt.get(), encrypt_pad.get(), start_encrypt.get()))
        encodeButton.grid(row=1, column=0)
        #decrypt button
        encodeButton = Button(self, text="Decrypt",
            command=lambda: self.decrypt(str(text_to_encrypt.get()), encrypt_pad.get(), start_encrypt.get()))
        encodeButton.grid(row=1, column=2)
        
      
        #generate pad
        padgen = Entry(self)
        padgen.grid(row=2, column=0)
        padgen.delete(0, Tkinter.END)
        padgen.insert(0, 0)
        
        #gen key button
        genkey = Button(self, text="Generate Key",
                        command=lambda: Cryptography.outputPad(Cryptography.GenerateKey(int(padgen.get())), encrypt_pad.get()))
        genkey.grid(row=2, column=1)
        
        #encrypted text
       
        self.T = Tkinter.Text(self)
        S = Scrollbar(self.T)
        S.grid(column=2);
        S.config(command=self.T.yview)
        self.T.config(yscrollcommand=S.set)
        self.T.insert(Tkinter.END,self.encrypted[0])
        self.T.grid(row=5, column=0, sticky="nsew", rowspan = 10, columnspan = 3)
        
       
        #input email
        e = Entry(self)
        e.grid(row = 3, column = 0)
        e.delete(0, Tkinter.END)
        e.insert(0, "Send encrypted message via email")
        #send email
        email = Button(self, text="Send Email",command=lambda:self.sendmail(e.get()))
        email.grid(row=3, column=1)

       
      
    def sendmail(self, to):
        key = "Encrypted Message" + self.encrypted[0]
        send_email(key,to)
        
    def encrypt(self, string, pad, start):

        start = int(start)
        list_of_0_1 = Cryptography.inputPad(pad)
        self.encrypted = Cryptography.Encrypt(repr(string), list_of_0_1, start)
        print self.encrypted[0]
        self.T.delete(2.0, Tkinter.END)
        self.T.insert(Tkinter.END, self.encrypted[0])
        
    def decrypt(self, string, pad, start):
        start = int(start)
        list_of_0_1 = Cryptography.inputPad(pad)
        self.encrypted = Cryptography.Encrypt((string), list_of_0_1, start)
        print self.encrypted[0]
        self.T.delete(2.0, Tkinter.END)
        self.T.insert(Tkinter.END, self.encrypted[0])
     

def main():
  
    print (repr("hello"));
    root = Tkinter.Tk()
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
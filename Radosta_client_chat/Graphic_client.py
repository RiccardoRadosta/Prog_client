#--IMPORT
from tkinter import *

#--VARIABILI

#--FUNZIONI
def register():
    window.geometry("700x700")
    window.title("create account")

    mex = Label(window, text="\n\n\n\n\n\n\n\n\nCreazione del nuovo account:",font=("ocr a extended",16))
    mex2 = Label(window, text="\n- La lunghezza dell'username deve essere compresa\n tra 4 e 30 caratteri\n- La lunghezza della password deve essere compresa tra 6 e 30\n", font=("ocr a extended",13))
    mex.pack(anchor="center")
    mex2.pack(anchor="center")

    txtusername = Label(window, text="Username", font = ("Magneto",16))
    username = Entry(window, bd=5)
    txtusername.pack(anchor = "center")
    username.pack(anchor = "center")

    txtpassword = Label(window, text="Password", font = ("Magneto",16))
    password = Entry(window, bd=5)
    txtpassword.pack(anchor = "center")
    password.pack(anchor = "center")

#--MAIN
if __name__ == "__main__":
    window = Tk()
    window.wm_iconbitmap("favicon.ico")
    register()#prima registrazione paggina
    window.mainloop()

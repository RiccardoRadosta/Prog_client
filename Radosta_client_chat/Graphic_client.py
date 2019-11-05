#--IMPORT
from tkinter import *

#--VARIABILI
sicurezza = True

#--FUNZIONI
def verifica(password, confirmpassword, window):
    global sicurezza
    password = password.get()
    confirmpassword = confirmpassword.get()
    print("password= " + password + "\nConfirmPassword= " + confirmpassword)
    if password == confirmpassword:
        print("sono uguali")
        sicurezza = True
    else:
        print("non sono uguali")
        sicurezza = False

    if sicurezza == False:
        errorMessage = Label(window, text="Le due password inserite non corrispondono, riprovare", font=("ocr a extended", 14))
        errorMessage.pack(anchor="center")
def register():
    window.geometry("700x700")
    window.title("Create Account")

    mex = Label(window, text="\n\n\n\n\n\n\n\n\nCreazione del nuovo account:", font=("ocr a extended",16))
    mex2 = Label(window, text="\n- La lunghezza dell'username deve essere compresa\n tra 4 e 30 caratteri\n- La lunghezza della password deve essere compresa tra 6 e 30\n", font=("ocr a extended", 13))
    mex.pack(anchor="center")
    mex2.pack(anchor="center")

    txtusername = Label(window, text="Username", font=("Magneto", 16))
    username = Entry(window, bd=5)
    txtusername.pack(anchor="center")
    username.pack(anchor="center")

    txtpassword = Label(window, text="Password", font = ("Magneto", 16))
    password = Entry(window, bd=5)
    txtpassword.pack(anchor="center")
    password.pack(anchor="center")

    txtconfirmpassword = Label(window, text="Conferma Password", font=("Magneto", 16))
    confirmpassword = Entry(window, bd=5)
    txtconfirmpassword.pack(anchor="center")
    confirmpassword.pack(anchor="center")

    bottone = Button(window, text="    invia    ", command = lambda : verifica(password, confirmpassword, window))
    bottone.pack(anchor="center")

def login():
    window.geometry("700x700")
    window.title("Log in!")

    space1 = Label(window, text="\n\n\n\n\n\nLog in!:\n\n", font=("Verdana", 16))
    space1.pack(anchor="center")

    textuser = Label(window, text="Username", font=("Magneto", 16))
    user = Entry(window, bd=5)
    textuser.pack(anchor="center")
    user.pack(anchor="center")

    space2 = Label(window, text="\n")
    space2.pack(anchor="center")

    textpwd = Label(window, text="Password", font=("Magneto", 16))
    pwd = Entry(window, bd=5)
    textpwd.pack(anchor="center")
    pwd.pack(anchor="center")

    space3 = Label(window, text="\n")
    space3.pack(anchor="center")

    registration = Button(window, text="Non sei ancora registrato? Clicca qui!", foreground="blue", bd=5, width=30, height=1, relief=RIDGE, font=("Verdana ", 10, "underline" ) )
    registration.pack(anchor="center")


#--MAIN
if __name__ == "__main__":
    window = Tk()
    window.wm_iconbitmap("favicon.ico")
    register() #registration user
    #login() #login
    window.mainloop()

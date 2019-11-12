#--IMPORT
from tkinter import *
#from PIL import ImageTk, Image
from Radosta_client_chat import Client_TCP

#--VARIABILI
sicurezza = True

#--FUNZIONI
def verifica(username, password, confirmpassword, window):
    global sicurezza
    password = password.get()
    confirmpassword = confirmpassword.get()
    print("password= " + password + "\nConfirmPassword= " + confirmpassword)

    if len(username.get()) > 4 and len(username.get()) < 30:
        sicureMex1 = True
        if len(password) > 6 and len(password) < 30 :
            sicureMex2 = True

            if password == confirmpassword:
                print("Sono uguali!\n")
                sicureMex3 = True
                Client_TCP.registerclient(username.get(), password)
                recv = Client_TCP.mex_recv()
                if recv[0] == 0:
                    print("stiamo lavorando per voi")
                    # AGGIUNGERE IL COLLEGAMENTO CON LA FINIìESTRA DEI MESSAGGI
                else:
                    Message = Label(window, text="Utente già registrato con queste credenziali", font=("ocr a extended", 14))
                    Message.pack(anchor="center")
            else:
                print("Non sono uguali!\n")
                sicureMex3 = False

            if sicureMex3 == False:
                errorMessage = Label(window, text="Le due password inserite non corrispondono, riprovare", font=("ocr a extended", 12), foreground="red")
                errorMessage.pack(anchor="center")
        else:
            sicureMex2 = False

        if sicureMex2 == False:
            errorMessage = Label(window, text="La password non soddisfa i requisiti. Riprova!", font=("ocr a extended", 12), foreground="red")
            errorMessage.pack(anchor="center")
    else:
        sicureMex1 = False

    if sicureMex1 == False:
        errorMessage = Label(window, text="L'username non soddisfa i requisiti. Riprova!", font=("ocr a extended", 12), foreground="red")
        errorMessage.pack(anchor="center")

def register(window2):
    window2.destroy()
    window = Tk()
    window.wm_iconbitmap("favicon.ico")
    window.geometry("700x700")
    window.title("Create Account")

    mex = Label(window, text="\n\n\n\n\n\n\n\n\nCreazione del nuovo account:", font=("ocr a extended",16))
    mex2 = Label(window, text="\n- La lunghezza dell'username deve essere compresa\n tra 4 e 30 caratteri\n- La lunghezza della password deve essere compresa tra 6 e 30\n", font=("ocr a extended",13))
    mex.pack(anchor="center")
    mex2.pack(anchor="center")

    txtusername = Label(window, text="Username", font=("Magneto", 16))
    username = Entry(window, bd=5)
    txtusername.pack(anchor="center")
    username.pack(anchor="center")

    txtpassword = Label(window, text="Password", font=("Magneto", 16))
    password = Entry(window, bd=5)
    txtpassword.pack(anchor="center")
    password.pack(anchor="center")

    txtconfirmpassword = Label(window, text="Conferma Password", font=("Magneto", 16))
    confirmpassword = Entry(window, bd=5)
    txtconfirmpassword.pack(anchor="center")
    confirmpassword.pack(anchor="center")

    bottone = Button(window, text="Invia", width=10, height=1, relief=RIDGE, command=lambda: verifica(username, password, confirmpassword, window))
    bottone.pack(anchor="center")

    window.mainloop()

def graphic_login (username, password, window2):
    Client_TCP.login(username.get(), password.get())
    recv = Client_TCP.mex_recv()
    if recv[0] == 0:
        Message = Label(window2, text="Credenziali accettate", font=("ocr a extended", 14))
        Message.pack(anchor="center")
        message_interface(window2)
    else:
        Message = Label(window2, text="Credenziali NON accettate", font=("ocr a extended", 14))
        Message.pack(anchor="center")

def login():
    window2 = Tk()
    # image = Image.open("blue-space.jpg")
    # photo = ImageTk.PhotoImage(image)
    # w = Label(window2, image=photo)
    # w.place(x=0, y=0, relwidth=1, relheight=1)
    window2.wm_iconbitmap("favicon.ico")
    window2.geometry("700x700")
    window2.title("Log in!")

    space0 = Label(window2, text="\n")
    space0.pack(anchor="center")

    space1 = Label(window2, text="Log in!:", font=("Verdana", 16))
    space1.pack(anchor="center")

    textuser = Label(window2, text="Username", font=("Magneto", 16))
    user = Entry(window2, bd=5)
    textuser.pack(anchor="center")
    user.pack(anchor="center")

    space2 = Label(window2, text="\n")
    space2.pack(anchor="center")

    textpwd = Label(window2, text="Password", font=("Magneto", 16))
    pwd = Entry(window2, bd=5)
    textpwd.pack(anchor="center")
    pwd.pack(anchor="center")

    space3 = Label(window2, text="\n")
    space3.pack(anchor="center")

    bottone = Button(window2, text="Invia", width=5, height=1, relief=RIDGE, command=lambda: graphic_login(user, pwd, window2))
    bottone.pack(anchor="center")

    space4 = Label(window2, text="\n")
    space4.pack(anchor="center")

    registration = Button(window2, text="Non sei ancora registrato? Clicca qui!", foreground="blue", bd=5, width=30, height=1, relief=RIDGE, font=("Verdana ", 10, "underline"), command=lambda: register(window2))
    registration.pack(anchor="center")

    window2.mainloop()

def graphic_online_users(window3):
    Client_TCP.online_users()
    r = Client_TCP.mex_recv()
    Message = Label(window3, text=r, font=("ocr a extended", 14))
    Message.pack(anchor="center")

def message_interface(window2):
    window2.destroy()
    window3 = Tk()
    window3.wm_iconbitmap("favicon.ico")
    window3.geometry("700x700")
    window3.title("Interfaccia messaggi")
    graphic_online_users(window3)
    window3.mainloop()


#--MAIN
if __name__ == "__main__":
    login() #login
    print("a")

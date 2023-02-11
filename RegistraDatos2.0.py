from tkinter import *
import sqlite3
from tkinter import  messagebox
#Colors (gris #ccd6f6, azul (#0a192f) letras(#64ffda))

###########################(Iniciar bases de datos)###########################

def ConexionBBDD():

    miConexion= sqlite3.connect("BaseDatos")
    myCursor= miConexion.cursor()

    try:

        myCursor.execute('''
            CREATE TABLE USERDATOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(20),
            password VARCHAR(20),
            email VARCHAR(30))
            ''')
        messagebox.showinfo("Ventana Emergente", "Bases de datos creada")
    except:
        messagebox.showwarning("¡ATENCION!", "YA EXISTE UNA BASE DE DATOS")

###########################(Funcion Crear (CRUD))###########################

def crear():

    miConexion = sqlite3.connect("BaseDatos")
    myCursor = miConexion.cursor()

    DATOS=username.get(),password.get(),email.get()
    #DATOS =email.get(), password.get(), username.get()
    myCursor.execute("INSERT INTO USERDATOS VALUES(NULL,?,?,?)", (DATOS))

    miConexion.commit()
    messagebox.showinfo("BBDD", "Datos insertados con exito")


###########################(Funcion Leer (CRUD))###########################

def leer():

    miConexion = sqlite3.connect("BaseDatos")
    myCursor = miConexion.cursor()

    myCursor.execute("SELECT * FROM USERDATOS WHERE ID=" + ID.get())

    UsuarioLeer = myCursor.fetchall()

    for usuario in UsuarioLeer:
        ID.set(usuario[0])
        username.set(usuario[1])
        password.set(usuario[2])
        email.set(usuario[3])

    miConexion.commit()

###########################(Funcion Leer (CRUD))###########################


def actulizar():

    miConexion = sqlite3.connect("BaseDatos")
    myCursor = miConexion.cursor()

    DATOS= username.get(), password.get(), email.get()

    myCursor.execute("UPDATE USERDATOS SET username=?, password=? , email=? " + "WHERE ID=" + ID.get(), (DATOS))

    miConexion.commit()
    messagebox.showinfo("BBDD", "Base de datos actulizada")

###########################(Funcion Eliminar (CRUD))###########################

def eliminar():

    miConexion = sqlite3.connect("BaseDatos")
    myCursor = miConexion.cursor()

    myCursor.execute("DELETE FROM USERDATOS WHERE ID=" + ID.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con exito")


###########################(Borrar campos)###########################


def eliminaCampos():
    username.set("")
    password.set("")
    email.set("")
    ID.set("")

###########################(Boton salir)###########################


def appExit():

    valor=messagebox.askquestion("Exit", "¿Te gustaria salir de la aplicacion?")

    if valor=="yes":
        root.destroy()


root= Tk()

root.geometry("350x400")

root.title("  Register Users")
root.resizable(False,False)
#root.iconbitmap("joystick.ico")
root.config(background="#fdeecd")

###########################(Barra Menu)###########################

barraMenu= Menu(root)
root.config(menu=barraMenu, width=300, height=300)

ArchivoFiles= Menu(barraMenu, tearoff=0)
ArchivoFiles.add_command(label="Iniciar BBDD", command=ConexionBBDD)
ArchivoFiles.add_command(label="Salir", command=appExit)
barraMenu.add_cascade(label="Archivo", menu=ArchivoFiles)

CRUD = Menu(barraMenu, tearoff=0)

CRUD.add_command(label="Crear", command=crear)
CRUD.add_command(label="Leer", command=leer)
CRUD.add_command(label="Actulizar", command=actulizar)
CRUD.add_command(label="Eliminar", command=eliminar)
barraMenu.add_cascade(label="CRUD", menu=CRUD)

DeleteCampos= Menu(barraMenu, tearoff=0)
DeleteCampos.add_command(label="Eliminar campos", command=eliminaCampos)
barraMenu.add_cascade(label="Borrar", menu=DeleteCampos)

###########################(Barra Menu)###########################

#main_title= Label(text= "Python Registration Users", font=("Cambria", 19), fg="#64ffda", bg="green", width="350", height="1", pady=10)
main_title= Label(text="Python Registration Users ", font=("Cambria",15), bg="#d24858", fg="White", width="550", height="2",)
main_title.pack()
#ccd6f6         #56CD63
miFrame=Frame(root, width=250, height=350, background="#fdeecd")
miFrame.pack()
modulo1= Frame(root,width=30,height=50, background="#fdeecd", pady=15)
modulo1.pack()


#Ahora vamos a hacer que los datos introducidos se guarden en un lado

username= StringVar()
password= StringVar()
email= StringVar()
ID= StringVar()

user_entry= Entry(miFrame,textvariable=username, width= 24, justify="center", border="4")
user_entry.grid(row=0,column=1, pady=10)

password_entry= Entry(miFrame,textvariable=password, width= 24, show= "*", justify="center", border="4")
password_entry.grid(row=1,column=1, pady=10)

email_entry= Entry(miFrame,textvariable=email, width= 24, justify="center", border="4")
email_entry.grid(row=2, column=1, pady=10)

ID_entry= Entry(miFrame,textvariable=ID, width= 24, justify="center",border="4")
ID_entry.grid(row=3, column=1, pady=10)


nombre_Label=Label(miFrame, text="Username", font=("Cambria", 14), fg="white", border="1", bg="#ea8676", width=8)
nombre_Label.grid(row=0, column=0, sticky="e", padx=10, pady=15)

password_Label=Label(miFrame, text="Password", font=("Cambria", 14), fg="white", border="1", bg="#ea8676", width=8)
password_Label.grid(row=1, column=0, sticky="e", padx=10, pady=15)

email_Label=Label(miFrame, text="Email", font=("Cambria", 14), fg="White", border="1", bg="#ea8676", width=8)
email_Label.grid(row=2, column=0, sticky="e", padx=10, pady=15)

game_Label=Label(miFrame, text="ID", font=("Cambria", 14), fg="White", border="1", bg="#ea8676", width=8)
game_Label.grid(row=3, column=0, sticky="e", padx=10, pady=15)

#AGREGAMOS UN BOTON PARA ENVIAR LOS DATOS

submit_btn= Button(modulo1, text="Create", overrelief=RIDGE, width="5", height="1", bg="#d24858", font=("Cambria",15),fg="white", command=crear)
submit_btn.grid(row=4,column=1,padx=8)
submit_btn= Button(modulo1, text="Read", overrelief=RIDGE, width="5", height="1", bg="#d24858", font=("Cambria",15),fg="white", command=leer)
submit_btn.grid(row=4,column=2,padx=8)
submit_btn= Button(modulo1, text="Update", overrelief=RIDGE, width="5", height="1", bg="#d24858", font=("Cambria",15) ,fg="white", command=actulizar)
submit_btn.grid(row=4,column=3,padx=8)
submit_btn= Button(modulo1, text="Delete", overrelief=RIDGE, width="5", height="1", bg="#d24858", font=("Cambria",15), fg="white", command=eliminar)
submit_btn.grid(row=4,column=4,padx=8)

#Colors (gris #ccd6f6, azul (#0a192f) letras(#64ffda))


root.mainloop()
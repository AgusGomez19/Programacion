from tkinter import Tk, Label, Button, Entry, Frame, messagebox, mainloop
from PIL import Image, ImageTk
import tkinter as tk

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x700")
        self.ventana.title("Login")

        Fondo = "#88FFB4"

        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(bg=Fondo)
        self.frame_superior.pack(fill="both", expand=True)

        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.pack(fill="both", expand=True)
        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

        self.titulo = Label(self.frame_superior,
                            text="Login",
                            font=("Calisto MT", 36, "bold"),
                            bg=Fondo)
        self.titulo.pack(side="top", pady=20)

        try:
            self.img = Image.open("PYTHON-TKINDER/usuario.png") 
            self.img = self.img.resize((160, 170))
            self.render = ImageTk.PhotoImage(self.img)
            self.fondo = Label(self.frame_superior, image=self.render, bg=Fondo)
            self.fondo.pack()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

        
        self.username_label = Label(self.frame_inferior, text="Usuario", bg=Fondo)
        self.username_label.grid(row=0, column=0, pady=10)
        self.username_entry = Entry(self.frame_inferior)
        self.username_entry.grid(row=0, column=1, pady=10)

        self.password_label = Label(self.frame_inferior, text="Contraseña", bg=Fondo)
        self.password_label.grid(row=1, column=0, pady=10)
        self.password_entry = Entry(self.frame_inferior, show="*")
        self.password_entry.grid(row=1, column=1, pady=10)

        self.login_button = Button(self.frame_inferior, text="Iniciar sesión", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.ventana.mainloop()

    def login(self):
        usuario = self.username_entry.get()
        contraseña = self.password_entry.get()
        messagebox.showinfo("Información", f"Usuario: {usuario}\nContraseña: {contraseña}")

if __name__ == "__main__":
    app = Login()

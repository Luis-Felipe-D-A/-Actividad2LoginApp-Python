import tkinter as tk
import json
from tkinter import messagebox, ttk
import webbrowser
from formularios.forms_usuarios import *
import util.generic as utl
from formularios.Login import *

class PAdmin(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        self.tipo_action ="Guardar"
        self.tipo_user = ""
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)  
        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Administracion de Usuarios", command=self.main_usuarios)  
        menubar.add_cascade(label="Usuarios", menu=menuuser)

        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Administracion de Clientes", command=self.main_clientes)  
        menubar.add_cascade(label="Clientes", menu=menuuser)

        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Administracion de Categorias", command=self.main_categorias)  
        menubar.add_cascade(label="Categorias", menu=menuuser)

        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Administracion de Productos", command=self.main_productos)  
        menubar.add_cascade(label="Productos", menu=menuuser)

        menuuser = tk.Menu(menubar, tearoff=0)  
        menuuser.add_command(label="Administracion de Ventas", command=self.main_ventas)  
        menubar.add_cascade(label="Ventas", menu=menuuser)

        self.config(menu=menubar)

        #frame user_info
        self.user_info = tk.Frame(self, bd=0, relief=tk.SOLID, width=200)
        self.user_info.pack(side=tk.LEFT,padx=4,pady=5, fill="y")
        titulo = tk.Label(self.user_info, text="PANEL ADMINISTRATIVO", font=('Arial',25))
        titulo.pack(padx=20, pady=4)
        
        self.userimg = utl.leer_imagen("imagenes/userinfo.png", (128,128))
        self.imgfacebook = utl.leer_imagen("imagenes/face.png",(48,48))
        self.imglinkedin = utl.leer_imagen("imagenes/linkedin.png", (48,48))
        self.imgwebsite = utl.leer_imagen("imagenes/website.png", (48,48))
        self.imglogout = utl.leer_imagen("imagenes/logout.png", (48,48))

        tk.Label(self.user_info, image=self.userimg).pack(padx=30, pady=4)
        tk.Label(self.user_info, text=self.name, font=('Arial',15)).pack(pady=4)
        tk.Label(self.user_info, text=self.email, font=('Arial',12)).pack(pady=2)

        tk.Button(self.user_info, image=self.imgfacebook, command=self.abrirfacebook, pady=4).place(x=100, y=300)
        tk.Button(self.user_info, image=self.imglinkedin, command=self.abrirlinkedin, pady=4).place(x=150, y=300)
        tk.Button(self.user_info, image=self.imgwebsite, command=self.abrirwebsite, pady=4).place(x=200, y=300)
        tk.Button(self.user_info, image=self.imglogout, command=self.logout).place(x=250, y=300)

        #Frame_Data
        self.frame_data = tk.Frame(self, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

        tk.Label(self.frame_data, text="BIENVENIDOS AL SISTEMA", font=('Arial', 20)).pack(padx=20, pady=4)

        #Frame_Dynamic
        self.frame_dynamic = tk.Frame(self.frame_data, bd=0, relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_dynamic.pack(side=tk.RIGHT,padx=4, pady=5, fill="both", expand=1)
        tk.Label(self.frame_dynamic, text="Frame Dinamico", font=('Arial', 20)).pack(padx=20, pady=4)


    def abrirfacebook(self):
        url= "https://www.facebook.com"
        webbrowser.open_new_tab(url)
    def abrirlinkedin(self):
        url= "https://www.linkedin.com"
        webbrowser.open_new_tab(url)
    def abrirwebsite(self):
        url= "http://www.itcloud.com.co"
        webbrowser.open_new_tab(url)
    def logout(self):
        self.destroy()

    def main_usuarios(self):
        self.limpiar_panel(self.frame_dynamic)
        FormUsuarios(self.frame_dynamic)

    def limpiar_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()
        
    def main_clientes(self):
        pass
    def main_categorias(self):
        pass
    def main_productos(self):
        pass
    def main_ventas(self):
        pass
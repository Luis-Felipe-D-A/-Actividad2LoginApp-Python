import json
import tkinter as tk
from tkinter import ttk, messagebox

class FormUsuarios(tk.Tk):
    def __init__(self, parent):
        self.tipo_action = "Guardar"
        self.tipo_user = ""
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self.frame, text="Registro de usuarios", font=('Times', 16)).place(x=70, y=30)

        labelid = tk.Label(self.frame, text="ID", font=('Times', 14))  
        labelid.place(x=70, y=100)  
        self.cid = tk.Entry(self.frame, width=40)  
        self.cid.place(x=220, y=100)  

        labelnombre = tk.Label(self.frame, text="Nombre", font=('Times', 14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame, text="Username", font=('Times', 14))
        labelusuario.place(x=70, y=160)
        self.cusuario = tk.Entry(self.frame, width=40)
        self.cusuario.place(x=220, y=160)

        labelcontrasena = tk.Label(self.frame, text="Contraseña", font=('Times', 14))
        labelcontrasena.place(x=500, y=100)
        self.ccontrasena = tk.Entry(self.frame, width=40, show="*")
        self.ccontrasena.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame, text="Correo", font=('Times', 14))
        labelcorreo.place(x=500, y=130)
        self.ccorreo = tk.Entry(self.frame, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame, text="Rol", font=('Times', 14))
        labeltipo.place(x=500, y=160)
        self.ctipo = ttk.Combobox(self.frame, width=40)
        self.ctipo.place(x=600, y=160)
        self.ctipo["values"] = ("Administrador", "Vendedor")

        btn_guardar = tk.Button(self.frame, text="Guardar", font=('Times', 14), command=self.guardar_usuario)
        btn_guardar.place(x=70, y=190)

        
        btnActualizar = tk.Button(self.frame, text="Actualizar", font=('Times', 14), command=self.actualizar_usuarios)
        btnActualizar.place(x=170, y=190)

        btnEliminar = tk.Button(self.frame, text="Eliminar", font=('Times', 14), command=self.eliminar_usuarios)
        btnEliminar.place(x=270, y=190)

        self.listar_usuarios()

    def listar_usuarios(self):
        tk.Label(self.frame, text="LISTADO DE USUARIOS", font=('Times', 16)).place(x=70, y=230)

        self.tablausuarios = ttk.Treeview(self.frame, columns=("Nombre", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="ID")  
        self.tablausuarios.heading("Nombre", text="Nombre")
        self.tablausuarios.heading("Username", text="Username")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")
        
        with open("db_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for usuarios in data["users"]:
                self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}', values=(f'{usuarios["name"]}', f'{usuarios["username"]}', f'{usuarios["email"]}', f'{usuarios["role"]}'))

        self.tablausuarios.place(x=70, y=280)
        self.cargar_usuarios()

        self.tablausuarios.place(x=70, y=280)

    def cargar_usuarios(self):
        self.tablausuarios.delete(*self.tablausuarios.get_children())
        with open("db_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            for usuarios in data["users"]:
                self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}', values=(f'{usuarios["name"]}', f'{usuarios["username"]}', f'{usuarios["email"]}', f'{usuarios["role"]}'))

    def guardar_usuario(self):
        nuevo_usuario = {
            "id": self.cid.get(),
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }
        
        with open("db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["users"].append(nuevo_usuario)
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.truncate()
        
        messagebox.showinfo( "Usuario guardado correctamente")
        self.limpiar_campos()
        self.cargar_usuarios()

    def actualizar_usuarios(self):
        seleccion = self.tablausuarios.selection()
        if not seleccion:
            messagebox.showerror( "Por favor, seleccione un usuario para actualizar")
            return

        item = self.tablausuarios.item(seleccion)
        id_usuario = item['text']

        usuario_actualizado = {
            "id": self.cid.get(),
            "name": self.cnombre.get(),
            "username": self.cusuario.get(),
            "password": self.ccontrasena.get(),
            "email": self.ccorreo.get(),
            "role": self.ctipo.get()
        }

        with open("db_users.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            for i, usuario in enumerate(data["users"]):
                if usuario["id"] == id_usuario:
                    data["users"][i] = usuario_actualizado
                    break
            file.seek(0)
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.truncate()

        messagebox.showinfo( "Usuario actualizado correctamente")
        self.limpiar_campos()
        self.cargar_usuarios()

    def eliminar_usuarios(self):
        seleccion = self.tablausuarios.selection()
        if not seleccion:
            messagebox.showerror("Por favor, seleccione un usuario para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este usuario?"):
            item = self.tablausuarios.item(seleccion)
            id_usuario = item['text']

            with open("db_users.json", "r+", encoding="utf-8") as file:
                data = json.load(file)
                data["users"] = [usuario for usuario in data["users"] if usuario["id"] != id_usuario]
                file.seek(0)
                json.dump(data, file, indent=4, ensure_ascii=False)
                file.truncate()

            messagebox.showinfo( "Usuario eliminado correctamente")
            self.limpiar_campos()
            self.cargar_usuarios()

    def limpiar_campos(self):
        campos = [self.cid, self.cnombre, self.cusuario, self.ccontrasena, self.ccorreo]
        
        
        for campo in campos:
            campo.delete(0, tk.END)
        
        self.ctipo.set('')

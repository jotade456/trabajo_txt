import tkinter as Ventana
from tkinter import messagebox,simpledialog

class Vista:
    def __init__(self,controlador):
        self.ventana = Ventana.Tk()
        self.ventana.title("Crear Archivo")
        self.ventana.geometry("380x250")
        self.ventana.configure(bg="#f0f0f0")
        self.objControlador=controlador

        self.label_style = {"bg": "#f0f0f0"}
        self.entry_style = {"font": "Helvetica"}

        
        self.label_mensaje = Ventana.Label(self.ventana, text="Mensaje del archivo:", **self.label_style)
        self.label_mensaje.grid(row=0, column=0, pady=10, padx=10)

        self.entry_mensaje = Ventana.Entry(self.ventana, **self.entry_style)
        self.entry_mensaje.grid(row=0, column=1, pady=10, padx=10)

        self.label_nombre = Ventana.Label(self.ventana, text="Nombre del archivo:", **self.label_style)
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)

        self.entry_nombre = Ventana.Entry(self.ventana, **self.entry_style)
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        self.boton_crear = Ventana.Button(self.ventana, text="Crear", command=self.agregar_dato)
        self.boton_crear.grid(row=2, column=0, columnspan=2, pady=20, padx=10)

        self.boton_ver = Ventana.Button(self.ventana, text="Ver datos", command=self.leer_deserializado)
        self.boton_ver.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

    def agregar_dato(self):
        mensaje_archivo = self.entry_mensaje.get()
        nombre_archivo = self.entry_nombre.get()
        if nombre_archivo and mensaje_archivo:
            self.entry_mensaje.delete(0, Ventana.END)
            self.entry_nombre.delete(0, Ventana.END)
            self.objControlador.guardarDatos(mensaje_archivo,nombre_archivo)
            messagebox.showinfo("Información", "Archivo creado con éxito!")
            
        else:
            messagebox.showwarning("Advertencia", "Ambos campos son obligatorios.")
    
    def leer_deserializado(self):
        datoArchivo=simpledialog.askstring("Digitar","Digite nombre del archivo")
        if datoArchivo:
            texto=self.objControlador.deserializar(datoArchivo)
            messagebox.showinfo("Contenido del archivo",texto )
        
    
    def iniciar(self):
        self.ventana.mainloop()
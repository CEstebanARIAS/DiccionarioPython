import tkinter as tk
from tkinter import ttk
from View.temas import variables_view, bucles_view, condicionales_view, funciones_view,listas_view

class MainView(tk.Tk):
    def __init__(self, user_name):
        super().__init__()

        self.title("AprendePython")
        self.geometry("800x600")

        # Barra de navegación (menú superior)
        self.create_menu(user_name)

        # Breadcrumbs inicial (solo mostrando Inicio)
        self.breadcrumbs_var = tk.StringVar()
        self.breadcrumbs_var.set("Inicio")
        self.breadcrumbs_label = tk.Label(self, textvariable=self.breadcrumbs_var, font=("Arial", 10))

        # Colocar las migas de pan (breadcrumbs) antes del contenido
        self.breadcrumbs_label.pack(anchor="w", padx=10, pady=5)

        # Creación del frame principal donde se mostrarán los temas
        self.contenido_frame = ttk.Frame(self)
        self.contenido_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Contenido inicial
        self.mostrar_inicio()

    def create_menu(self, user_name):
        # Barra de navegación superior
        menubar = tk.Menu(self)

        # Menú "Temas"
        temas_menu = tk.Menu(menubar, tearoff=0)
        

        temas_menu.add_command(label="Inicio", command=lambda: self.mostrar_inicio())
        temas_menu.add_command(label="Variables", command=lambda: self.mostrar_tema("Variables", variables_view.mostrar_contenido_variables))
        temas_menu.add_command(label="Condicionales", command=lambda: self.mostrar_tema("Condicionales", mostrar_contenido_condicionales))
        temas_menu.add_command(label="Bucles", command=lambda: self.mostrar_tema("Bucles", bucles_view.mostrar_contenido_bucles))
        temas_menu.add_command(label="Funciones", command=lambda: self.mostrar_tema("Funciones", mostrar_contenido_funciones))
        temas_menu.add_command(label="Listas", command=lambda: self.mostrar_tema("Listas", mostrar_contenido_listas))
        menubar.add_cascade(label="Temas", menu=temas_menu)

        # Menú de usuario
        usuario_menu = tk.Menu(menubar, tearoff=0)
        usuario_menu.add_command(label="Configurar perfil")
        usuario_menu.add_separator()
        usuario_menu.add_command(label="Cerrar sesión")
        menubar.add_cascade(label=user_name, menu=usuario_menu)

        # Añadir la barra de menús a la ventana
        self.config(menu=menubar)

    def mostrar_inicio(self):
        """Muestra el contenido de inicio"""
        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

        label_inicio = tk.Label(self.contenido_frame, text="Bienvenido a AprendePython", font=("Arial", 16))
        label_inicio.pack(pady=20)

    def mostrar_tema(self, tema, mostrar_contenido_func):
        """Muestra el contenido del tema seleccionado y actualiza las migas de pan"""
        self.actualizar_breadcrumbs(tema)

        # Limpiar el frame de contenido antes de agregar nuevo contenido
        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

        # Llamar a la función que muestra el contenido específico del tema
        mostrar_contenido_func(self.contenido_frame)

    def actualizar_breadcrumbs(self, tema):
        """Actualiza las migas de pan según el tema seleccionado"""
        self.breadcrumbs_var.set(f"Inicio > {tema}")

# Ejecutar la ventana principal
if __name__ == "__main__":
    app = MainView("Usuario")
    app.mainloop()

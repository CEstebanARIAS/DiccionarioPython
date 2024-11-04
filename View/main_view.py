import tkinter as tk
from tkinter import ttk
from View.temas import variables_view, bucles_view, condicionales_view, funciones_view, listas_view
from Utils.progresTracker_utils import ProgressTracker
from View.configuser_view import ConfigUserView

class MainView(tk.Tk):
    def __init__(self, user_name):
        super().__init__()

        self.title("AprendePython")

        # Crear instancia de ProgressTracker para manejar el progreso
        self.progress_tracker = ProgressTracker()

        # Barra de navegación (menú superior)
        self.create_menu(user_name)

        # Breadcrumbs y progreso
        self.breadcrumbs_var = tk.StringVar()
        self.breadcrumbs_var.set("Inicio")

        # Etiqueta de progreso
        self.progreso_var = tk.StringVar()
        self.progreso_var.set(f"Progreso: {self.progress_tracker.obtener_progreso()}%")

        # Layout para Breadcrumbs y Progreso
        self.header_frame = ttk.Frame(self)
        self.header_frame.pack(fill="x", padx=10, pady=5)

        self.breadcrumbs_label = tk.Label(self.header_frame, textvariable=self.breadcrumbs_var, font=("Arial", 10))
        self.breadcrumbs_label.pack(side="left")

        self.progreso_label = tk.Label(self.header_frame, textvariable=self.progreso_var, font=("Arial", 10))
        self.progreso_label.pack(side="right")

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
        temas_menu.add_command(label="Variables", command=lambda: self.completar_tema("Variables", variables_view.mostrar_contenido_variables))
        temas_menu.add_command(label="Condicionales", command=lambda: self.completar_tema("Condicionales", condicionales_view.mostrar_contenido_condicionales))
        temas_menu.add_command(label="Bucles", command=lambda: self.completar_tema("Bucles", bucles_view.mostrar_contenido_bucles))
        temas_menu.add_command(label="Funciones", command=lambda: self.completar_tema("Funciones", funciones_view.mostrar_contenido_funciones))
        temas_menu.add_command(label="Listas", command=lambda: self.completar_tema("Listas", listas_view.mostrar_contenido_listas))
        menubar.add_cascade(label="Temas", menu=temas_menu)

        # Menú de usuario
        usuario_menu = tk.Menu(menubar, tearoff=0)
        usuario_menu.add_command(label="Configurar perfil", command=lambda: ConfigUserView(user_name))
        usuario_menu.add_separator()
        usuario_menu.add_command(label="Cerrar sesión", command=self.cerrar_sesion)
        menubar.add_cascade(label=user_name, menu=usuario_menu)

        # Añadir la barra de menús a la ventana
        self.config(menu=menubar)

    def cerrar_sesion(self):
        from View import login_view
        self.destroy()
        login_view.LoginWindow().mainloop()

    def mostrar_inicio(self):
        """Muestra el contenido de inicio"""
        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

        label_inicio = tk.Label(self.contenido_frame, text="Bienvenido a AprendePython", font=("Arial", 16))
        label_inicio.pack(pady=20)

        # Ajuste automático al contenido
        self.update_idletasks()  # Fuerza el recalculo del tamaño
        self.geometry("")  # Permite que tkinter ajuste el tamaño automáticamente

    def completar_tema(self, tema, mostrar_contenido_func):
        """Llama a ProgressTracker para actualizar el progreso y muestra el tema seleccionado"""
        nuevo_progreso = self.progress_tracker.completar_tema(tema)
        self.progreso_var.set(f"Progreso: {nuevo_progreso}%")  # Actualiza la visualización del progreso
        self.mostrar_tema(tema, mostrar_contenido_func)

    def mostrar_tema(self, tema, mostrar_contenido_func):
        """Muestra el contenido del tema seleccionado y actualiza las migas de pan"""
        self.actualizar_breadcrumbs(tema)

        # Limpiar el frame de contenido antes de agregar nuevo contenido
        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

        # Llamar a la función que muestra el contenido específico del tema
        mostrar_contenido_func(self.contenido_frame)

        # Ajuste automático al contenido
        self.update_idletasks()  # Fuerza el recalculo del tamaño
        self.geometry("")  # Permite que tkinter ajuste el tamaño automáticamente

    def actualizar_breadcrumbs(self, tema):
        """Actualiza las migas de pan según el tema seleccionado"""
        self.breadcrumbs_var.set(f"Inicio > {tema}")

# Ejecutar la ventana principal
if __name__ == "__main__":
    app = MainView("Usuario")
    app.mainloop()

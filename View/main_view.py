import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from View.temas import variables_view, bucles_view, condicionales_view, funciones_view, listas_view
from Utils.progresTracker_utils import ProgressTracker
from View.configuser_view import ConfigUserView

class MainView(tk.Tk):
    def __init__(self, user_name):
        super().__init__()

        self.title("AprendePython")
       
        self.configure(bg="#ffffff")  # Fondo blanco para la ventana principal

        # Crear instancia de ProgressTracker para manejar el progreso
        self.progress_tracker = ProgressTracker()

        # Crear el encabezado principal
        self.create_header(user_name)

        # Creación del frame principal donde se mostrarán los temas
        self.contenido_frame = ttk.Frame(self, padding=(20, 10), style="Contenido.TFrame")
        self.contenido_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Permitir que la ventana se ajuste automáticamente al contenido
        self.update_idletasks()  # Asegura que el contenido inicial esté cargado
        self.geometry("")  # Elimina el tamaño fijo, ajustándose al contenido
        self.resizable(True, True)  # Permite que la ventana sea redimensionable

        # Contenido inicial
        self.mostrar_inicio()

    def create_header(self, user_name):
        # Encabezado con bienvenida y progreso
        header_frame = tk.Frame(self, bg="#ffffff")  # Fondo blanco para el encabezado
        header_frame.pack(fill="x", pady=(0, 20))

        # Breadcrumbs y progreso
        self.breadcrumbs_var = tk.StringVar(value="Inicio")
        self.progreso_var = tk.StringVar(value=f"Progreso: {self.progress_tracker.obtener_progreso()}%")

        breadcrumbs_label = tk.Label(header_frame, textvariable=self.breadcrumbs_var, font=("Arial", 10), fg="#002c77", bg="#ffffff")
        progreso_label = tk.Label(header_frame, textvariable=self.progreso_var, font=("Arial", 10), fg="#002c77", bg="#ffffff")

        breadcrumbs_label.pack(side="left", padx=(0, 20))
        progreso_label.pack(side="right", padx=(0, 20))

        # Barra de navegación (menú superior)
        self.create_menu(user_name)

    def create_menu(self, user_name):
        # Barra de navegación superior
        menubar = tk.Menu(self)

        # Menú "Temas"
        temas_menu = tk.Menu(menubar, tearoff=0)
        temas_menu.add_command(label="Inicio", command=self.mostrar_inicio)
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
        """Muestra el contenido de inicio con el texto a la izquierda y la imagen a la derecha"""
        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

        # Crear un Frame para el contenido de bienvenida y organizar el texto y la imagen
        welcome_content_frame = tk.Frame(self.contenido_frame, bg="#ffffff")
        welcome_content_frame.pack(fill="both", expand=True)

        # Frame para el texto
        text_frame = tk.Frame(welcome_content_frame, bg="#ffffff")
        text_frame.pack(side="left", fill="both", expand=True)

        # Texto de bienvenida
        texto_titulo = tk.Label(
            text_frame, 
            text="\nBienvenido al sistema de aprendizaje para Python", 
            font=("Arial", 14, "bold"), 
            fg="#002c77",
            bg="#ffffff"
        )
        texto_titulo.pack(anchor="center", pady=(20, 10))

        texto_descripcion = tk.Label(
            text_frame,
            text="\nTu sistema de aprendizaje interactivo de Python.\nExplora temas desde variables hasta listas.",
            font=("Arial", 13),
            fg="#333333",
            bg="#ffffff"
        )
        texto_descripcion.pack(anchor="center", pady=(20,10))

        texto_bienvenida = tk.Label(
            text_frame,
            text="\nComienza a aprender con lecciones prácticas y adquiere habilidades en Python.\nCada tema te guiará paso a paso.",
            font=("Arial", 13),
            fg="#333333",
            bg="#ffffff",
            wraplength=400
        )
        texto_bienvenida.pack(anchor="center", pady=(20, 10))

        # Frame para la imagen
        image_frame = tk.Frame(welcome_content_frame, bg="#ffffff")
        image_frame.pack(side="right", fill="both", expand=True)

        # Espacio para la imagen
        try:
            image_path = "images/Main.jpg"  # Ruta de la imagen que subiste
            image = Image.open(image_path)
            image = image.resize((350, 300), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(image_frame, image=photo, bg="#ffffff")
            image_label.image = photo
            image_label.pack(anchor="e", padx=50)
        except Exception as e:
            print(f"No se pudo cargar la imagen: {e}")

    def completar_tema(self, tema, mostrar_contenido_func):
        """Llama a ProgressTracker para actualizar el progreso y muestra el tema seleccionado"""
        nuevo_progreso = self.progress_tracker.completar_tema(tema)
        self.progreso_var.set(f"Progreso: {nuevo_progreso}%")
        self.mostrar_tema(tema, mostrar_contenido_func)

    def mostrar_tema(self, tema, mostrar_contenido_func):
        """Muestra el contenido del tema seleccionado y actualiza las migas de pan"""
        self.actualizar_breadcrumbs(tema)


        for widget in self.contenido_frame.winfo_children():
            widget.destroy()

    
        mostrar_contenido_func(self.contenido_frame)

    
    
    def actualizar_breadcrumbs(self, tema):
        """Actualiza las migas de pan según el tema seleccionado"""
        self.breadcrumbs_var.set(f"Inicio > {tema}")

# Ejecutar la ventana principal
if __name__ == "__main__":
    app = MainView("Usuario")
    app.mainloop()

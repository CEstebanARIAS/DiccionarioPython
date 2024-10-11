import tkinter as tk
from tkinter import ttk


# Funciones para mostrar contenido adicional
def mostrar_contenido_condicionales(frame):
    contenido = """
    En Python, las estructuras condicionales permiten tomar decisiones basadas en condiciones.
    Las palabras clave principales son: if, elif, else.
    
    Ejemplo:
    edad = 20
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
    """
    label = tk.Label(frame, text=contenido, font=("Arial", 12), justify="left")
    label.pack(pady=10)

def mostrar_contenido_bucles(frame):
    contenido = """
    Los bucles permiten ejecutar un bloque de código repetidamente. En Python, se utilizan las estructuras for y while.
    
    Ejemplo de bucle for:
    for i in range(5):
        print(i)
    
    Ejemplo de bucle while:
    contador = 0
    while contador < 5:
        print(contador)
        contador += 1
    """
    label = tk.Label(frame, text=contenido, font=("Arial", 12), justify="left")
    label.pack(pady=10)

def mostrar_contenido_funciones(frame):
    contenido = """
    Las funciones permiten agrupar código en bloques reutilizables. 
    Para definir una función en Python, se usa la palabra clave def.
    
    Ejemplo:
    def saludar(nombre):
        return f"Hola, {nombre}"
    
    print(saludar("Ana"))
    """
    label = tk.Label(frame, text=contenido, font=("Arial", 12), justify="left")
    label.pack(pady=10)

def mostrar_contenido_listas(frame):
    contenido = """
    Las listas son colecciones que permiten almacenar múltiples valores.
    Puedes agregar, eliminar o modificar elementos en una lista.
    
    Ejemplo:
    lista = [1, 2, 3, 4, 5]
    lista.append(6)  # Añadir un elemento
    lista.remove(3)  # Eliminar un elemento
    print(lista)
    """
    label = tk.Label(frame, text=contenido, font=("Arial", 12), justify="left")
    label.pack(pady=10)

def mostrar_contenido_variables(parent_frame):
    """Muestra el contenido del tema Variables en el frame principal"""

    # Título del tema
    tk.Label(parent_frame, text="Variables en Python", font=("Arial", 16, "bold")).pack(pady=10)

    # Descripción del tema
    descripcion = (
        "En Python, una variable se utiliza para almacenar información y puede cambiar su valor durante la ejecución del programa. "
        "No es necesario declarar el tipo de dato de la variable explícitamente, ya que Python lo infiere según el valor que se le asigne. "
        "Aquí hay un ejemplo:\n\n"
        "x = 5  # Asigna el valor 5 a la variable 'x'\n"
        "nombre = 'Juan'  # Asigna una cadena de texto a la variable 'nombre'\n"
        "pi = 3.1416  # Asigna un número decimal a la variable 'pi'\n\n"
        "Las variables en Python son dinámicas y no requieren una declaración previa con su tipo."
    )
    tk.Label(parent_frame, text=descripcion, wraplength=550, justify="left").pack(pady=10)

    # Ejemplo de aplicación
    ejemplo_codigo = (
        "Ejemplo de uso:\n"
        "a = 10\n"
        "b = 20\n"
        "resultado = a + b\n"
        "print(f'La suma de {{a}} y {{b}} es {{resultado}}')"
    )
    tk.Label(parent_frame, text=ejemplo_codigo, font=("Courier", 10), justify="left").pack(pady=10)

    # Formulario de selección múltiple
    quiz(parent_frame)

def quiz(parent_frame):
    """Formulario de selección múltiple para el tema Variables"""
    # Pregunta del formulario
    tk.Label(parent_frame, text="¿Cuál de las siguientes es una declaración válida de una variable en Python?", font=("Arial", 12)).pack(pady=10)

    # Opciones
    var = tk.StringVar()

    opciones = [
        ("x == 10", "incorrecto"),
        ("x = 10", "correcto"),
        ("x := 10", "incorrecto"),
        ("10 = x", "incorrecto")
    ]

    for texto, valor in opciones:
        tk.Radiobutton(parent_frame, text=texto, variable=var, value=valor).pack(anchor="w")

    # Botón para enviar respuesta
    tk.Button(parent_frame, text="Enviar respuesta", command=lambda: verificar_respuesta(var)).pack(pady=10)

def verificar_respuesta(var):
    """Verifica si la respuesta del cuestionario es correcta"""
    if var.get() == "correcto":
        tk.messagebox.showinfo("Resultado", "¡Correcto! La asignación de variables en Python es 'x = valor'.")
    else:
        tk.messagebox.showwarning("Resultado", "Incorrecto. La respuesta correcta es 'x = valor'.")

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
        temas_menu.add_command(label="Variables", command=lambda: self.mostrar_tema("Variables", mostrar_contenido_variables))
        temas_menu.add_command(label="Condicionales", command=lambda: self.mostrar_tema("Condicionales", mostrar_contenido_condicionales))
        temas_menu.add_command(label="Bucles", command=lambda: self.mostrar_tema("Bucles", mostrar_contenido_bucles))
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

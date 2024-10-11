import tkinter as tk
from tkinter import messagebox

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
        ("1. x == 10", "incorrecto"),
        ("2. x = 10", "correcto"),
        ("3. x := 10", "incorrecto"),
        ("4. 10 = x", "incorrecto")
    ]

    for texto, valor in opciones:
        tk.Radiobutton(parent_frame, text=texto, variable=var, value=valor).pack(anchor="w")

    # Botón para enviar respuesta
    tk.Button(parent_frame, text="Enviar respuesta", command=lambda: verificar_respuesta(var)).pack(pady=10)

def verificar_respuesta(var):
    """Verifica si la respuesta del cuestionario es correcta"""
    if var.get() == "correcto":
        messagebox.showinfo("Resultado", "¡Correcto! La asignación de variables en Python es 'x = valor'.")
    else:
        messagebox.showwarning("Resultado", "Incorrecto. La respuesta correcta es 'x = valor'.")

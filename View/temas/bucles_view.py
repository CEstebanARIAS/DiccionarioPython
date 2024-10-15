import tkinter as tk
from tkinter import messagebox

def mostrar_contenido_bucles(parent_frame):
    """Muestra el contenido del tema Bucles en el frame principal"""

    # Título del tema
    tk.Label(parent_frame, text="Bucles en Python", font=("Arial", 16, "bold")).pack(pady=10)

    # Descripción del tema
    descripcion = (
        "Los bucles permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición o durante un rango definido de veces.\n"
        "En Python, existen dos tipos principales de bucles: `for` y `while`.\n\n"
        "El bucle `for` se utiliza para iterar sobre una secuencia de elementos, como una lista, tupla o cadena de texto.\n\n"
        "El bucle `while` ejecuta el bloque de código siempre que la condición especificada sea verdadera."
    )
    tk.Label(parent_frame, text=descripcion, wraplength=550, justify="left").pack(pady=10)

    # Ejemplo de bucle for
    ejemplo_for = (
        "Ejemplo de bucle `for`:\n"
        "numeros = [1, 2, 3, 4, 5]\n"
        "for num in numeros:\n"
        "    print(num)\n"
        "# Este código imprime cada número de la lista 'numeros'."
    )
    tk.Label(parent_frame, text=ejemplo_for, font=("Courier", 10), justify="left").pack(pady=10)

    # Ejemplo de bucle while
    ejemplo_while = (
        "Ejemplo de bucle `while`:\n"
        "contador = 0\n"
        "while contador < 5:\n"
        "    print(contador)\n"
        "    contador += 1\n"
        "# Este código imprime los números del 0 al 4 mientras el valor de 'contador' sea menor que 5."
    )
    tk.Label(parent_frame, text=ejemplo_while, font=("Courier", 10), justify="left").pack(pady=10)

    # Formulario de selección múltiple
    quiz_bucles(parent_frame)

def quiz_bucles(parent_frame):
    """Formulario de selección múltiple para el tema Bucles"""
    # Pregunta del formulario
    tk.Label(parent_frame, text="¿Cuál de las siguientes es una declaración válida de un bucle `for` en Python?", font=("Arial", 12)).pack(pady=10)

    # Opciones
    var = tk.StringVar()
    var.set('')

    opciones = [
        ("1. for (i = 0; i < 5; i++)", "incorrecto"),
        ("2. for i in range(5)", "correcto"),
        ("3. for i to 5", "incorrecto"),
        ("4. for i < 5", "incorrecto")
    ]

    for texto, valor in opciones:
        tk.Radiobutton(parent_frame, text=texto, variable=var, value=valor).pack(anchor="w")

    # Botón para enviar respuesta
    tk.Button(parent_frame, text="Enviar respuesta", command=lambda: verificar_respuesta_bucles(var)).pack(pady=10)

def verificar_respuesta_bucles(var):
    """Verifica si la respuesta del cuestionario es correcta"""
    if var.get() == "correcto":
        messagebox.showinfo("Resultado", "¡Correcto! La sintaxis correcta para un bucle `for` en Python es 'for i in range()'.")
    else:
        messagebox.showwarning("Resultado", "Incorrecto. La respuesta correcta es 'for i in range()'.")


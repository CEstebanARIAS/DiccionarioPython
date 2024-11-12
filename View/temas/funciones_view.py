import tkinter as tk
from tkinter import messagebox

def mostrar_contenido_funciones(parent_frame):
        """Muestra el contenido del tema Funciones en el frame principal"""

        # Título del tema
        tk.Label(parent_frame, text="Funciones en Python", font=("Arial", 16, "bold")).pack(pady=10)

        # Descripción del tema de Funciones
        descripcion = (
            "En Python, una función es un bloque de código que realiza una tarea específica y se puede reutilizar en diferentes "
            "partes del programa. Las funciones se definen usando la palabra clave 'def' seguida del nombre de la función y paréntesis. "
            "Dentro de los paréntesis, se pueden incluir parámetros que permiten pasar valores a la función.\n\n"
            "Ejemplo de función:\n"
            "def suma(a, b):\n"
            "    return a + b\n\n"
            "Para usar la función 'suma', simplemente la llamamos y le pasamos los valores que queremos sumar.\n"
            "resultado = suma(5, 10)"
        )
        tk.Label(parent_frame, text=descripcion, wraplength=550, justify="left").pack(pady=10)

        # Ejemplo de aplicación
        ejemplo_codigo = (
            "Ejemplo de uso de una función:\n"
            "def calcular_area(base, altura):\n"
            "    return 0.5 * base * altura\n\n"
            "base = 10\n"
            "altura = 5\n"
            "area = calcular_area(base, altura)\n"
            "print(f'El área del triángulo es {area}')"
        )
        tk.Label(parent_frame, text=ejemplo_codigo, font=("Courier", 10), justify="left").pack(pady=10)

        # Formulario de selección múltiple
        quiz_funciones(parent_frame)

def quiz_funciones(parent_frame):
        """Formulario de selección múltiple para el tema Funciones"""
        # Pregunta del formulario
        tk.Label(parent_frame, text="¿Cuál de las siguientes es una declaración válida de una función en Python?", font=("Arial", 12)).pack(pady=10)

        # Opciones
        var = tk.StringVar()
        var.set('')

        opciones = [
            ("function suma(a, b):", "incorrecto1"),
            ("def suma(a, b):", "correcto"),
            ("func suma(a, b):", "incorrecto2"),
            ("suma(a, b):", "incorrecto3")
        ]

        for texto, valor in opciones:
            tk.Radiobutton(parent_frame, text=texto, variable=var, value=valor).pack(anchor="w")

        # Botón para enviar respuesta
        tk.Button(parent_frame, text="Enviar respuesta", command=lambda: verificar_respuesta_funciones(var)).pack(pady=10)

def verificar_respuesta_funciones(var):
        """Verifica si la respuesta del cuestionario es correcta"""
        if var.get() == "":
            messagebox.showwarning("Resultado", "Selecciona una respuesta primero")
        elif var.get() == "correcto":
            messagebox.showinfo("Resultado", "¡Correcto! Las funciones en Python se definen con 'def nombre_funcion(parametros):'.")
        else:
            messagebox.showwarning("Resultado", "Incorrecto. Inténtelo nuevamente")
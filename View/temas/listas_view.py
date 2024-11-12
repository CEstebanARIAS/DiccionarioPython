import tkinter as tk
from tkinter import messagebox

def mostrar_contenido_listas(parent_frame):
        """Muestra el contenido del tema Listas en el frame principal"""

        # Título del tema
        tk.Label(parent_frame, text="Listas en Python", font=("Arial", 16, "bold")).pack(pady=10)

        # Descripción del tema de Listas
        descripcion = (
            "Las listas en Python son colecciones ordenadas y mutables que permiten almacenar múltiples elementos en una sola variable. "
            "Se definen utilizando corchetes [] y pueden contener cualquier tipo de datos, como números, cadenas o incluso otras listas.\n\n"
            "Ejemplo de lista:\n"
            "nombres = ['Ana', 'Luis', 'Carlos']\n"
            "nombres.append('Maria')  # Agrega un nuevo nombre al final de la lista\n\n"
            "Las listas tienen varios métodos útiles para manipular sus elementos, como 'append', 'remove' y 'sort'."
        )
        tk.Label(parent_frame, text=descripcion, wraplength=550, justify="left").pack(pady=10)

        # Ejemplo de aplicación
        ejemplo_codigo = (
            "Ejemplo de uso de listas:\n"
            "edades = [23, 19, 21, 25]\n"
            "edades.append(20)\n"
            "print(f'Las edades actualizadas son {edades}')"
        )
        tk.Label(parent_frame, text=ejemplo_codigo, font=("Courier", 10), justify="left").pack(pady=10)

        # Formulario de selección múltiple
        quiz_listas(parent_frame)

def quiz_listas(parent_frame):
        """Formulario de selección múltiple para el tema Listas"""
        # Pregunta del formulario
        tk.Label(parent_frame, text="¿Cuál de las siguientes es una declaración válida de una lista en Python?", font=("Arial", 12)).pack(pady=10)

        # Opciones
        var = tk.StringVar()
        var.set('')

        opciones = [
            ("list = (1, 2, 3)", "incorrecto1"),
            ("list = [1, 2, 3]", "correcto"),
            ("list = {1, 2, 3}", "incorrecto2"),
            ("list = 1, 2, 3", "incorrecto3")
        ]

        for texto, valor in opciones:
            tk.Radiobutton(parent_frame, text=texto, variable=var, value=valor).pack(anchor="w")

        # Botón para enviar respuesta
        tk.Button(parent_frame, text="Enviar respuesta", command=lambda: verificar_respuesta_listas(var)).pack(pady=10)

def verificar_respuesta_listas(var):
        """Verifica si la respuesta del cuestionario es correcta"""
        if var.get() == "":
            messagebox.showwarning("Resultado", "Selecciona una respuesta primero")
        elif var.get() == "correcto":
            messagebox.showinfo("Resultado", "¡Correcto! Las listas en Python se definen usando corchetes [].")
        else:
            messagebox.showwarning("Resultado", "Incorrecto. Inténtelo nuevamente")
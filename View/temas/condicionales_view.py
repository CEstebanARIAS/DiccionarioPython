import tkinter as tk
from tkinter import messagebox

def mostrar_contenido_condicionales(parent_frame):
    """Muestra el contenido del tema Variables en el frame principal"""

    # Título del tema
    tk.Label(parent_frame, text="Condicionales en Python", font=("Arial", 16, "bold")).pack(pady=10)

    # Descripción del tema
    descripcion = (
        "En Python, los condicionales permiten tomar decisiones en el flujo de un programa, ejecutando ciertas secciones de código solo cuando se cumplen ciertas condiciones. Estos condicionales se construyen principalmente con las estructuras if, elif y else. "
        "Aquí diferentes ejemplos:\n\n"
        "Para el condicional if\n\n"
        "x = 5  # Asigna el valor 5 a la variable 'x'\n"
        "if x > 5:   # Crea la condicion (Si x mayor que 5)'\n"
        "    print('x es mayor que 5')\n\n"
        "Para el condicional elif \n\n"
        "Este se utiliza una vez finaliza el condicional if, no puede utilizarse como principal o independiente, siempre dependera del condicional if como se muestra en el ejemplo. \n\n"
        "x = 5  # Asigna el valor 5 a la variable 'x'\n"
        "if x > 5:   # Crea la condicion (Si x mayor que 5)'\n"
        "    print('x es mayor que 5')  #Imprime el mensaje solo si la condicion es verdadera\n"
        "elif:  #Declaramos la condicion elif\n"
        "    print('x es menor que 5')   #En caso de no cumplir la condicion if, imprime su respectiva respuesta"
        
    )
    tk.Label(parent_frame, text=descripcion, wraplength=550, justify="left").pack(pady=10)

    # Ejemplo de aplicación
    ejemplo_codigo = (
        "Ejemplo de uso:\n"
        "a = 10\n"
        "if (a<10):\n"
        "    print('El valor de a es menor a 10)\n"
        "else:\n"
        "    print('El valor de a es mayor que 10)"
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
    var.set('')

    opciones = [
        ("1. x == 10", "incorrecto1"),
        ("2. x = 10", "correcto"),
        ("3. x := 10", "incorrecto2"),
        ("4. 10 = x", "incorrecto3")
    ]

    for texto, valor in opciones:
        tk.Radiobutton(parent_frame, text=texto, variable=var, value=valor).pack(anchor="w")

    # Botón para enviar respuesta
    tk.Button(parent_frame, text="Enviar respuesta", command=lambda: verificar_respuesta(var)).pack(pady=10)

def verificar_respuesta(var):
    """Verifica si la respuesta del cuestionario es correcta"""
    if var.get() == "":
        messagebox.showwarning("Resultado","Selecciona una respuesta primero")
    elif var.get() == "correcto":
        messagebox.showinfo("Resultado", "¡Correcto! La asignación de variables en Python es 'x = valor'.")
    else:
        messagebox.showwarning("Resultado", "Incorrecto. Intentelo nuevamente")
        


import tkinter as tk
from tkinter import messagebox
from View.main_view import MainView
from Model.user_model import get_user

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Educa.py - Inicio de Sesión")
        self.geometry("600x400")  # Tamaño de la ventana reducido
        self.configure(bg="#f3f3f3")

        # Frame principal para contener todo el diseño
        main_frame = tk.Frame(self, bg="white")
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=380)

        # Título y subtítulo
        tk.Label(main_frame, text="Educa.py", font=("Arial", 24, "bold"), bg="white", fg="#333").place(x=50, y=30)
        tk.Label(main_frame, text="Regístrate y empieza a convertirte en un gran programador.", 
                 font=("Arial", 12), bg="white", fg="#666").place(x=50, y=70)

        # Sección del formulario de inicio de sesión centrada
        form_frame = tk.Frame(main_frame, bg="white")
        form_frame.place(relx=0.5, y=120, anchor="n")  # Centramos el form_frame horizontalmente

        tk.Label(form_frame, text="INGRESAR", font=("Arial", 14, "bold"), bg="white", fg="#333").pack(pady=5)

        # Campo de correo electrónico
        tk.Label(form_frame, text="Correo electrónico", font=("Arial", 10), bg="white", fg="#666").pack(anchor="w", padx=10, pady=(10, 0))
        self.email_entry = tk.Entry(form_frame, font=("Arial", 10), width=30, bd=1, relief="solid")
        self.email_entry.pack(padx=10, pady=5)

        # Campo de contraseña
        tk.Label(form_frame, text="Contraseña", font=("Arial", 10), bg="white", fg="#666").pack(anchor="w", padx=10, pady=(10, 0))
        self.password_entry = tk.Entry(form_frame, show="*", font=("Arial", 10), width=30, bd=1, relief="solid")
        self.password_entry.pack(padx=10, pady=5)

        # Botón de inicio de sesión
        tk.Button(form_frame, text="Iniciar Sesión", font=("Arial", 10), bg="#FF5C8D", fg="white", 
                  activebackground="#ff4b7a", width=20, height=1, relief="flat", command=self.login).pack(pady=10)

        # Botón de registro
        tk.Button(form_frame, text="Registrarse", font=("Arial", 9), bg="#D3D3D3", fg="black", 
                  activebackground="#cccccc", width=10, height=1, relief="flat", command=self.go_to_register).pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        user = get_user(email, password)
        if user:
            self.destroy()
            MainView(user[1]).mainloop()  # user[1] es el nombre
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

    def go_to_register(self):
        from View.register_view import RegisterWindow  # Importamos aquí para evitar el ciclo
        self.destroy()
        RegisterWindow().mainloop()

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()

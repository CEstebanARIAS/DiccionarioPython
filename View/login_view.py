import tkinter as tk
from tkinter import messagebox
from View.main_view import MainView
from Model.user_model import get_user

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de Sesión")
        self.geometry("400x300")

        tk.Label(self, text="Correo:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Iniciar Sesión", command=self.login).pack(pady=20)
        tk.Button(self, text="Registrarse", command=self.go_to_register).pack(pady=5)

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

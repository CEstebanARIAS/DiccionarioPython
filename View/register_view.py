import tkinter as tk
from tkinter import messagebox
from Model.user_model import add_user

class RegisterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registrarse")
        self.geometry("400x300")

        tk.Label(self, text="Nombre:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Correo:").pack(pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(self, text="Registrarse", command=self.register).pack(pady=20)
        tk.Button(self, text="Cancelar", command=self.cancelar).pack(pady=10)


    def cancelar(self):
        self.destroy()
        from View.login_view import LoginWindow  # Importamos aquí para evitar el ciclo
        LoginWindow().mainloop()
        
    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if name and email and password:
            add_user(name, email, password)
            messagebox.showinfo("Éxito", "Registro exitoso. Inicie sesión ahora.")
            self.destroy()
            from View.login_view import LoginWindow  # Importamos aquí para evitar el ciclo
            LoginWindow().mainloop()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

if __name__ == "__main__":
    app = RegisterWindow()
    app.mainloop()

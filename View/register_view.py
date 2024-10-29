import tkinter as tk
from tkinter import messagebox
from Model.user_model import add_user

class RegisterWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Educa.py - Registrarse")
        self.geometry("550x500")
        self.configure(bg="#e8e8e8")

        # Frame centralizado para el formulario de registro
        form_frame = tk.Frame(self, bg="white", relief="raised")
        form_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

        # Título del formulario
        tk.Label(form_frame, text="Educa.py", font=("Arial", 20, "bold"), bg="white", fg="#333333").pack(pady=10)

        tk.Label(form_frame, text="REGISTRARSE", font=("Arial", 10, "bold"), bg="white", fg="#333333").pack(pady=(15, 5))

        # Campo de nombre
        tk.Label(form_frame, text="Nombre", font=("Arial", 10), bg="white", fg="#666").pack(pady=(10, 0))
        self.name_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, relief="solid")
        self.name_entry.pack(pady=5)

        # Campo de correo
        tk.Label(form_frame, text="Correo electrónico", font=("Arial", 10), bg="white", fg="#666").pack(pady=(10, 0))
        self.email_entry = tk.Entry(form_frame, font=("Arial", 12), width=30, relief="solid", justify="center")
        self.email_entry.pack(pady=5)

        # Campo de contraseña
        tk.Label(form_frame, text="Contraseña", font=("Arial", 10), bg="white", fg="#666").pack(pady=(10, 0))
        self.password_entry = tk.Entry(form_frame, show="*", font=("Arial", 12), width=30, relief="solid", justify="center")
        self.password_entry.pack(pady=5)

        # Botón de registro
        tk.Button(form_frame, text="Registrarse", font=("Arial", 10), bg="#FF5C8D", fg="white", 
                  activebackground="#ff4b7a", width=20, height=1, relief="flat", command=self.register).pack(pady=(20, 10))

        # Botón de cancelación
        tk.Button(form_frame, text="Cancelar", font=("Arial", 10), bg="#b0b0b0", fg="black", activebackground="#a9a9a9", width=10, height=1, relief="flat", command=self.cancelar).pack()

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

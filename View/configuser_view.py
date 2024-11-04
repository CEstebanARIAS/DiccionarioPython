import tkinter as tk
from tkinter import ttk, messagebox

class ConfigUserView(tk.Toplevel):
    def __init__(self, user_name):
        super().__init__()

        self.title("Configurar Perfil")
        self.geometry("400x350")
        self.resizable(False, False)

        self.user_name = user_name

        # Etiquetas y campos de entrada para la configuración
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de nombre de usuario
        label_user = tk.Label(self, text="Nombre de Usuario:")
        label_user.pack(pady=10)

        self.entry_user = tk.Entry(self)
        self.entry_user.insert(0, self.user_name)  # Cargar el nombre de usuario actual
        self.entry_user.pack(pady=5)

        # Etiqueta de correo electrónico
        label_email = tk.Label(self, text="Correo Electrónico:")
        label_email.pack(pady=10)

        self.entry_email = tk.Entry(self)
        self.entry_email.pack(pady=5)

        # Etiqueta de contraseña
        label_password = tk.Label(self, text="Nueva Contraseña:")
        label_password.pack(pady=10)

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        # Botón para guardar cambios
        self.btn_save = ttk.Button(self, text="Guardar Cambios", command=self.guardar_cambios)
        self.btn_save.pack(pady=20)

        # Botón para cerrar la ventana
        self.btn_cancel = ttk.Button(self, text="Cancelar", command=self.destroy)
        self.btn_cancel.pack(pady=5)

    def guardar_cambios(self):
        # Aquí puedes implementar la lógica para guardar los cambios del usuario
        new_user_name = self.entry_user.get()
        new_email = self.entry_email.get()
        new_password = self.entry_password.get()

        # Aquí podrías validar los datos y guardarlos en la base de datos o en un archivo
        # Por ahora, solo mostramos un mensaje de éxito
        messagebox.showinfo("Éxito", "Los cambios se han guardado correctamente.")
        self.destroy()  # Cerrar la ventana después de guardar

# Ejemplo de uso si necesitas ejecutar esto de manera independiente
if __name__ == "__main__":
    app = ConfigUserView()
    app.mainloop()

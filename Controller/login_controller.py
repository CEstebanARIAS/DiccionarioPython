from Model import user_model

def login(correo, contrasena):
    user = user_model.get_user(correo, contrasena)
    if user:
        return True
    return False

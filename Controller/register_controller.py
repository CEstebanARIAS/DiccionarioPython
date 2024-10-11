from Model import user_model

def register_user(nombre, correo, contrasena):
    try:
        user_model.add_user(nombre, correo, contrasena)
        return True
    except:
        return False

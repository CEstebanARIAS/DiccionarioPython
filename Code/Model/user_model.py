##ESTE ARCHIVO CONTIENE LAS FUNCIONES QUE INTERACTUAN CON LA BASE DE DATOS PARA LA TABLA USUARIOS.
from db_connect import connect


def get_all_users():
    conn = connect()
    cursor= conn.cursor()
    # Consultar todos los usuarios
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios
    


def add_users(nombre, correo, contrasena):
    conn = connect()
    cursor= conn.cursor()
    # Consultar todos los usuarios
    cursor.execute('INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?,?,?)'), (nombre, correo, contrasena)
    conn.commit()
    conn.close()


print(get_all_users())
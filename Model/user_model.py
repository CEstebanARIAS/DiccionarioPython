from Model.db_connect import connect

def create_user_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      nombre TEXT, 
                      correo TEXT, 
                      contrasena TEXT)''')
    conn.commit()
    conn.close()

def add_user(nombre, correo, contrasena):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nombre, correo, contrasena) VALUES (?,?,?)', 
                   (nombre, correo, contrasena))
    conn.commit()
    conn.close()

def get_user(correo, contrasena):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE correo = ? AND contrasena = ?', 
                   (correo, contrasena))
    user = cursor.fetchone()
    conn.close()
    return user



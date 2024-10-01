from db_connect import connect
def create_tables():
    conn = connect()
    cursor = conn.cursor()
    # Crear una tabla de usuarios (si aún no existe)
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS usuarios ( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   nombre TEXT NOT NULL, 
                   correo TEXT NOT NULL UNIQUE, 
                   contrasena TEXT NOT NULL, 
                   fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                   ''')
    # Crear una tabla de lecciones
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS lecciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    descripcion TEXT,
                    nivel INTEGER)
                    ''')
    # Guardar los cambios en la base de datos
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

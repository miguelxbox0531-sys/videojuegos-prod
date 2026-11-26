import pymysql
import os

def obtener_conexion():
    
    host = os.environ.get('DB_HOST', 'db') 
    user = os.environ.get('DB_USER', 'user')
    password = os.environ.get('DB_PASSWORD', 'pwd')
    database = os.environ.get('DB_NAME', 'videojuegos')
    port = int(os.environ.get('DB_PORT', 3306))

    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=database,
        port=port,
        charset='utf8mb4'
    )
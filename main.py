from flask import Flask, render_template, request, redirect, url_for, flash
import controlador_juegos as controllers
from config import Config
from models import db, Usuario
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import time
import sys

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    print("--- INICIANDO CREACIÓN DE TABLAS ---", flush=True)
    for i in range(15):
        try:
            db.create_all()
            print("¡Base de datos conectada y tablas creadas exitosamente!", flush=True)
            break
        except Exception as e:
            print(f"Esperando a la base de datos... (intento {i+1}/15). Error: {e}", flush=True)
            time.sleep(3)
    else:
        print("No se pudo conectar a la base de datos después de varios intentos.", flush=True)
        sys.exit(1)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return redirect('/juegos')
        else:
            flash('Usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nuevo_user = Usuario(username=username, password=password)
        db.session.add(nuevo_user)
        db.session.commit()
        return redirect('/login')
    return render_template('registro.html')



@app.route("/")
@app.route("/juegos")
@login_required
def juegos():
    lista = controllers.obtener_juegos()
    return render_template("juegos.html", juegos=lista)

@app.route("/agregar_juego")
@login_required
def formulario_agregar_juego():
    return render_template("agregar_juego.html")

@app.route("/guardar_juego", methods=["POST"])
@login_required
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controllers.insertar_juego(nombre, descripcion, precio)
    return redirect("/juegos")

@app.route("/eliminar_juego", methods=["POST"])
@login_required
def eliminar_juego():
    controllers.eliminar_juego(int(request.form["id"]))
    return redirect("/juegos")

@app.route("/formulario_editar_juego/<int:id>")
@login_required
def editar_juego(id):
    juego = controllers.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)

@app.route("/actualizar_juego", methods=["POST"])
@login_required
def actualizar_juego():
    id = int(request.form["id"])
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controllers.actualizar_juego(nombre, descripcion, precio, id)
    return redirect("/juegos")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
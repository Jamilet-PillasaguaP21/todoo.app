#LIBRERIA DE FLASK
from flask import Flask, render_template, request
#LIBRERIAS INDISPENSABLE PARA LA CREACION DE LA BASE DE DATOS 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase    
from sqlalchemy.orm import Mapped, mapped_column

app = Flask(__name__)

#CREACION DE LA BASE DE DATOS Y LA TABLA 
#CREAMOS LA CADENA DE CONEXION
#CONFIGURO EL PARAMETRO SQLALCHEMY_DATABASE_URI CON LA UBICACION DE LA BASE DE DATOS
#SQLALCHEMY_DATABASE_URI NO SE PUEDE CAMBIAR
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todoo.sqlite"

#VINCULAMOS LA BASE DE DATOS CON LA APP
db = SQLAlchemy(app)

#CREAR LA TABLA
class Todoo(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String, nullable=False)
    state: Mapped[float] = mapped_column(db.String, nullable=False, default='Incompleto')

#CREACION DE LA BASE Y LAS TABLAS NECESARIAS CON EL CONTEXTO DE LA APLICACION
with app.app_context():
    db.create_all()

#RUTAS BASICAS QUE DEBA TENER LA APLICACION 
@app.route("/", methods=['GET', 'POST'])
def home():
    #CLICK EN AGREGAR
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            obj = Todoo(name=name)
            db.session.add(obj)
            db.session.commit()
            return f'Agregado {name}'
        Lista_tareas = Todoo.query.all()
    return render_template('select.html')



@app.route("/insert/<id>")
def insert(id):
    return f'Hola esto es una prueba de insertar el id {id}'

@app.route("/update/<id>")
def update(id):
    return f'Hola esto es una prueba de actualizar el id {id}'

@app.route("/delete/<id>")
def delete(id):
    return f'Hola esto es una prueba de eliminar el id {id}'

if __name__ == "__main__":
    app.run()
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escritorios.db'
db = SQLAlchemy(app)


class Escritorios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, nullable=True)
    descripcion = db.Column(db.String, nullable=True)
    estado = db.Column(db.Boolean, nullable=True)

    
with app.app_context():
    db.create_all()

@app.route('/agregar_escritorio/<nombre>/<descripcion>/<estado>')
def agregar_escritorio(nombre, descripcion, estado):
    escritorio = Escritorios(nombre=nombre,
                             descripcion=descripcion,
                             estado=estado == 'True')
    db.session.add(escritorio)
    db.session.commit()
    return jsonify({'mensaje': 'Escritorio creado existosamente'})


@app.route('/mostrar_escritorios')
def mostrar_escritorios():
    escritorios = Escritorios.query.all()
    escritorios_json = [{'id': escritorio.id,
                          'nombre': escritorio.nombre,
                          'descripcion': escritorio.descripcion,
                          'estado': escritorio.estado} 
                          for escritorio in escritorios]
    return jsonify(escritorios_json)



if __name__ == '__main__':
    app.run(debug=True)

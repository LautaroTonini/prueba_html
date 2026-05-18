from unicodedata import category

from flask import Flask, render_template
from config.config import DATABASE_CONNECTION_URI
from models.db import db


app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False




db.init_app(app)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/users')
def users():
    lista_usuarios = ["ana", "juan", "maria", "pedro"]
    return render_template("users.html", list_users = lista_usuarios)

@app.route('/admin')
def admin():
    es_admin = True
    
    return render_template("admin.html", es_admin=es_admin)

@app.route('/presentacion')
def presentacion():
    return render_template("presentacion.html")

with app.app_context():
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
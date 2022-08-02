from flask import render_template  

from . import app
from .models import DBManager


RUTA = 'data/balance.db'

@app.route("/")
def inicio():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * FROM movientos")
    return render_template("inicio.html", movs=movimientos)
    # return "tabla de movimientos"


@app.route("/purchase", methods=["GET", "POST"])
def purchase():
    return "Tabla de convertir a monedas"


@app.route("/status")
def estado():
    return "estado de criptomonedas"
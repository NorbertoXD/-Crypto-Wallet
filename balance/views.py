from . import app


@app.route("/")
def hola():
    return "tabla de movimientos"


@app.route("/purchase")
def purchase():
    return "Tabla de convertir a monedas"


@app.route("/status")
def estado():
    return "estado de criptomonedas"
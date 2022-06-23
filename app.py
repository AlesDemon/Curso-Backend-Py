import random as rn
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello():
    if request.method == "GET":
        numero = rn.randint(1,100000)
        return "Hola mundo numero: {}".format(numero)
    if request.method == "POST":
        nombre = request.form["nombre"]
        return "Hola {}".format(nombre)

if __name__ == "__main__":
    app.run(debug=True)
from random import randint as rn
from flask import Flask

app = Flask(__name__)

@app.route("/adulto")
def mayoria_edad(edad):
    if edad >= 18:
        return "Como tienes {}, eres mayor de edad y puedes acceder al contenido".format(edad)
    elif edad < 18:
        return "Como tienes {}, eres menor de edad. Solo mayores de edad pueden acceder al contenido".format(edad)

@app.route("/inicio")
def inicio(nombre):
    return "Bienvenido de vuelta {}, en que puedo servirte?".format(nombre)

@app.route("/random_positivo")
def random_numpositivo(limite):
    num = rn(0,limite)
    return str(num)

@app.route("/imc")
def imc(peso,altura):
    imc = peso/(altura**2)
    return str(imc)

@app.route("/imagen_valida_720p")
def validez_720p(alto,largo):
    if alto == 720 and largo == 1080:
        return "Imagen valida"
    else:
        return "Imagen invalida"
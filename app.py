#Iniciando servicio para la API REST con Flask
from flask import Flask, jsonify, request 
from reglas import *

app = Flask(__name__)

#Definiendo la ruta de la API (hola mundo)
@app.route('/', methods=['GET'])
def index():
    return jsonify({"mensaje":"pong"})

#ruta que recibe los sintomas y signos de la enfermedad y devuelve la enfermedad (JSON)
@app.route('/diagnosticar', methods=['POST'])

def diagnosticar(): 
    #traer los datos del request
    data = request.get_json()
    #print(data)
    #print(data['sintomas'])
    #print(data['signos'])
    #print(data['sintomas'][0])
    #print(data['signos'][0])

    #Obtener los datos del JSON
    nombre = data['nombre']
    sexo = data['sexo']
    edad = data['edad']
    sintomas = data['sintomas']
    signos = data['signos']

    #cargar los datos en el motor de conocimiento
    motorDeConocimiento.reset() #limpiar el motor de conocimiento para que no se acumulen los datos
    for sintoma in sintomas:
        motorDeConocimiento.declare(Fact(sintoma=sintoma))
    for signo in signos:
        motorDeConocimiento.declare(Fact(signo=signo))
    #ejecutar el motor de conocimiento
    motorDeConocimiento.run()

    #obtener la enfermedad del motor de conocimiento (detectada por las reglas)
    enfermedad = motorDeConocimiento.facts[0]['enfermedad']
    #print(enfermedad)

    #retornar la enfermedad en formato JSON
    respuesta = {
        "nombre":nombre,
        "sexo":sexo,
        "edad":edad,
        "enfermedad":enfermedad,
        "tratamiento": obtenerTratamiento(enfermedad)
    }
# esenciales para que arranque el servidor
def obtenerTratamiento(enfermedad):

    if enfermedad == 'Gripe':
        return 'Tomar Acetaminofen y descansar'
    elif enfermedad == 'Bronquitis':
        return 'Tomar Acetaminofen y descansar ademas de tomar antibioticos'
    elif enfermedad == 'Gripe Severa':
        return 'Tomar Acetaminofen y descansar pero si no mejora ir al medico'
    else:
        return 'No se encontro tratamiento para la enfermedad'
        


if __name__ == '__main__':
    app.run(debug=True, port=5000)



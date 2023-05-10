# api que recibe json
from flask import Flask, jsonify, request
#importar sistema experto
from sistemaexperto import SistemaExperto, Sintoma

app = Flask(__name__)
"""
Este módulo contiene la aplicación Flask para el sistema experto.
"""

@app.route('/diagnosticar', methods=['POST'])
def diagnosticar():
    datos = request.get_json()
    nombre = datos["nombre"]
    sexo = datos["sexo"]
    edad = datos["edad"]
    sintomas = datos["sintomas"]

    sistema_experto = SistemaExperto()

    for sintoma in sintomas:
        sistema_experto.declare(Sintoma(sintoma=sintoma))

    sistema_experto.reset()

    sistema_experto.run()

    enfermedad = sistema_experto.facts[-1]

    if enfermedad:
        resultado = {
            "nombre": nombre,
            "sexo": sexo,
            "edad": edad,
            "enfermedad": enfermedad['enfermedad'],
            "tratamiento": enfermedad['tratamiento']
        }
    else:
        resultado = {
            "nombre": nombre,
            "sexo": sexo,
            "edad": edad,
            "enfermedad": "Desconocida",
            "tratamiento": "No se encontró una enfermedad que coincida con los síntomas proporcionados."
        }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

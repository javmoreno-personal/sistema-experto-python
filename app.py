from flask import Flask, jsonify, request
from sistemaexperto import SistemaExperto, Sintoma

app = Flask(__name__)


@app.route('/diagnosticar', methods=['POST'])
def diagnosticar():
    datos = request.get_json()
    nombre = datos["nombre"]
    sexo = datos["sexo"]
    edad = datos["edad"]
    sintomas = datos["sintomas"]

    sistema_experto = SistemaExperto()
    sistema_experto.reset()

    for sintoma in sintomas:
        sistema_experto.declare(Sintoma(sintoma=sintoma))

    sistema_experto.run()
    if sistema_experto.facts:
        enfermedad = sistema_experto.facts[-1]
    # Resto del código
    else:
        enfermedad = None

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
            "tratamiento": "No se encontró una enfermedad que coincida."
        }

    return jsonify(resultado)


if __name__ == '__main__':
    app.run(debug=True)

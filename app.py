from flask import Flask, request, jsonify
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
app = Flask(__name__)

@app.route('/diagnostic', methods=['POST'])
def diagnostic():
    # Obtener datos del JSON enviado en la solicitud
    data = request.get_json()

    # Definir variables difusas
    temperature = ctrl.Antecedent(np.arange(35, 41, 1), 'temperature')
    cough = ctrl.Antecedent(np.arange(0, 11, 1), 'cough')
    disease = ctrl.Consequent(np.arange(0, 101, 1), 'disease')

    # Definir funciones de membresía
    temperature['low'] = fuzz.trimf(temperature.universe, [35, 35, 37])
    temperature['medium'] = fuzz.trimf(temperature.universe, [36, 37, 38])
    temperature['high'] = fuzz.trimf(temperature.universe, [37, 39, 41])

    cough['mild'] = fuzz.trimf(cough.universe, [0, 0, 5])
    cough['severe'] = fuzz.trimf(cough.universe, [0, 10, 10])

    disease['low'] = fuzz.trimf(disease.universe, [0, 0, 50])
    disease['high'] = fuzz.trimf(disease.universe, [0, 100, 100])

    # Definir reglas difusas
    rule1 = ctrl.Rule(temperature['low'] & cough['mild'], disease['low'])
    rule2 = ctrl.Rule(temperature['high'] | cough['severe'], disease['high'])

    # Construir el sistema de control difuso
    diagnostic_ctrl = ctrl.ControlSystem([rule1, rule2])
    diagnostic_sim = ctrl.ControlSystemSimulation(diagnostic_ctrl)

    # Asignar valores de entrada y realizar inferencia
    diagnostic_sim.input['temperature'] = data['temperature']
    diagnostic_sim.input['cough'] = data['cough']
    diagnostic_sim.compute()

    # Obtener el diagnóstico difuso
    diagnosis = diagnostic_sim.output['disease']
    treatment = "Consulte a su médico para un diagnóstico preciso."

    # Construir la respuesta en formato JSON
    response = {
        'diagnosis': diagnosis,
        'treatment': treatment
    }

    return jsonify(response)

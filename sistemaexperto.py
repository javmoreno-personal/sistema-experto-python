from pyknow import Fact, Rule, KnowledgeEngine, MATCH

class Diagnostico(Fact):
    pass

class Enfermedad(Fact):
    pass

class Sintoma(Fact):
    pass

class SistemaExperto(KnowledgeEngine):
    @Rule(Diagnostico(enfermedad=MATCH.enfermedad, tratamiento=MATCH.tratamiento))
    def mostrar_diagnostico(self, enfermedad, tratamiento):
        self.declare(Enfermedad(enfermedad=enfermedad, tratamiento=tratamiento))

base_reglas = [
    SistemaExperto(),
    Rule(Diagnostico(enfermedad='Gripe', tratamiento='Tomar paracetamol'))
        .salience(-2)
        .AND(Sintoma('Tos'), Sintoma('Fiebre'), Sintoma('Dolor de cabeza')),
    # Agrega más reglas para otras enfermedades y síntomas aquí
]

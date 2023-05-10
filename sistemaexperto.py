from pyknow import Fact, Rule, KnowledgeEngine, MATCH

class Diagnostico(Fact):
    pass

class Enfermedad(Fact):
    pass

class Sintoma(Fact):
    pass

class SistemaExperto(KnowledgeEngine):
    @Rule(Diagnostico(enfermedad=MATCH.enfermedad, tratamiento=MATCH.tratamiento),
          Sintoma('Tos'), Sintoma('Fiebre'), Sintoma('Dolor de cabeza'))
    def mostrar_diagnostico(self, enfermedad, tratamiento):
        self.declare(Enfermedad(enfermedad=enfermedad, tratamiento=tratamiento))

base_reglas = [
    SistemaExperto(),
    Rule(Diagnostico(enfermedad='Gripe', tratamiento='Tomar paracetamol'))
]

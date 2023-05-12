from experta import Fact, Rule, KnowledgeEngine
#estos son los hechos que se van a utilizar para las reglas (signos, sintomas y enfermedad)
class enfermedad(Fact):
    """Informacion de la enfermedad"""
    pass

class signo(Fact):
    """Informacion de los signos"""
    pass

class sintoma(Fact):
    """Informacion de los sintomas"""
    pass


class motorDeConocimiento(KnowledgeEngine):
    """
    Estructura basica para definir una regla en el motor de conocimiento

      @Rule(
        Fact(sintoma=''),
        Fact(sintoma=''),
        Fact(signo=''),
        Fact(signo=''),
    )
    def regla3(self):
        self.declare(Fact(enfermedad=''))
        
    Otra forma de hacer esto y evitando declarar los mismos sintomas y signos en cada regla es decir
    que si se cumple una regla pero aun hay mas sintomas y signos que no se han declarado en la regla 
    se puede seguir ejecutando la misma regla hasta que se cumpla la condicion de la regla
    @Rule(
        Fact(sintoma=MATCH.sintoma1),
        Fact(sintoma=MATCH.sintoma2),
        Fact(signo=MATCH.signo1),
        Fact(signo=MATCH.signo2),
    )
    def regla3(self, sintoma1, sintoma2, signo1, signo2):
        self.declare(Fact(enfermedad=''))
        
        """




    # Condiciones de la regla
    @Rule(enfermedad(sintoma=sintoma(sintoma='Tos')) 
          & enfermedad(sintoma=sintoma(sintoma='Fiebre')) 
          & enfermedad(signo=signo(signo='Dolor de cabeza'))
    )
    def regla1(self):
        # Acciones de la regla (enfermedad que se puede tener segun los sintomas y signos)
        self.declare(Fact(enfermedad='Gripe'))
    
    @Rule(enfermedad(sintoma=sintoma(sintoma='Tos')) 
          & enfermedad(sintoma=sintoma(sintoma='Fiebre')) 
          & enfermedad(signo=signo(signo='Dolor de cabeza'))
          & enfermedad(signo=signo(signo='Dolor de garganta'))
    )
    def regla2(self):
        self.declare(Fact(enfermedad='Gripe Severa'))
  
#Bronquitis se puede tener con los siguientes sintomas y signos ()
    @Rule(enfermedad(sintoma=sintoma(sintoma='Tos')) 
          & enfermedad(sintoma=sintoma(sintoma='Fiebre')) 
          & enfermedad(signo=signo(signo='fatiga'))
          & enfermedad(signo=signo(signo='Dolor de garganta'))
    )
    def regla3(self):
        self.declare(Fact(enfermedad='Bronquitis'))
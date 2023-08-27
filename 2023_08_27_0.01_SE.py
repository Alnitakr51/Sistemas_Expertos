# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 00:59:32 2023

@author: Gadiel Jimenez
"""

# Ejemplo de Adquisición de Conocimiento
class ExpertoHumano:
    def conocimiento_experto(self):
        return "Si la temperatura es alta y el cielo está despejado, entonces es un día caluroso."

# Ejemplo de Representación del Conocimiento
class BaseConocimiento:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, regla):
        self.reglas.append(regla)

class Regla:
    def __init__(self, condicion, conclusion):
        self.condicion = condicion
        self.conclusion = conclusion

# Ejemplo de Motor de Inferencia
class MotorInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def inferir(self, hechos):
        for regla in self.base_conocimiento.reglas:
            if regla.condicion(hechos):
                return regla.conclusion
        return "No se pudo llegar a una conclusión."

# Ejemplo de Interfaz
class InterfazUsuario:
    def hacer_pregunta(self):
        return input("¿Cuál es la temperatura y el estado del cielo? (Ejemplo: alta despejado):")

# Ejemplo de Usuario
class Usuario:
    def __init__(self):
        self.interfaz = InterfazUsuario()

    def obtener_datos(self):
        datos = self.interfaz.hacer_pregunta()
        temperatura, cielo = datos.split()
        return {"temperatura": temperatura, "cielo": cielo}

# Ejemplo completo de ejecución
if __name__ == "__main__":
    experto = ExpertoHumano()
    conocimiento = experto.conocimiento_experto()

    base_conocimiento = BaseConocimiento()
    regla = Regla(
        lambda hechos: hechos["temperatura"] == "alta" and hechos["cielo"] == "despejado",
        "Es un día caluroso."
    )
    base_conocimiento.agregar_regla(regla)

    motor_inferencia = MotorInferencia(base_conocimiento)
    usuario = Usuario()

    hechos = usuario.obtener_datos()
    conclusion = motor_inferencia.inferir(hechos)
    print(conclusion)

# Utils/progress_tracker.py

class ProgressTracker:
    def __init__(self):
        self.temas = {
            "Variables": 20,
            "Condicionales": 20,
            "Bucles": 20,
            "Funciones": 20,
            "Listas": 20
        }
        self.progreso_actual = 0
        self.completados = set()

    def completar_tema(self, tema):
        if tema in self.temas and tema not in self.completados:
            self.progreso_actual += self.temas[tema]
            self.completados.add(tema)
        return self.progreso_actual

    def obtener_progreso(self):
        return self.progreso_actual

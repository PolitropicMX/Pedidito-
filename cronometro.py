from datetime import datetime
from threading import Thread
import time

class CronometroApp(Thread):
    def __init__(self, etiqueta, intervalo=1):
        super().__init__()
        self.etiqueta = etiqueta
        self.intervalo = intervalo
        self.terminar = False

    def run(self):
        segundos = 0
        while not self.terminar:
            time.sleep(self.intervalo)
            segundos += 1
            self.actualizar_etiqueta(segundos)

    def actualizar_etiqueta(self, segundos):
        tiempo_formato = "{:02}:{:02}".format(segundos // 60, segundos % 60)
        self.etiqueta.config(text=tiempo_formato)

    def detener(self):
        self.terminar = True

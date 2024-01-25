import tkinter as tk
from threading import Thread
import time

class Cronometro(Thread):
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

def iniciar_cronometro(etiqueta, cronometros_activos):
    cronometro = Cronometro(etiqueta)
    cronometro.start()
    cronometros_activos.append(cronometro)

def detener_todos_cronometros(cronometros_activos):
    for cronometro in cronometros_activos:
        cronometro.detener()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Cronómetros Múltiples")

# Etiqueta para mostrar el tiempo del cronómetro
etiqueta_cronometro = tk.Label(ventana, text="00:00", font=("Helvetica", 24))
etiqueta_cronometro.pack(pady=20)

# Botones para iniciar y detener cronómetros
boton_iniciar = tk.Button(ventana, text="Iniciar Cronómetro", command=lambda: iniciar_cronometro(etiqueta_cronometro, cronometros_activos))
boton_iniciar.pack(pady=10)

boton_detener = tk.Button(ventana, text="Detener Todos", command=lambda: detener_todos_cronometros(cronometros_activos))
boton_detener.pack(pady=10)

# Lista para almacenar los cronómetros activos
cronometros_activos = []

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()

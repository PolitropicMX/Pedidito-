import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from cronometro import CronometroApp
import openpyxl
from threading import Thread
import time

#Esta funcion es una ventana de tkinter que solo necesita la ruta del archivo excel a analizar
class Analisis_class:
    def __init__(self,root):
        ruta_archivo_excel = 'PEDIDITO_DB.xlsx'
        nombre_hoja_excel = 'BASE_PEDIDITO'
        rango_a_extraer = 'A2:K1500'  # Por ejemplo, desde A1 hasta C10

        # Cargar el libro de trabajo (workbook)
        libro = openpyxl.load_workbook(ruta_archivo_excel)

        # Acceder a una hoja específica
        hoja = libro[nombre_hoja_excel]

        # Extraer información desde el rango especificado
        informacion_extraida = self.extraer_informacion_desde_rango(hoja, rango_a_extraer)
##        print(informacion_extraida[0:5])
        pedidos_totales = len(informacion_extraida)
        print("ingreso de base de datos a PEDIDITO SOFTWARE")
        conjunto_telefonos = set()
        conjunto_ubicaciones = set()
        conjunto_nombres = set()
        tne = 0
        une = 0
        nne = 0
        nombres_y_telefonos = []
        clientes_no_esp= []
        for i,fila in enumerate(informacion_extraida):
##            print(f"{fila[2]}")
            if fila[3] == "No especificado":
                tne += 1
                clientes_no_esp.append([fila[2],fila[5]])
            elif fila[3] not in conjunto_telefonos:
                conjunto_telefonos.add(fila[3])
                conjunto_ubicaciones.add(fila[5])
                conjunto_nombres.add(fila[2])
                nombres_y_telefonos.append([fila[3],fila[2],fila[5],1])
            elif fila[3] in conjunto_telefonos:
                for i,perfil in enumerate(nombres_y_telefonos):
                    if fila[3] == perfil[0]:
                        perfil[3] += 1
            
            elif fila[5] == "No especificado":
                une += 1
            elif fila[2] == "No especificado":
                nne += 1

                
##        print(conjunto_telefonos)
        
        print(f'total de datos:{len(informacion_extraida)}')
        print(f'telefonos:{len(conjunto_telefonos)} no esp {tne}')
        print(f'ubicaciones:{len(conjunto_ubicaciones)} no esp {une}')
        print(f'nombres:{len(conjunto_nombres)} no esp {nne}')
        for i in range(len(nombres_y_telefonos)):
            print(nombres_y_telefonos[i])
        for i in range(len(clientes_no_esp)):
            print(clientes_no_esp[i])
        
        #Momento de la creacion de este objeto
        ahora = datetime.now()
        self.fecha_y_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")

        ## TODOS LOS WIDGETS A USAR ------------------------------------------------------------------------------------------------------------------------------------
        # Create a Frame for the Checkbuttons
        self.root = tk.Toplevel(root,bg="#046546")# 0
        self.check_frame = ttk.LabelFrame(self.root, text="Detalles del Pedido", padding=(20, 10))
        ## Hora y fecha
        self.hora_label = tk.Label(self.root,text=self.fecha_y_hora)
        ## DIRECCIÓN DE ENTREGA
        self.direc_cliente_frame = ttk.LabelFrame(self.check_frame, text="Costo total del pedido ", padding=(20, 10))
        self.direc_cliente_entry = ttk.Entry(self.direc_cliente_frame)
        self.direc_cliente_entry.insert(0, "Ej. 141")
        self.direc_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(self.direc_cliente_entry))# Asociar la función borrar_texto al evento clic
        ## NOMBRE DEL CLIENTE
        self.nombre_cliente_frame = ttk.LabelFrame(self.check_frame, text="$ para pedido", padding=(20, 10))
        self.nombre_cliente_entry = ttk.Entry(self.nombre_cliente_frame)
        self.nombre_cliente_entry.insert(0, "Ej.200")
        self.nombre_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(nombre_cliente_entry))# Asociar la función borrar_texto al evento clic
        ## NUMERO DEL CLIENTE
        self.num_cliente_frame = ttk.LabelFrame(self.check_frame, text="$ regresado repartidor", padding=(20, 10))
        self.num_cliente_entry = ttk.Entry(self.num_cliente_frame)
        self.num_cliente_entry.insert(0, "Ej. 210")
        self.num_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(num_cliente_entry))# Asociar la función borrar_texto al evento clic
        ## TARIFA
        self.tarifa_frame = ttk.LabelFrame(self.check_frame, text="Tarifa $MXN", padding=(20, 10))
        self.tarifa_entry = ttk.Entry(self.tarifa_frame)
        self.tarifa_entry.insert(0, "Ej. 10")
        self.tarifa_entry.bind("<Button-1>", lambda event: self.borrar_texto(tarifa_entry))# Asociar la función borrar_texto al evento clic

        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self.check_frame, text="Metodo de Pago", padding=(20, 10))
        # Radiobuttons
        self.metodos_de_pago = ["Efectivo","Transferencia"]
        self.var_metodos_de_pago = tk.StringVar(value='') 
        self.radio_metodos_de_pago = [tk.Radiobutton(self.radio_frame, text=metodo, variable=self.var_metodos_de_pago, value=metodo) for i,metodo in enumerate(self.metodos_de_pago)]
        # BOTONES
        self.widgets_frame = ttk.Frame(self.check_frame)
        self.botones = [("Guardar",self.guardar_f),("Cancelar",self.cancelar_f)]
        self.botones_button = [ttk.Button(self.widgets_frame, text=i[0],command=i[1] ) for i in self.botones]
##        for i,btn in enumerate(self.botones_button):
##            
    def guardar_f(self):
        
        self.root.destroy()
    def cancelar_f(self):
        self.root.destroy()
    def extraer_informacion_desde_rango(self,hoja, rango):
        datos_extraidos = []

        # Obtener las celdas en el rango especificado
        celdas = hoja[rango]
        
        # Iterar sobre las celdas en el rango
        for fila in reversed(celdas):
            fila_datos = [celda.value for celda in fila]
            datos_extraidos.append(fila_datos)

        return datos_extraidos
    def draw(self):
        ## TODO LO QUE DIBUJA A LOS WIDGETS -------------------------------------------------------------------------------------------------------------------------------

        ## MAPA JERARQUICO DE WIDGETS
        ## root
        ##     fecha_y_hora
        ##     productos
        ##         orden: text
        ##     detalles del pedido/checkframe
        ##         direccion_de_entrega:entry
        ##         nombre:entry
        ##         numero:entry
        ##         metodo de pago: Radio_buttons
        self.check_frame.grid(row=2, column=0, padx=(3), pady=(3), sticky="nsew")
        self.hora_label.grid(row=0, column=0, padx=(3), pady=(3), sticky="nsew")

        self.direc_cliente_frame.grid(row=0, column=0, sticky="nsew")
        self.direc_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.nombre_cliente_frame.grid(row=1, column=0, sticky="nsew")
        self.nombre_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.num_cliente_frame.grid(row=1, column=1, sticky="nsew")
        self.num_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.tarifa_frame.grid(row=0, column=1, sticky="nsew")
        self.tarifa_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        for i,radio in enumerate(self.radio_metodos_de_pago):
##            radio.state(["alternate"])
            
            radio.grid(row=i, column=0, sticky="nsew")

        for i,btn in enumerate(self.botones_button):
            btn.grid(row=0, column=i, sticky="nsew")
        self.widgets_frame.grid(row=3, column=0, sticky="nsew")

    def get_data(self,func):
        direccion = self.direc_cliente_entry.get()
        nombre = self.nombre_cliente_entry.get()
        numero = self.num_cliente_entry.get()
        orden = self.orden_text.get()
        data = [self.fecha_y_hora,direccion, nombre, numero, orden]
        func(data)
    def borrar_texto(self,entry):
        # Borra el texto dentro del Entry al recibir un clic
        entry.delete(0, tk.END)


"""
PEDIDITO SOFTWARE

Author: PolitropicMX
"""
import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from cronometro import CronometroApp
import openpyxl
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
    print("Se inicializo el cronometro")
    cronometro = Cronometro(etiqueta)
    cronometro.start()
    cronometros_activos.append(cronometro)

def detener_todos_cronometros(cronometros_activos):
    for cronometro in cronometros_activos:
        cronometro.detener()
class Agregar_pedido:
    def __init__(self,root,tree,func_rtrn,pedidos):
        self.pedidos = pedidos
        self.return_func = func_rtrn## Funcion de retorno a la ventana principal o ventana padre
        self.tree = tree# el treeview de la ventana principal o ventana padre
        ## CODIGO PARA ESTRAER FECHAY HORA
        ahora = datetime.now()
        self.fecha_y_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")

        ## TODOS LOS WIDGETS A USAR ------------------------------------------------------------------------------------------------------------------------------------
        ## VENTANA
        self.root = tk.Toplevel(root,bg="#046546")# 0
        ## FRAME
        self.check_frame = ttk.LabelFrame(self.root, text="Detalles del Pedido", padding=(20, 10))
        ## TITULO: HORA
        self.hora_label = tk.Label(self.root,text=self.fecha_y_hora)
        ## FRAME: DIRECCIÓN DE ENTREGA
        self.direc_cliente_frame = ttk.LabelFrame(self.check_frame, text="Dirección de Entrega", padding=(20, 10))
        ## ENTRY: IRECCIÓN DE ENTREGA
        self.direc_cliente_entry = ttk.Entry(self.direc_cliente_frame)
        self.direc_cliente_entry.insert(0, "Ej. Purisima 55")
        self.direc_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(self.direc_cliente_entry))# Asociar la función borrar_texto al evento clic
        ## NOMBRE DEL CLIENTE
        self.nombre_cliente_frame = ttk.LabelFrame(self.check_frame, text="Nombre Cliente", padding=(20, 10))
        self.nombre_cliente_entry = ttk.Entry(self.nombre_cliente_frame)
        self.nombre_cliente_entry.insert(0, "Ej. Tierno")
        self.nombre_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(nombre_cliente_entry))# Asociar la función borrar_texto al evento clic
        ## NUMERO DEL CLIENTE
        self.num_cliente_frame = ttk.LabelFrame(self.check_frame, text="Numero celular", padding=(20, 10))
        self.num_cliente_entry = ttk.Entry(self.num_cliente_frame)
        self.num_cliente_entry.insert(0, "Ej. 5510293483")
        self.num_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(num_cliente_entry))# Asociar la función borrar_texto al evento clic
        ## TARIFA
        self.tarifa_frame = ttk.LabelFrame(self.check_frame, text="Tarifa $MXN", padding=(20, 10))
        self.tarifa_entry = ttk.Entry(self.tarifa_frame)
        self.tarifa_entry.insert(0, "Ej. 10")
        self.tarifa_entry.bind("<Button-1>", lambda event: self.borrar_texto(tarifa_entry))# Asociar la función borrar_texto al evento clic
        ## Orden
        # Crear un widget Text
        self.orden_text_frame = ttk.LabelFrame(self.root, text="Productos")
        self.orden_text = tk.Text(self.orden_text_frame, height=10, width=40)
        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self.check_frame, text="Lista de articulos", padding=(20, 10))
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
        orden = str(self.orden_text.get("1.0", "end-1c"))
        print(orden)
        dicc_orden = self.procesar_lista_compras(orden)
        print(dicc_orden)
        # "N° de Pedido","Fecha","Nombre del cliente","N° de Contacto","Recoleccion","Entrega","Producto","Paga con…","Costo del pedido","Tarifa","Cobro total","Dinero entregado a repartidor para compra","$ entregado al repartidor para cambio","$ total dado al repartidor","$ total recibido por el repartidor"]  

        direccion = self.direc_cliente_entry.get()
        nombre = self.nombre_cliente_entry.get()
        numero = self.num_cliente_entry.get()
        orden = self.orden_text.get("1.0", "end-1c")
        tarifa = self.tarifa_entry.get()
        list_cli = [self.pedidos,self.fecha_y_hora,nombre,numero,"No especificado",direccion,orden,"No especificado","No especificado",tarifa,"No especificado","No especificado","No especificado","No especificado","No especificado"]
        dicc_cli = {"dict":["No especificado",str(self.fecha_y_hora),nombre,numero,"No especificado",direccion,orden,"No especificado","No especificado",tarifa,"No especificado","No especificado","No especificado","No especificado","No especificado"]}
        self.return_func(self.tree,list_cli)
        self.root.destroy()
    def cancelar_f(self):
        self.root.destroy()      
    def procesar_lista_compras(self,cadena_lista):
        if any(char.isdigit() for char in cadena_lista):
            # La cadena contiene al menos un número
            print("La cadena contiene números. Realizar alguna acción aquí.")
            print(f"cadena : '{cadena_lista}'")
            lista_items = cadena_lista.split(', ')
            resultado = {}

            for item in lista_items:
                partes = item.split(' ')
                if len(partes) >= 2:
                    cantidad = int(partes[0])
                    producto = ' '.join(partes[1:])
                    resultado[producto] = cantidad
            return resultado
        else:
            # La cadena no contiene números, no hacer nada
            
            pass
        
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
        
        self.orden_text_frame.grid(row=1, column=0, sticky="nsew")
        self.orden_text.pack(pady=10)

        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        for i,radio in enumerate(self.radio_metodos_de_pago):
##            radio.state(["alternate"])
            
            radio.grid(row=i, column=0, sticky="nsew")

        for i,btn in enumerate(self.botones_button):
            btn.grid(row=0, column=i, sticky="nsew")
        self.widgets_frame.grid(row=3, column=0, sticky="nsew")

    def get_data(self,func):
        
        data = [self.fecha_y_hora,direccion, nombre, numero, orden]
        func(data)
    def borrar_texto(self,entry):
        # Borra el texto dentro del Entry al recibir un clic
        entry.delete(0, tk.END)

class Pendientes_class:
    def __init__(self,root):

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


## BUTTON FUNC; ACTIVATED WHEN PRESSED
def agregar():
    iniciar_cronometro(pizarra[6][0], main_cronometro_cli)
    agregar_ventana = Agregar_pedido(root,treeview,agregar_rtrn,pedidos_totales)
    agregar_ventana.draw()
## RETURN FUNC; THIUS IS THE GRIDGE BETWEEN THAT WINDOW AN THIS WINDOW
def agregar_rtrn(tree,lista):
    lista_de_tiendas = {
                    "1":"Hamburguesas al carbon",
                    "2":"Tacos Beto",
                    "3":"Hamburguesas al carbon 2",
                    "4":"Postres la jaula",
                    "5":"Tacos de arrachera",
                    "6":"Crepas",
                    "7":"Tacos birria",
                    "8":"Banderillas luigi",
                    "9":"Panaderia los 2000",
                    "10":"Carnitas prados",
                    "11":"Azcarbon",
                    "12":"Fonda los 50",
                    "13":"Tienda la lupita",
                    "14":"Tacos foodtruck",
                    "15":"purificadora rosa",
                    "16":"Farmacia Abuelitos",
                    "17":"Supercito",
                    "18":"Carniceria los rucos",
                    "19":"polleria bachoco",
                    "20":"comida para llevar orange",
                    "21":"farmacia bambi",
                    "22":"pollo la corcholata",
                    "23":"la carniceria el chico",
                    "24":"Tienda Irma",
                    "25":"Huaraches",
                    "26":"Papeleria fake",
                    "27":"Optica",
                    "28":"Panaderia francisco",
                    "29":"Listones Ruca",
                    "30":"EdgarOnline",
                    "31":"Donas coche",
                    "32":"OXXO",
                    "33":"tacos don dani",
                    "34":"Carniceria Angel los putos",
                    "35":"Tienda Angel",
                    "36":"Tienda las girlfriend",
                    "37":"Ferreteria Prados",
                    "38":"Magnum",
                    "39":"Cocina Claudette",
                    "40":"Barbacha",
                    "41":"Tienda Pet",
                    "42":"Purificadora Iglesia",
                    "43":"Recauderia iglesia",
                    "44":"Serranita",
                    "45":"Tienda Israel",
                    "46":"Chilaquiles Israel",
                    "47":"Cerrajero el Verde",
                    "48":"El verduras Cetis 33",
                    "49":"Helados Cetis 33",
                    "50":"OfficeDepot",
                    "51":"Tacos de carnitas el rosario",
                    "52":"Abarrotes Oasis",
                    "53":"Soriana",
                    "54":"Tortas Soriana",
                    "55":"Hamburguesas olvidadas",
                    "56":"Cerrajeria",
                    "57":"Tacos de Canasta",
                    "58":"Local de Frutas",
                    "59":"TownCenter Rosario",
                    "60":"BbqCronch",
                    "61":"Mandrake",
                    "62":"Aquacliva",
                    "63":"Pan chino",# Rancho la esmeralda
                    "64":"Quesadillas la curva",
                    "65":"Reyes",
                    "66":"Antojitos Mario"
                    }
    tiendas = list(lista_de_tiendas.values())
    print(f"tienda es: {tiendas}")
    ultimo_indice = tree.get_children()[-1]
    mostrar_dicc(tree,lista,"btn-add")
    orden_sin_terminar.append(lista)
    print(f"orden a añadir : {orden_sin_terminar}")
    main_name_cli.set(lista[2])
    main_num_cli.set(lista[3])
    main_direccion_cli.set(lista[5])
    main_hora_cli.set(f"Hora del Pedido: {lista[1]}")
    main_costo_cli.set("")
    main_cambio_cli.set("")
    main_tarifa_cli.set("")
    main_entrega_cli.set("")
    productos = procesar_lista_compras(lista[6])
    ## TITULOS 
    pizarra.append([tk.Label(pizarra[9][0],text="Productos",font=("Helvetica",15)),(0,0)])
    pizarra.append([tk.Label(pizarra[9][0],text="Cantidad",font=("Helvetica",15)),(0,1)])
    pizarra.append([tk.Label(pizarra[9][0],text="Costo unitario",font=("Helvetica",15)),(0,2)])
    pizarra.append([tk.Label(pizarra[9][0],text="Lo compraron de:",font=("Helvetica",15)),(0,3)])
    opciones_var = []
    for i,producto in enumerate(productos):
        # Variable para almacenar la opción seleccionada
        opciones_var.append(tk.StringVar(pizarra[9][0]))
        opciones_var[i].set(tiendas[0])
        pizarra.append([tk.Label(pizarra[9][0],text=producto,font=("Helvetica",15)),(i+1,0)])
        pizarra.append([tk.Label(pizarra[9][0],text=productos[producto],font=("Helvetica",15)),(i+1,1)])
        pizarra.append([tk.Entry(pizarra[9][0]),(i+1,2)])
        pizarra.append([tk.Entry(pizarra[9][0]),(i+1,2)])
        pizarra.append([tk.OptionMenu(pizarra[9][0], opciones_var[i], *tiendas),(i+1,3)])
    for i,widget in enumerate(pizarra):
        if len(widget) > 2:
            widget[0].grid(row = widget[1][0],column = widget[1][1],rowspan= widget[2][0],columnspan=widget[2][1])
        else:
            widget[0].grid(row = widget[1][0],column = widget[1][1])
    
def procesar_lista_compras(cadena_lista):
    if any(char.isdigit() for char in cadena_lista):
        # La cadena contiene al menos un número
        print("La cadena contiene números. Realizar alguna acción aquí.")
        print(f"cadena : '{cadena_lista}'")
        lista_items = cadena_lista.split(', ')
        resultado = {}

        for item in lista_items:
            partes = item.split(' ')
            if len(partes) >= 2:
                cantidad = int(partes[0])
                producto = ' '.join(partes[1:])
                resultado[producto] = cantidad
        return resultado
    else:
        # La cadena no contiene números, no hacer nada
        
        pass
    
def btn_pendientes():
    pendientes_win = Pendientes_class(root)
    pendientes_win.draw()
    
def devolver(data):
    return data

def mostrar_dicc(tree, diccionario, parent=""):
    print(diccionario)
    
    if parent == "btn-add":# 
        tree.insert("", '0',text=diccionario[0], values=diccionario[1:])
    else:
        tree.insert("", 'end',text=diccionario[0], values=diccionario[1:])
        
def leer_excel(ruta_archivo, nombre_hoja, rango):
    # Leer el archivo Excel
    df = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja)
    print(df)
    # Seleccionar el rango específico
    df_rango = df.loc[rango[0]:rango[1]]

    # Convertir el DataFrame a un diccionario
    datos_diccionario = df_rango.to_dict(orient='records')

    return datos_diccionario

def extraer_informacion_desde_rango(hoja, rango):
    datos_extraidos = []

    # Obtener las celdas en el rango especificado
    celdas = hoja[rango]
    
    # Iterar sobre las celdas en el rango
    for fila in reversed(celdas):
        fila_datos = [celda.value for celda in fila]
        datos_extraidos.append(fila_datos)

    return datos_extraidos

def actualizar_fecha(etiqueta):
    fecha_hora_actual = datetime.now()
    fecha_hora_str = fecha_hora_actual.strftime("%A %d de %B %Y, hora %H:%M:%S")
    etiqueta.config(text=f"Bienvenido, la fecha del día de hoy es {fecha_hora_str}")
    root.after(1000, lambda: actualizar_fecha(etiqueta))  # Actualizar cada 1000 milisegundos (1 segundo)

def autocompletar(event):
    entrada_texto = entry.get().lower()
    sugerencias = [item for item in lista_palabras if entrada_texto in item.lower()]

    mostrar_sugerencias(sugerencias)

def mostrar_sugerencias(sugerencias):
    if sugerencias:
        lista_sugerencias.delete(0, tk.END)
        for sugerencia in sugerencias:
            lista_sugerencias.insert(tk.END, sugerencia)
        lista_sugerencias.place(x=entry.winfo_x(), y=entry.winfo_y() + entry.winfo_height())
    else:
        lista_sugerencias.place_forget()

def seleccionar_sugerencia(event):
    entry.delete(0, tk.END)
    entry.insert(0, lista_sugerencias.get(tk.ACTIVE))
    lista_sugerencias.place_forget()

##### MAPA JERARQUICO
## root
##    hojas
##       paginas
##          opciones_labelframes
##             opciones_widgets_1



# VENTANA PRINCIPAL
## VENTANA
root = tk.Tk()
root.title("PEDIDITO SYSTEMS TECHNOLOGY by Fernando López V.")
root.option_add("*tearOff", False) # This is always a good idea
# Notebook
cuaderno = ttk.Notebook(root)# jerarquia: 0
encabezados = ['Principal','Buscar','Mapa']
# hojas
hojas = []# jerarquia: 1
# paginas
paginas = []# jerarquia: 2
# labelframe
opciones_principal = [["Nueva Orden",(0,0)],["Ordenes Pendientes",(0,1)],["Orden Actual",(1,0)]]
opciones_labelframes = []# jerarquia: 3
# widgets
opciones_widgets_1 = []# jerarquia: 4
opciones_widgets_2 = []# jerarquia: 4
# pizarra
pizarra = []# jerarquia: 2
productos_strvar = []

treeview_data = {}
orden_sin_terminar = []

for i,encabezado in enumerate(encabezados):
    hojas.append(ttk.Frame(cuaderno))
    cuaderno.add(hojas[i], text=encabezado)
    paginas.append(ttk.Frame(hojas[i]))
    
for i,frame in enumerate(paginas):
    frame.grid(row=0,column=0,padx=0,pady=0)


# -------------------------------------------------------------------------- FRAMES----------------------------------------------------
for i,opcion in enumerate(opciones_principal):
    opciones_labelframes.append(tk.LabelFrame(paginas[0], text=opcion[0]))
    opciones_labelframes[i].grid(row = opcion[1][0], column = opcion[1][1])

opciones_widgets_1.append([tk.Button(opciones_labelframes[0],text="(   +   )",command=agregar),(0,0)])
opciones_widgets_1[len(opciones_widgets_1)-1][0].grid(row=opciones_widgets_1[len(opciones_widgets_1)-1][1][0],column=opciones_widgets_1[len(opciones_widgets_1)-1][1][1], sticky = "we")
pendientes = 0
opciones_widgets_1.append([tk.Button(opciones_labelframes[0],text=f"Ordenes Pendientes : {pendientes}",command=btn_pendientes),(0,1)])
opciones_widgets_1[len(opciones_widgets_1)-1][0].grid(row=opciones_widgets_1[len(opciones_widgets_1)-1][1][0],column=opciones_widgets_1[len(opciones_widgets_1)-1][1][1])

cuaderno.grid(row=0,column=0,padx=0,pady=0,sticky="nswe")
fecha_actual = datetime.now()

## PIZARRA WIDGETS
## Label-Fecha
## FECHA Y HORA
pizarra.append([tk.Label(opciones_labelframes[0],text=fecha_actual,font=("Helvetica",25)),(1,0),(1,3)])# 0
actualizar_fecha(pizarra[len(pizarra)-1][0])
## StringVar's
main_name_cli = tk.StringVar()
main_num_cli = tk.StringVar()
main_direccion_cli = tk.StringVar()
main_costo_cli = tk.StringVar()
main_cambio_cli = tk.StringVar()
main_tarifa_cli = tk.StringVar()
main_entrega_cli = tk.StringVar()
main_hora_cli = tk.StringVar()
main_cronometro_cli = []
##main_cronometro_cli.append(tk.StringVar())
main_name_cli.set("El. Eliseo")
main_num_cli.set("Ej. 5530181574")
main_costo_cli.set("Ej. 170")
main_cambio_cli.set("Ej. 20")
main_tarifa_cli.set("Ej. 10")
main_entrega_cli.set("Ej. 210")
main_direccion_cli.set("Ej. Edif 14B 303")
main_hora_cli.set("--:--")
##main_cronometro_cli[0].set("Sin Pedido")
## WIDGETS
pizarra.append([tk.Label(opciones_labelframes[0],text= "Nombre del cliente"),(2,0)])# 1
pizarra.append([tk.Entry(opciones_labelframes[0],textvariable=main_name_cli,font=("Helvetica",15)),(2,1)])# 2
pizarra.append([tk.Label(opciones_labelframes[0],textvariable=main_hora_cli),(2,2)])# 3
pizarra.append([tk.Label(opciones_labelframes[0],text= "Numero del cliente"),(3,0)])# 4
pizarra.append([tk.Entry(opciones_labelframes[0],textvariable=main_num_cli,font=("Helvetica",15)),(3,1)])# 5
pizarra.append([tk.Label(opciones_labelframes[0],text="--:--"),(3,2)])# 6
pizarra.append([tk.Label(opciones_labelframes[0],text= "Dirección del cliente"),(4,0)])# 7
pizarra.append([tk.Entry(opciones_labelframes[0],textvariable=main_direccion_cli,font=("Helvetica",15)),(4,1)])# 8
pizarra.append([tk.LabelFrame(opciones_labelframes[0],text= "Productos"),(5,0),(1,2)])# 9 Recuerda Cambiar
pizarra.append([tk.LabelFrame(opciones_labelframes[0],text= "Costo"),(6,0)])
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_costo_cli,font=("Helvetica",15)),(0,0)])
pizarra.append([tk.LabelFrame(opciones_labelframes[0],text= "Cambio"),(6,1)])
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_cambio_cli,font=("Helvetica",15)),(0,0)])
pizarra.append([tk.LabelFrame(opciones_labelframes[0],text= "Tarifa"),(7,0)])
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_tarifa_cli,font=("Helvetica",15)),(0,0)])
pizarra.append([tk.LabelFrame(opciones_labelframes[0],text= "Dinero entregado"),(7,1)])
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_entrega_cli,font=("Helvetica",15)),(0,0)])
for i,widget in enumerate(pizarra):
    if len(widget) > 2:
        widget[0].grid(row = widget[1][0],column = widget[1][1],rowspan= widget[2][0],columnspan=widget[2][1])
    else:
        widget[0].grid(row = widget[1][0],column = widget[1][1])

# -------------------------------------------------------------------------- TREEVIEW -------------------------------------------------
# Create a Frame for the Treeview
treeFrame = ttk.Frame(hojas[1])
treeFrame.grid(row=1, column=0)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")
treeScrollx = ttk.Scrollbar(treeFrame,orient="horizontal")
treeScrollx.pack(side="bottom", fill="x")
encabezados = ["N° de Pedido","Fecha","Nombre del cliente","N° de Contacto","Recoleccion","Entrega","Producto","Paga con…","Costo del pedido","Tarifa","Cobro total","Dinero entregado a repartidor para compra","$ entregado al repartidor para cambio","$ total dado al repartidor","$ total recibido por el repartidor"]  

# Treeview
columnas = [i for i in range(1,len(encabezados))]
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, xscrollcommand = treeScrollx.set, columns=columnas, height=30)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)
treeScrollx.config(command=treeview.xview)


# Treeview headings
for i, j in enumerate(encabezados):
    if i == 0:
        treeview.column("#0", width=100)
        treeview.heading("#0", text=j, anchor="center")
    else:
        treeview.heading(i, text=j, anchor="center")
        treeview.column(i, anchor="w", width=100)


##cronometro = CronometroApp(opciones_widgets_1,paginas)

# Ejemplo de uso
ruta_archivo_excel = 'PEDIDITO_DB.xlsx'
nombre_hoja_excel = 'Semana 1 del 21 al 27 de agost'
rango_a_extraer = 'A1:L72'  # Por ejemplo, desde A1 hasta C10

# Cargar el libro de trabajo (workbook)
libro = openpyxl.load_workbook(ruta_archivo_excel)

# Acceder a una hoja específica
hoja = libro[nombre_hoja_excel]

# Extraer información desde el rango especificado
informacion_extraida = extraer_informacion_desde_rango(hoja, rango_a_extraer)
pedidos_totales = len(informacion_extraida)
print("ingreso de base de datos a PEDIDITO SOFTWARE")
for i,fila in enumerate(informacion_extraida):
    mostrar_dicc(treeview,fila)

# Cerrar el libro después de usarlo
libro.close()

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()

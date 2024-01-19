"""
Example script for testing the Forest theme

Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""
import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import openpyxl

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
##        ## Orden
##        # Crear un widget Text
##        self.orden_text_frame = ttk.LabelFrame(self.root, text="Productos")
##        self.orden_text = tk.Text(self.orden_text_frame, height=10, width=40)
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
    agregar_ventana = Agregar_pedido(root,treeview,agregar_rtrn,pedidos_totales)
    agregar_ventana.draw()
## RETURN FUNC; THIUS IS THE GRIDGE BETWEEN THAT WINDOW AN THIS WINDOW
def agregar_rtrn(tree,lista):
    ultimo_indice = tree.get_children()[-1]
    mostrar_dicc(tree,lista,"btn-add")
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


# VENTANA PRINCIPAL
treeview_data = {}
## VENTANA
root = tk.Tk()
root.title("PEDIDITO SYSTEMS TECHNOLOGY by Fernando López V.")
root.option_add("*tearOff", False) # This is always a good idea
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Notebook
cuaderno = ttk.Notebook(root)
encabezados = ['Principal','Clientes','Mapa']
# hojas
hojas = []
# paginas
paginas = []
# labelframe
opciones_principal = ["Nueva Orden","Ordenes Pendientes"]
opciones_labelframes = []
# widgets
opciones_widgets_1 = []
opciones_widgets_2 = []


for i,encabezado in enumerate(encabezados):
    hojas.append(ttk.Frame(cuaderno))
    cuaderno.add(hojas[i], text=encabezado)
    paginas.append(ttk.Frame(hojas[i]))
for i,frame in enumerate(paginas):
    frame.grid(row=0,column=0,padx=0,pady=0)
# -------------------------------------------------------------------------- FRAMES----------------------------------------------------
for i,opcion in enumerate(opciones_principal):
    opciones_labelframes.append([tk.LabelFrame(paginas[0], text=opcion),(0,i)])
    opciones_labelframes[i][0].grid(row = 0, column = i)


opciones_widgets_1.append([tk.Button(opciones_labelframes[0][0],text="(   +   )",command=agregar),(0,0)])
opciones_widgets_1[len(opciones_widgets_1)-1][0].grid(row=0,column=0)
pendientes = 0
opciones_widgets_2.append([tk.Button(opciones_labelframes[1][0],text=f"Ordenes Pendientes : {pendientes}",command=btn_pendientes),(0,0)])
opciones_widgets_2[len(opciones_widgets_2)-1][0].grid(row=0,column=0)
    
cuaderno.grid(row=0,column=0,padx=0,pady=0,sticky="nswe")

# -------------------------------------------------------------------------- TREEVIEW -------------------------------------------------
# Create a Frame for the Treeview
treeFrame = ttk.Frame(hojas[1])
treeFrame.grid(row=1, column=0)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")
treeScrollx = ttk.Scrollbar(treeFrame,orient="horizontal")
treeScrollx.pack(side="bottom", fill="x")

#
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

# Ejemplo de uso
ruta_archivo_excel = 'PEDIDITO_DB.xlsx'
nombre_hoja_excel = 'Semana 1 del 21 al 27 de agost'
rango_a_extraer = 'A1:P72'  # Por ejemplo, desde A1 hasta C10

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


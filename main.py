"""
PEDIDITO SOFTWARE

Author: PolitropicMX
"""
### LIBRERIAS

import pandas as pd
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from cronometro import CronometroApp
from threading import Thread
import time
from agregar_pedido_win import Agregar_pedido
from pendientes_win import Pendientes_class
from analisis_win import Analisis_class
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import Workbook
import openpyxl


#### FUNCIONES DEL PROGRAMA Y OTROS ARCHIVOS

#       ###     #          #
#      #   #   #   #   #    #
#     #       #     # #      #
#   #######   #      #       #
#     #       #     # #      #
#     #       #    #   #     #
#     #        #  #     #   #
#     #         #          #


## El CRONOMETRO CUANDO UNA ORDEN SE INICIA
def iniciar_cronometro(etiqueta, cronometros_activos):
    print("Se inicializo el cronometro")
    cronometro = CronometroApp(etiqueta)
    cronometro.start()
    cronometros_activos.append(cronometro)

def detener_todos_cronometros(cronometros_activos):
    for cronometro in cronometros_activos:
        cronometro.detener()
        
## BUTTON FUNC; ACTIVATED WHEN PRESSED
def agregar():
    iniciar_cronometro(pizarra[6][0], main_cronometro_cli)
    agregar_ventana = Agregar_pedido(root,treeview,agregar_rtrn,pedidos_totales)
##    agregar_ventana.draw()
    # DIBUJATIVA
## RETURN FUNC; THIUS IS THE GRIDGE BETWEEN THAT WINDOW AN THIS WINDOW
def agregar_rtrn(tree,lista):
    lista_de_tiendas = {
                    "1":"Reyes",
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
                    "65":"Hamburguesas al carbon",
                    "66":"Antojitos Mario"
                    }
    productos_main = ''
    costos_unitarios = []
    cantidades = []
    tiendas = list(lista_de_tiendas.values())
    print(f"tienda es: {tiendas}")
    ultimo_indice = tree.get_children()[-1]
    mostrar_dicc(tree,lista,"btn-add")
    orden_sin_terminar.append(lista)
    print(f"orden a añadir : {orden_sin_terminar}")
    main_name_cli.set(lista[1])
    main_num_cli.set(lista[2])
    main_direccion_cli.set(lista[4])
    fecha, hora = lista[0].split(' ')
    print(fecha, hora)
    main_hora_cli.set(f"Hora del Pedido: {hora}")
    main_fecha_cli.set(fecha)
    main_costo_cli.set("")
    main_cambio_cli.set("")
    main_tarifa_cli.set(lista[8])
    main_entrega_cli.set("")
    main_metodo_pago.set(lista[11])
    main_paga_con.set(lista[6])
    productos = procesar_lista_compras(lista[5])
    productos_main = lista[5]
    main_orden_cli.set(lista[5])
    ## TITULOS 
    pizarra.append([tk.Label(pizarra[9][0],text="Productos",font=("Helvetica",15)),(0,0)])
    pizarra.append([tk.Label(pizarra[9][0],text="Cantidad",font=("Helvetica",15)),(0,1)])
    pizarra.append([tk.Label(pizarra[9][0],text="Costo unitario",font=("Helvetica",15)),(0,2)])
    pizarra.append([tk.Label(pizarra[9][0],text="Lo compraron de:",font=("Helvetica",15)),(0,3)])
    
    for i,producto in enumerate(productos):# Aqui hacemos la suma
        # Variable para almacenar la opción seleccionada
        costos_unitarios.append([tk.StringVar(),productos[producto]])
        cantidades.append(productos[producto])
##        print(costos_unitarios[len(costos_unitarios)])
        opciones_var.append(tk.StringVar(pizarra[9][0]))
        opciones_var[i].set(tiendas[0])
        pizarra.append([tk.Label(pizarra[9][0],text=producto,font=("Helvetica",15)),(i+1,0)])
        pizarra.append([tk.Label(pizarra[9][0],text=productos[producto],font=("Helvetica",15)),(i+1,1)])
        pizarra.append([tk.Entry(pizarra[9][0],textvariable=costos_unitarios[len(costos_unitarios)-1][0]),(i+1,2)])
        pizarra.append([tk.Entry(pizarra[9][0]),(i+1,2)])
        pizarra.append([tk.OptionMenu(pizarra[9][0], opciones_var[i], *tiendas),(i+1,3)])
    for i,widget in enumerate(pizarra):
        if len(widget) > 2:
            widget[0].grid(row = widget[1][0],column = widget[1][1],rowspan= widget[2][0],columnspan=widget[2][1])
        else:
            widget[0].grid(row = widget[1][0],column = widget[1][1])
    
def procesar_lista_compras(cadena_lista):# devuelve un diccionario
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
    
def analisis_ventana():
    analisis_win = Analisis_class(root)
    analisis_win.draw()
    
def devolver(data):
    return data

def mostrar_dicc(tree, diccionario, parent=""):
    
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
    fecha_hora_str = fecha_hora_actual.strftime("%A %d de %B %Y\n %H:%M:%S")
    etiqueta.config(text=f"Bienvenido\nhoy es {fecha_hora_str}")
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

## Funcion usada para el --boton:Terminar orden--
def agregar_base_datos():
    def filtrar_y_unir(lista_var):
        tiendas = []
        for i,tienda in enumerate(lista_var):
            contenido = tienda.get()
            tiendas.append(contenido)
        lista_filtrada = list(set(tiendas))  # Convertir a conjunto para eliminar duplicados y luego volver a convertir a lista
        resultado = ', '.join(map(str, lista_filtrada))  # Convertir la lista a cadena separada por coma
        return resultado
    
    
    fecha = main_fecha_cli.get() # Var guarda la fecha
    hora = main_hora_cli.get() # var guarda la hora en que se tomo orden
    nombre = main_name_cli.get() # nombre del cliente
    numero = main_num_cli.get()
    recoleccion = filtrar_y_unir(opciones_var)
    print(recoleccion)
    direccion = main_direccion_cli.get()
    orden = main_orden_cli.get()
    tarifa = main_tarifa_cli.get()
    paga_con = main_paga_con.get()
    costo = main_costo_cli.get()
    cambio = main_cambio_cli.get()
    d_entregado = main_entrega_cli.get()
    metodo_pago = main_metodo_pago.get()
    main_cronometro_cli = []
    pedido = [fecha, hora, nombre, numero, recoleccion, direccion, orden,  paga_con, costo, tarifa,  d_entregado,  metodo_pago, cambio]
    print(f"Este es el pedido {pedido}")
    # Cargar el archivo Excel
    archivo_excel = 'PEDIDITO_DB.xlsx'
    hoja_nombre = 'BASE_PEDIDITO'

    wb = load_workbook(archivo_excel)
    hoja = wb[hoja_nombre]

    # Insertar la nueva fila al principio de la tabla
    hoja.insert_rows(2, amount=1)
    for col_num, value in enumerate(pedido, start=1):
        hoja.cell(row=2, column=col_num, value=value)
    # Guardar el archivo Excel actualizado
    wb.save(archivo_excel)
    for i,widget in enumerate(pizarra):
        
        widget[0].grid_forget()
####    productos = ""
##    for i,producto in enumerate(productos_main):
##        if i == len(productos_main)-1:
##            productos += producto.get()
##        else:
##            productos += producto.get()+","

# Funcion para sumar los numeros y mostrar los resultdos
def sumar_conceptos(event):
    pass

# Función para restar los números y mostrar el resultado
def restar_numeros(event):
    try:
        costo = float(main_costo_cli.get())
        paga_con = float(main_paga_con.get())
        tarifa = float(main_tarifa_cli.get())
        costo_total = costo + tarifa
        main_total_cli.set(costo_total)
        resultado = paga_con - costo_total
        main_cambio_cli.set(resultado)
        suma = 0
        for i,j in enumerate(costos_unitarios):
            costo = j.get()
            suma += costo*cantidades[i]
    except ValueError:
        # Manejar la excepción si los valores ingresados no son números
        pass


##### AQUI EMPIEZA LA APP DE PEDIDITO VENTANA PRINCIPAL #####
    
###       ##
         # #
           #
           #
           #
           #
        #######

    
##### MAPA JERARQUICO
## root
##    cuaderno
##       hojas: encabezados = ['Principal','Buscar','Mapa']
##          paginas
##             opciones_labelframes
##                opciones_widgets_1
##             pizarra


# VENTANA PRINCIPAL
## VENTANA
root = tk.Tk()
root.title("PEDIDITO SYSTEMS TECHNOLOGY by Fernando López V.")
root.option_add("*tearOff", False) # This is always a good idea
# Notebook
cuaderno = ttk.Notebook(root)# jerarquia: 0
encabezados = ['Principal','Buscar','Mapa']
# hojas - Frames de "cuaderno"
hojas = []# jerarquia: 1
# paginas - Frames de "hojas"
paginas = []# jerarquia: 2
# labelframe
opciones_principal = [["Acciones pendientes",(0,0)],["Ordenes Pendientes",(0,1)],["Orden Actual",(1,0)]]
opciones_labelframes = []# jerarquia: 3
# widgets
opciones_widgets_1 = []# jerarquia: 4
opciones_widgets_2 = []# jerarquia: 4
# pizarra
pizarra = []# jerarquia: 2
productos_strvar = []
# opciones_ var
opciones_var = []

# Labelframe 2
opciones_buscar = [["",(0,0)],["Ordenes Pendientes",(0,1)],["Orden Actual",(1,0)]]
opciones_labelframes = []# jerarquia: 3

treeview_data = {}
orden_sin_terminar = []
productos = []
costos_unitarios = []
for i,encabezado in enumerate(encabezados):
    hojas.append(ttk.Frame(cuaderno))
    cuaderno.add(hojas[i], text=encabezado)
    paginas.append(ttk.Frame(hojas[i]))
    paginas[i].grid(row=0,column=0,padx=20,pady=20)


# -------------------------------------------------------------------------- FRAMES----------------------------------------------------
for i,opcion in enumerate(opciones_principal):
    opciones_labelframes.append(tk.LabelFrame(paginas[0], text=opcion[0]))
    opciones_labelframes[i].grid(row = opcion[1][0], column = opcion[1][1])

opciones_widgets_1.append([tk.Button(opciones_labelframes[0],text="(   +   )",command=agregar,font=("Helvetica",25)),(0,0)])
opciones_widgets_1[len(opciones_widgets_1)-1][0].grid(row=opciones_widgets_1[len(opciones_widgets_1)-1][1][0],column=opciones_widgets_1[len(opciones_widgets_1)-1][1][1], sticky = "we")
fecha_actual = datetime.now()
opciones_widgets_1.append([tk.Button(opciones_labelframes[0],text=f"Analisis",command=analisis_ventana,font=("Helvetica",25)),(0,2)])
opciones_widgets_1[len(opciones_widgets_1)-1][0].grid(row=opciones_widgets_1[len(opciones_widgets_1)-1][1][0],column=opciones_widgets_1[len(opciones_widgets_1)-1][1][1])
cuaderno.grid(row=0,column=0,padx=0,pady=0,sticky="EW",columnspan=2)


## PIZARRA WIDGETS
## Label-Fecha
## FECHA Y HORA
##pizarra.append([tk.Label(paginas[0],text=fecha_actual,font=("Helvetica",25)),(1,0),(1,3)])# 0

## Strings del dia
main_ordenes_del_dia = tk.IntVar()

## StringVar's
main_fecha_cli = tk.StringVar()
main_hora_cli = tk.StringVar()
main_name_cli = tk.StringVar()
main_num_cli = tk.StringVar()
main_recoleccion = tk.StringVar()
main_direccion_cli = tk.StringVar()
main_orden_cli = tk.StringVar()
main_paga_con = tk.IntVar()
main_costo_cli = tk.StringVar()
main_tarifa_cli = tk.StringVar()
main_total_cli = tk.StringVar()
main_cambio_cli = tk.StringVar()
main_entrega_cli = tk.StringVar()
main_metodo_pago = tk.StringVar()
main_cronometro_cli = []



##main_cronometro_cli.append(tk.StringVar())
main_ordenes_del_dia.set(0)
main_name_cli.set("El. Eliseo")
main_num_cli.set("Ej. 5530181574")
main_costo_cli.set("Ej. 170")
main_cambio_cli.set("Ej. 20")
main_tarifa_cli.set("Ej. 10")
main_entrega_cli.set("Ej. 210")
main_direccion_cli.set("Ej. Edif 14B 303")
main_hora_cli.set("--:--")

## ESTRUCTURA DE LA PIZARRA
##hojas[0]
##    pi[0]:LB"Pedido actual"
##        pi[1]:L"Nombre del cliente"
##        pi[2]:En
##        pi[3]:L"Hora y fecha"
##        pi[4]:L"Numero del cliente"
##        pi[5]:En
##        pi[6]:L"--:--"
##        pi[7]:L"Direccion del cliente"
##        pi[8]:En
##        pi[9]:LF"Productos"
##        pi[10]:LF"costo"
##            pi[11]:En
##        pi[12]:LF"Cambio"
##            pi[13]:En
##        pi[14]:LF"Tarifa"
##            pi[15]:En
##        pi[16]:LF"Dinero para comprar"
##            pi[17]:En
##        pi[14]:LF"Metodo de pago"
##            pi[15]:En
##        pi[14]:LF"paga con ..."
##            pi[15]:En
##        pi[14]:B"Terminar orden"
# DECLARATIVA 
fechas = tk.Label(hojas[0],text=fecha_actual,font=("Helvetica",25))
fechas.grid(row=1,column=0)
# ACTIVITY 2: TERMINAR ORDEN
actualizar_fecha(fechas)
pizarra.append([tk.LabelFrame(hojas[0],text= "Pedido Actual"),(2,0)])# 0
pizarra.append([tk.Label(pizarra[0][0],text= "Nombre del cliente"),(0,0)])# 1
pizarra.append([tk.Entry(pizarra[0][0],textvariable=main_name_cli,font=("Helvetica",15)),(0,1)])# 2
pizarra.append([tk.Label(pizarra[0][0],textvariable=main_hora_cli),(0,2)])# 3
pizarra.append([tk.Label(pizarra[0][0],text= "Numero del cliente"),(1,0)])# 4
pizarra.append([tk.Entry(pizarra[0][0],textvariable=main_num_cli,font=("Helvetica",15)),(1,1)])# 5
pizarra.append([tk.Label(pizarra[0][0],text="--:--"),(1,2)])# 6
pizarra.append([tk.Label(pizarra[0][0],text= "Dirección del cliente"),(2,0)])# 7
pizarra.append([tk.Entry(pizarra[0][0],textvariable=main_direccion_cli,font=("Helvetica",15)),(2,1)])# 8
pizarra.append([tk.LabelFrame(pizarra[0][0],text= "Productos"),(3,0),(1,2)])# 9 Recuerda Cambiar
pizarra.append([tk.LabelFrame(pizarra[0][0],text= "Costo"),(4,0)])# 10
pizarra[len(pizarra)-1][0].bind('<FocusOut>', restar_numeros) 
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_costo_cli,font=("Helvetica",13)),(0,0)])## 11
pizarra.append([tk.LabelFrame(pizarra[0][0],text= "Cambio"),(4,1)])# 12
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_cambio_cli,font=("Helvetica",15)),(0,0)])# 13
pizarra.append([tk.LabelFrame(pizarra[0][0],text= "Tarifa"),(5,0)])# 14
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_tarifa_cli,font=("Helvetica",15)),(0,0)])# 15
pizarra[len(pizarra)-1][0].bind('<FocusOut>', restar_numeros) 
pizarra.append([tk.LabelFrame(pizarra[0][0],text= "Dinero para comprar"),(5,1)])# 16
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_entrega_cli,font=("Helvetica",15)),(0,0)])# 17
pizarra[len(pizarra)-1][0].bind('<FocusOut>', restar_numeros) 
pizarra.append([tk.LabelFrame(pizarra[0][0],text= "Metodo de Pago"),(6,0)])#18
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_metodo_pago,font=("Helvetica",15)),(0,0)])# 19
pizarra.append([tk.LabelFrame(pizarra[0][0],text= "Paga con..."),(6,1)])# 20
pizarra.append([tk.Entry(pizarra[len(pizarra)-1][0],textvariable=main_paga_con,font=("Helvetica",15)),(0,0)])# 21
pizarra[len(pizarra)-1][0].bind('<FocusOut>', restar_numeros) 
pizarra.append([tk.Button(pizarra[0][0],text="Terminar Orden",font=("Helvetica",15),command=agregar_base_datos),(7,0)])#22

##for i,widget in enumerate(pizarra):
##        if len(widget) > 2:
##            widget[0].grid(row = widget[1][0],column = widget[1][1],rowspan= widget[2][0],columnspan=widget[2][1])
##        else:
##            widget[0].grid(row = widget[1][0],column = widget[1][1])

# -------------------------------------------------------------------------- TREEVIEW -------------------------------------------------
# Create a Frame for the Treeview
treeFrame = ttk.Frame(hojas[1])
treeFrame.grid(row=1, column=0)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")
treeScrollx = ttk.Scrollbar(treeFrame,orient="horizontal")
treeScrollx.pack(side="bottom", fill="x")
encabezados = ["N° de Pedido","Fecha","Hora del pedido","Nombre del cliente","N° de Contacto","Recoleccion","Entrega","Producto","Paga con…","Costo del pedido","Tarifa","Cobro total","Dinero entregado a repartidor para compra","$ entregado al repartidor para cambio","$ total dado al repartidor","$ total recibido por el repartidor"]  

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
nombre_hoja_excel = 'BASE_PEDIDITO'
rango_a_extraer = 'A2:K1500'  # Por ejemplo, desde A1 hasta C10

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

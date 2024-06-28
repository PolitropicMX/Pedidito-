import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from cronometro import CronometroApp
import openpyxl
from threading import Thread
import time

### UN WIDGET SE COMPONE DE 4 LINEAS DE CODIGO
### EL PASO CERO ES CREAR UN OBJETO QUE ALMACENE UN VALOR DE UN WIDGET, PERTENECIENTE A LA CLASE TKINTER, COMO StringVar()
### PRIMERO SE DECLARA EL WIDGET, INDICANDO EL TEXTO QUE CMOSTRARÁ Y EL RECIPIENTE QUE LO CONTENDRÁ
### Y LA SEGUNDA LINEA INDICA EN QUÉ POSICIÓN ESTARÁ EN EL WIDGET PADRE
### LA TERCERA, QUE AL IGUAL A LA LINEA CERO SON OPCIONALES DEPENDIENDO EL WIDGET

class Agregar_pedido:
    def __init__(self,root,tree,func_rtrn,pedidos):
        ### ABOUT
        ### ESTA ES UNA FUNCION CONSTRUCTOR DONDE SE DECLARAN LOS WIDGETS QUE FORMAN LA VENTANA

         # #
           #
           #
           #
           #
        #######
           
        self.pedidos = pedidos
        self.return_func = func_rtrn## Funcion de retorno a la ventana principal o ventana padre
        self.tree = tree# el treeview de la ventana principal o ventana padre
        ## CODIGO PARA ESTRAER FECHAY HORA
        ahora = datetime.now()
        self.fecha_y_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")
        self.opciones_var = []
        self.lista_de_tiendas = {
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

        ##      ESTRUCTURA DE LA VENTANA
##        root
##            orden_text_frame
##                orden_text
##            check_frame
##                direc_cliente_frame
##                    direc_cliente_entry
##                nombre_cliente_frame
##                    nombre_cliente_entry
##                num_cliente_frame
##                    num_cliente_entry
##                tarifa_frame
##                    tarifa_entry
##                radio_frame
##                    radio_metodos_de_pago
##                    metodo_pago_label
##                    metodo_pago_frame
##                        efectivo_widgets
##                        transferencia_widgets
##                widgets_frame
##                    botones_button
##            hora_label
    
##        ## FRAME
##        # ESTRUCTURA DEL primera_activity
##        p_a[0]:LB"Detalles del pedido"(0,1,3,3
##            p_a[2]:LB"Direccion de entrega"
##                p_a[3]:En
##            p_a[4]:LB"Nombre cliente"
##                p_a[5]:En
##            p_a[6]:LB"Nombre cliente"
##                p_a[7]:En
##            p_a[8]:LB"Nombre cliente"
##                p_a[9]:En
##            p_a[12]:LB"Metodo de pago"
##                p_a[13]
##                p_a[14]
##                p_a[15]
##                p_a[15]:LB"No ha selecciónado\n metodo de pago"
##                p_a[16]:F
##            p_a[21]:LB""
##                p_a[22]:B"Guardar"
##                p_a[23]:B"Cancelar"
##        p_a[1]:L"fecha y hora"
##        p_a[10]:LB"Productos"
##            p_a[11]:Textbox
            
## TODOS LOS WIDGETS A USAR ------------------------------------------------------------------------------------------------------------------------------------


        ## StringVar's
        self.main_fecha_cli = tk.StringVar()
        self.main_hora_cli = tk.StringVar()
        self.main_name_cli = tk.StringVar()
        self.main_num_cli = tk.StringVar()
        self.main_recoleccion = tk.StringVar()
        self.main_direccion_cli = tk.StringVar()
        self.main_orden_cli = tk.StringVar()
        self.main_paga_con = tk.IntVar()
        self.main_costo_cli = tk.StringVar()
        self.main_tarifa_cli = tk.StringVar()
        self.main_total_cli = tk.StringVar()
        self.main_cambio_cli = tk.StringVar()
        self.main_entrega_cli = tk.StringVar()
        self.main_metodo_pago = tk.StringVar()
        self.main_cronometro_cli = []

        ## VENTANA
        self.root = tk.Toplevel(root,bg="#046546")# 0
        
        self.activity = "primera activity"
        self.primera_activity = []
        self.primera_activity.append([ttk.LabelFrame(self.root, text="Detalles del Pedido"),(1,0,3,3,"nsew")])# 0
        self.primera_activity.append([tk.Label(self.root,text=self.fecha_y_hora),(0,0,5,5,"nwes")])# 1
        self.primera_activity.append([ttk.LabelFrame(self.primera_activity[0][0], text="Dirección de Entrega"),(0,0,0,0,"nwes")])# 2
        self.primera_activity.append([ttk.Entry(self.primera_activity[2][0],textvariable=self.main_direccion_cli ),(0,0,5,5,"ew")])# 3
        self.primera_activity[len(self.primera_activity)-1][0].insert(0, "Purisima 55")
        self.primera_activity[len(self.primera_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.primera_activity[3][0]))# Asociar la función borrar_texto al evento clic
        self.primera_activity.append([ttk.LabelFrame(self.primera_activity[0][0], text="Nombre Cliente", padding=(20, 10)),(0,1,5,5,"nwes")])# 4
        self.primera_activity.append([ttk.Entry(self.primera_activity[4][0]),(0,0,0,0,"ew")])# 5
        self.primera_activity[len(self.primera_activity)-1][0].insert(0, "Tierno")
        self.primera_activity[len(self.primera_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.primera_activity[5][0]))# Asociar la función borrar_texto al evento clic
        self.primera_activity.append([ttk.LabelFrame(self.primera_activity[0][0], text="Numero celular", padding=(20, 10)),(1,0,0,0,"nsew")])# 6
        self.primera_activity.append([ttk.Entry(self.primera_activity[6][0]),(0,0,0,0,"")])# 7
        self.primera_activity[len(self.primera_activity)-1][0].insert(0, "5510293483")
        self.primera_activity[len(self.primera_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.primera_activity[7][0]))# Asociar la función borrar_texto al evento clic
        self.primera_activity.append([ttk.LabelFrame(self.primera_activity[0][0], text="Tarifa $MXN", padding=(20, 10)),(1,1,0,0,"nswe")])# 8
        self.primera_activity.append([ttk.Entry(self.primera_activity[8][0]),(0,0,0,0,"ew")])# 9
        self.primera_activity[len(self.primera_activity)-1][0].insert(0, 10)
        self.primera_activity[len(self.primera_activity)-1][0].bind("<Button-1>", lambda event: self.borrar_texto(self.primera_activity[9][0]))# Asociar la función borrar_texto al evento clic
        ## Orden
        # Crear un widget Text
        self.primera_activity.append([ttk.LabelFrame(self.root, text="Productos"),(2,0,0,0,"")])# 10
        self.primera_activity.append([tk.Text(self.primera_activity[10][0], height=10, width=40),(0,0,0,0,"")])# 11
        # Create a Frame for the Radiobuttons
        self.primera_activity.append([ttk.LabelFrame(self.primera_activity[0][0], text="Metodo de Pago", padding=(20, 10)),(2,0,0,0,"")])# 12
        # Radiobuttons
        self.metodos_de_pago = ["Efectivo","Transferencia"]
        self.var_metodos_de_pago = tk.StringVar()
        self.var_metodos_de_pago.set(None)
        for i,metodo in enumerate(self.metodos_de_pago):# 13-14
            self.primera_activity.append([tk.Radiobutton(self.primera_activity[12][0], text=metodo, variable=self.var_metodos_de_pago, value=metodo, command = self.metodo_pago_func),(i,0,0,0,"")])# 13
        self.primera_activity.append([tk.Label(self.primera_activity[12][0], text="No ha selecciónado\n metodo de pago"),(0,1,0,0,"")])# 15
        self.primera_activity.append([tk.Frame(self.primera_activity[12][0]),(1,1,0,0,"")])# 16
        self.paga_con = tk.StringVar()
        self.primera_activity.append([tk.Entry(self.primera_activity[12][0],textvariable=self.paga_con),(2,1,0,0,"")])# 17
        self.primera_activity.append([tk.Label(self.primera_activity[12][0], text= f"Numero de Tarjeta:\nXXXX-XXXX-XXXX-XXXX"),(3,1,20,20,"")])# 18
        self.primera_activity.append([tk.Button(self.primera_activity[12][0], text="Copiar Numero de cuenta"),(4,1,0,0,"")])#19
        # BOTONES
        self.primera_activity.append([ttk.Frame(self.primera_activity[0][0]),(3,0,0,0,"nsew")])#20
        self.botones = [("Guardar",self.guardar_f,(0,0,0,0,"")),("Cancelar",self.cancelar_f,(0,1,0,0,""))]
        for i in self.botones:# 22-23
            self.primera_activity.append([ttk.Button(self.primera_activity[20][0], text=i[0],command=i[1]),i[2]])


        



        ##self.main_cronometro_cli.append(tk.StringVar())
        self.main_name_cli.set("El. Eliseo")
        self.main_num_cli.set("Ej. 5530181574")
        self.main_costo_cli.set("Ej. 170")
        self.main_cambio_cli.set("Ej. 20")
        self.main_tarifa_cli.set("Ej. 10")
        self.main_entrega_cli.set("Ej. 210")
        self.main_direccion_cli.set("Ej. Edif 14B 303")
        self.main_hora_cli.set("--:--")
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
        self.draw(self.primera_activity)
        self.pizarra =[]
        self.pizarra.append([tk.LabelFrame(self.root,text= "Pedido Actual"),(0,0,0,0,"")])# 0
        self.pizarra.append([tk.Label(self.pizarra[0][0],text= "Nombre del cliente"),(0,0,0,0,"")])# 1
        self.pizarra.append([tk.Entry(self.pizarra[0][0],textvariable=self.main_name_cli,font=("Helvetica",15)),(0,1,0,0,"")])# 2
        self.pizarra.append([tk.Label(self.pizarra[0][0],textvariable=self.main_hora_cli),(0,2,0,0,"")])# 3
        self.pizarra.append([tk.Label(self.pizarra[0][0],text= "Numero del cliente"),(1,0,0,0,"")])# 4
        self.pizarra.append([tk.Entry(self.pizarra[0][0],textvariable=self.main_num_cli,font=("Helvetica",15)),(1,1,0,0,"")])# 5
        self.pizarra.append([tk.Label(self.pizarra[0][0],text="--:--"),(1,2,0,0,"")])# 6
        self.pizarra.append([tk.Label(self.pizarra[0][0],text= "Dirección del cliente"),(2,0,0,0,"")])# 7
        self.pizarra.append([tk.Entry(self.pizarra[0][0],textvariable=self.main_direccion_cli,font=("Helvetica",15)),(2,1,0,0,"")])# 8
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Productos"),(3,0,0,0,"")])# 9 Recuerda Cambiar
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Costo"),(4,0,0,0,"")])# 10
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_costo_cli,font=("Helvetica",13)),(0,0,0,0,"")])## 11
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Cambio"),(4,1,0,0,"")])# 12
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_cambio_cli,font=("Helvetica",15)),(0,0,0,0,"")])# 13
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Tarifa"),(5,0,0,0,"")])# 14
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_tarifa_cli,font=("Helvetica",15)),(0,0,0,0,"")])# 15
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Dinero para comprar"),(5,1,0,0,"")])# 16
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_entrega_cli,font=("Helvetica",15)),(0,0,0,0,"")])# 17
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Metodo de Pago"),(6,0,0,0,"")])#18
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_metodo_pago,font=("Helvetica",15)),(0,0,0,0,"")])# 19
        self.pizarra.append([tk.LabelFrame(self.pizarra[0][0],text= "Paga con..."),(6,1,0,0,"")])# 20
        self.pizarra.append([tk.Entry(self.pizarra[len(self.pizarra)-1][0],textvariable=self.main_paga_con,font=("Helvetica",15)),(0,0,0,0,"")])# 21
        self.pizarra[len(self.pizarra)-1][0].bind('<FocusOut>', self.restar_numeros) 
        self.pizarra.append([tk.Button(self.pizarra[0][0],text="Terminar Orden",font=("Helvetica",15)),(7,0,0,0,"")])#22
                                    
##        # A transformar!
##        self.check_frame = ttk.LabelFrame(self.root, text="Detalles del Pedido", padding=(20, 10))
##        ## TITULO: HORA
##        self.hora_label = tk.Label(self.root,text=self.fecha_y_hora)
##        ## FRAME: DIRECCIÓN DE ENTREGA
##        self.direc_cliente_frame = ttk.LabelFrame(self.check_frame, text="Dirección de Entrega", padding=(20, 10))
##        ## ENTRY: DIRECCIÓN DE ENTREGA
##        self.direc_cliente_entry = ttk.Entry(self.direc_cliente_frame)
##        self.direc_cliente_entry.insert(0, "Purisima 55")
##        self.direc_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(self.direc_cliente_entry))# Asociar la función borrar_texto al evento clic
##        ## NOMBRE DEL CLIENTE
##        self.nombre_cliente_frame = ttk.LabelFrame(self.check_frame, text="Nombre Cliente", padding=(20, 10))
##        self.nombre_cliente_entry = ttk.Entry(self.nombre_cliente_frame)
##        self.nombre_cliente_entry.insert(0, "Tierno")
##        self.nombre_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(self.nombre_cliente_entry))# Asociar la función borrar_texto al evento clic
##        ## NUMERO DEL CLIENTE
##        self.num_cliente_frame = ttk.LabelFrame(self.check_frame, text="Numero celular", padding=(20, 10))
##        self.num_cliente_entry = ttk.Entry(self.num_cliente_frame)
##        self.num_cliente_entry.insert(0, "5510293483")
##        self.num_cliente_entry.bind("<Button-1>", lambda event: self.borrar_texto(self.num_cliente_entry))# Asociar la función borrar_texto al evento clic
##        ## TARIFA
##        self.tarifa_frame = ttk.LabelFrame(self.check_frame, text="Tarifa $MXN", padding=(20, 10))
##        self.tarifa_entry = ttk.Entry(self.tarifa_frame)
##        self.tarifa_entry.insert(0, 10)
##        self.tarifa_entry.bind("<Button-1>", lambda event: self.borrar_texto(self.tarifa_entry))# Asociar la función borrar_texto al evento clic
##        ## Orden
##        # Crear un widget Text
##        self.orden_text_frame = ttk.LabelFrame(self.root, text="Productos")
##        self.orden_text = tk.Text(self.orden_text_frame, height=10, width=40)
##        # Create a Frame for the Radiobuttons
##        self.radio_frame = ttk.LabelFrame(self.check_frame, text="Lista de articulos", padding=(20, 10))
##        # Radiobuttons
##        self.metodos_de_pago = ["Efectivo","Transferencia"]
##        self.var_metodos_de_pago = tk.StringVar()
##        self.var_metodos_de_pago.set(None)
##        self.radio_metodos_de_pago = [tk.Radiobutton(self.radio_frame, text=metodo, variable=self.var_metodos_de_pago, value=metodo, command = lambda o = metodo:self.metodo_pago_func(o)) for i,metodo in enumerate(self.metodos_de_pago)]
##        self.metodo_pago_label = tk.Label(self.radio_frame, text="No ha selecciónado\n metodo de pago")
##        self.metodo_pago_frame = tk.Frame(self.radio_frame)
##        self.paga_con = tk.StringVar()
##        self.efectivo_widgets = [[tk.Entry(self.metodo_pago_frame,textvariable=self.paga_con),(0,0)]]
##        self.transferencia_widgets = [[tk.Label(self.metodo_pago_frame, text= f"Numero de Tarjeta:\nXXXX-XXXX-XXXX-XXXX"),(0,0)],
##                                 [tk.Button(self.metodo_pago_frame, text="Copiar Numero de cuenta"),(1,0)]]
##        # BOTONES
##        self.widgets_frame = ttk.Frame(self.check_frame)
##        self.botones = [("Guardar",self.guardar_f),("Cancelar",self.cancelar_f)]
##        self.botones_button = [ttk.Button(self.widgets_frame, text=i[0],command=i[1] ) for i in self.botones]

    def guardar_f(self):
        orden = str(self.primera_activity[11][0].get("1.0", "end-1c"))
        print(f" Orden es : {orden}")
        if orden == "":
            messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia.")
        else:
            dicc_orden = self.procesar_lista_compras(orden)
            print(dicc_orden)
            # "N° de Pedido","Fecha","Nombre del cliente","N° de Contacto","Recoleccion","Entrega","Producto","Paga con…","Costo del pedido","Tarifa","Cobro total","Dinero entregado a repartidor para compra","$ entregado al repartidor para cambio","$ total dado al repartidor","$ total recibido por el repartidor"]  

            direccion = self.primera_activity[3][0].get()
            nombre = self.primera_activity[5][0].get()
            numero = self.primera_activity[7][0].get()
            orden = self.primera_activity[11][0].get("1.0", "end-1c")
            tarifa = self.primera_activity[9][0].get()
            metodo_pago = self.var_metodos_de_pago.get()
            paga_con = self.paga_con.get()
            list_cli = [self.fecha_y_hora,#0
                        nombre,#1
                        numero,#2
                        "No especificado",#3
                        direccion,#4
                        orden,#5
                        paga_con,#6
                        "No especificado",#7
                        tarifa,#8
                        "No especificado",#9
                        "No especificado",#10
                        metodo_pago # 11
                        ]
            lista = ["No especificado",str(self.fecha_y_hora),nombre,numero,"No especificado",direccion,orden,"No especificado","No especificado",tarifa,"No especificado","No especificado","No especificado","No especificado","No especificado"]
##            self.return_func(self.tree,list_cli)
##            self.root.destroy()
        self.erase(self.primera_activity)
        self.draw(self.pizarra)
        productos_main = ''
        costos_unitarios = []
        cantidades = []
        tiendas = list(self.lista_de_tiendas.values())
        print(f"tienda es: {tiendas}")
##        ultimo_indice = tree.get_children()[-1]
##        mostrar_dicc(tree,lista,"btn-add")
##        orden_sin_terminar.append(lista)
##        print(f"orden a añadir : {orden_sin_terminar}")
        self.main_name_cli.set(lista[2])
        self.main_num_cli.set(lista[3])
        self.main_direccion_cli.set(lista[5])
        fecha, hora = lista[0].split(' ')
        print(fecha, hora)
        self.main_hora_cli.set(f"Hora del Pedido: {hora}")
        self.main_fecha_cli.set(fecha)
        self.main_costo_cli.set("")
        self.main_cambio_cli.set("")
        self.main_tarifa_cli.set(lista[9])
        self.main_entrega_cli.set("")
        self.main_metodo_pago.set(lista[12])
        self.main_paga_con.set(lista[7])
        productos = self.procesar_lista_compras(lista[6])
        productos_main = lista[5]
        self.main_orden_cli.set(lista[5])
        ## TITULOS 
        self.pizarra.append([tk.Label(self.pizarra[9][0],text="Productos",font=("Helvetica",15)),(0,0,0,0,"")])
        self.pizarra.append([tk.Label(self.pizarra[9][0],text="Cantidad",font=("Helvetica",15)),(0,1,0,0,"")])
        self.pizarra.append([tk.Label(self.pizarra[9][0],text="Costo unitario",font=("Helvetica",15)),(0,2,0,0,"")])
        self.pizarra.append([tk.Label(self.pizarra[9][0],text="Lo compraron de:",font=("Helvetica",15)),(0,3,0,0,"")])
        
        for i,producto in enumerate(productos):# Aqui hacemos la suma
            # Variable para almacenar la opción seleccionada
            costos_unitarios.append([tk.StringVar(),productos[producto]])
            cantidades.append(productos[producto])
    ##        print(costos_unitarios[len(costos_unitarios)])
            self.opciones_var.append(tk.StringVar(self.pizarra[9][0]))
            self.opciones_var[i].set(tiendas[0])
            self.pizarra.append([tk.Label(self.pizarra[9][0],text=productos[producto],font=("Helvetica",15)),(i+1,1)])
            self.pizarra.append([tk.Entry(self.pizarra[9][0],textvariable=costos_unitarios[len(costos_unitarios)-1][0]),(i+1,2)])
            self.pizarra.append([tk.Entry(self.pizarra[9][0]),(i+1,2)])
            self.pizarra.append([tk.OptionMenu(self.pizarra[9][0], self.opciones_var[i], *tiendas),(i+1,3)])
        for i,widget in enumerate(self.pizarra):
            if len(widget) > 2:
                widget[0].grid(row = widget[1][0],column = widget[1][1],rowspan= widget[2][0],columnspan=widget[2][1])
            else:
                widget[0].grid(row = widget[1][0],column = widget[1][1])
    def cancelar_f(self):
        self.root.destroy()

    ### METODO DE PAGO: RADIOBUTTONS COMMAND
    def metodo_pago_func(self):
        metodo = self.var_metodos_de_pago.get()
        self.primera_activity[15][0].config(text=f"Pagará con:\n{metodo}")
        print(f"Metodo es : {metodo}")
        self.diccionarios_widgets = {"Efectivo":self.primera_activity[13][0],"Transferencia":self.primera_activity[14][0]}
        print(self.diccionarios_widgets.values())
        for i,conjunto in enumerate(self.diccionarios_widgets.values()):
            print(f"conjunto {i} es : {conjunto}")
            conjunto.grid_forget()
##            for j, widget in enumerate(conjunto):
##                print(f"widget {j} es: {widget}")
##                widget.grid_forget()
##        for i,lista in enumerate(self.diccionarios_widgets[metodo]):
##            lista[0].grid(row=lista[1][0],column=lista[1][1])
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
        
    def draw(self,activity):
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

        for i,widget in enumerate(activity):
            widget[0].grid(row=widget[1][0],column=widget[1][1],padx= widget[1][2],pady = widget[1][3],sticky= widget[1][4])
    def erase(self,activity):
        for i,widget in enumerate(activity):
            widget[0].grid_forget()

    
##        self.check_frame.grid(row=2, column=0, padx=(3), pady=(3), sticky="nsew")
##        self.hora_label.grid(row=0, column=0, padx=(3), pady=(3), sticky="nsew")
##
##        self.direc_cliente_frame.grid(row=0, column=0, sticky="nsew")
##        self.direc_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
##
##        self.nombre_cliente_frame.grid(row=1, column=0, sticky="nsew")
##        self.nombre_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
##
##        self.num_cliente_frame.grid(row=1, column=1, sticky="nsew")
##        self.num_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
##
##        self.tarifa_frame.grid(row=0, column=1, sticky="nsew")
##        self.tarifa_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")
##        
##        self.orden_text_frame.grid(row=1, column=0, sticky="nsew")
##        self.orden_text.pack(pady=10)
##
##        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
##        
##        for i,radio in enumerate(self.radio_metodos_de_pago):            
##            radio.grid(row=i, column=0, sticky="nsew")
##        self.metodo_pago_label.grid(row=0,column=1)
##        self.metodo_pago_frame.grid(row=1,column=1)
##        for i,btn in enumerate(self.botones_button):
##            btn.grid(row=0, column=i, sticky="nsew")
##        self.widgets_frame.grid(row=3, column=0, sticky="nsew")

    def get_data(self,func):
        
        data = [self.fecha_y_hora,direccion, nombre, numero, orden]
        func(data)
        
    def borrar_texto(self,entry):
        # Borra el texto dentro del Entry al recibir un clic
        entry.delete(0, tk.END)
    # Función para restar los números y mostrar el resultado
    def restar_numeros(self,event):
        try:
            costo = float(self.main_costo_cli.get())
            paga_con = float(self.main_paga_con.get())
            tarifa = float(self.main_tarifa_cli.get())
            costo_total = costo + tarifa
            self.main_total_cli.set(costo_total)
            resultado = paga_con - costo_total
            self.main_cambio_cli.set(resultado)
            suma = 0
            for i,j in enumerate(costos_unitarios):
                costo = j.get()
                suma += costo*cantidades[i]
        except ValueError:
            # Manejar la excepción si los valores ingresados no son números
            pass
##    def agregar_rtrn(self,lista):
##        
##        productos_main = ''
##        costos_unitarios = []
##        cantidades = []
##        tiendas = list(self.lista_de_tiendas.values())
##        print(f"tienda es: {tiendas}")
####        ultimo_indice = tree.get_children()[-1]
####        mostrar_dicc(tree,lista,"btn-add")
##        orden_sin_terminar.append(lista)
##        print(f"orden a añadir : {orden_sin_terminar}")
##        self.main_name_cli.set(lista[1])
##        self.main_num_cli.set(lista[2])
##        self.main_direccion_cli.set(lista[4])
##        fecha, hora = lista[0].split(' ')
##        print(fecha, hora)
##        main_hora_cli.set(f"Hora del Pedido: {hora}")
##        main_fecha_cli.set(fecha)
##        main_costo_cli.set("")
##        main_cambio_cli.set("")
##        main_tarifa_cli.set(lista[8])
##        main_entrega_cli.set("")
##        main_metodo_pago.set(lista[11])
##        main_paga_con.set(lista[6])
##        productos = procesar_lista_compras(lista[5])
##        productos_main = lista[5]
##        main_orden_cli.set(lista[5])
##        ## TITULOS 
##        pizarra.append([tk.Label(pizarra[9][0],text="Productos",font=("Helvetica",15)),(0,0)])
##        pizarra.append([tk.Label(pizarra[9][0],text="Cantidad",font=("Helvetica",15)),(0,1)])
##        pizarra.append([tk.Label(pizarra[9][0],text="Costo unitario",font=("Helvetica",15)),(0,2)])
##        pizarra.append([tk.Label(pizarra[9][0],text="Lo compraron de:",font=("Helvetica",15)),(0,3)])
##        
##        for i,producto in enumerate(productos):# Aqui hacemos la suma
##            # Variable para almacenar la opción seleccionada
##            costos_unitarios.append([tk.StringVar(),productos[producto]])
##            cantidades.append(productos[producto])
##    ##        print(costos_unitarios[len(costos_unitarios)])
##            opciones_var.append(tk.StringVar(pizarra[9][0]))
##            opciones_var[i].set(tiendas[0])
##            pizarra.append([tk.Label(pizarra[9][0],text=producto,font=("Helvetica",15)),(i+1,0)])
##            pizarra.append([tk.Label(pizarra[9][0],text=productos[producto],font=("Helvetica",15)),(i+1,1)])
##            pizarra.append([tk.Entry(pizarra[9][0],textvariable=costos_unitarios[len(costos_unitarios)-1][0]),(i+1,2)])
##            pizarra.append([tk.Entry(pizarra[9][0]),(i+1,2)])
##            pizarra.append([tk.OptionMenu(pizarra[9][0], opciones_var[i], *tiendas),(i+1,3)])
##        for i,widget in enumerate(pizarra):
##            if len(widget) > 2:
##                widget[0].grid(row = widget[1][0],column = widget[1][1],rowspan= widget[2][0],columnspan=widget[2][1])
##            else:
##                widget[0].grid(row = widget[1][0],column = widget[1][1])
    def procesar_lista_compras(self,cadena_lista):# devuelve un diccionario
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

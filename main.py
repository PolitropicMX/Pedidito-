"""
Example script for testing the Forest theme

Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""


import tkinter as tk
from tkinter import ttk
from datetime import datetime


class Agregar_pedido:
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
        self.direc_cliente_frame = ttk.LabelFrame(self.check_frame, text="Dirección de Entrega", padding=(20, 10))
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
        self.radio_frame = ttk.LabelFrame(self.check_frame, text="Metodo de Pago", padding=(20, 10))
        # Radiobuttons
        self.metodos_de_pago = ["Efectivo","Transferencia"]
        self.var_metodos_de_pago = tk.StringVar(value='') 
        self.radio_metodos_de_pago = [tk.Radiobutton(self.radio_frame, text=metodo, variable=self.var_metodos_de_pago, value=metodo) for i,metodo in enumerate(self.metodos_de_pago)]
        # BOTONES
        self.widgets_frame = ttk.Frame(self.check_frame)
        self.botones = ["Guardar","Cancelar"]
        self.botones_button = [ttk.Button(self.widgets_frame, text=i) for i in self.botones]

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
        direccion = self.direc_cliente_entry.get()
        nombre = self.nombre_cliente_entry.get()
        numero = self.num_cliente_entry.get()
        orden = self.orden_text.get()
        data = [self.fecha_y_hora,direccion, nombre, numero, orden]
        func(data)
    def borrar_texto(self,entry):
        # Borra el texto dentro del Entry al recibir un clic
        entry.delete(0, tk.END)


def agregar():
    agregar_ventana = Agregar_pedido(root)
    agregar_ventana.draw()
def devolver(data):
    return data
def mostrar_dicc(tree, diccionario, parent=""):# args: (treeview object, dict, (optional) parent)
    for key, value in diccionario.items():
        if isinstance(value, dict):
            # Si el valor es un diccionario, recurrir de forma recursiva
            nuevo_parent = tree.insert(parent, 'end', text=str(key), open=True)
##                print(f' Nuevo parent es : {nuevo_parent}')
            mostrar_dicc(tree, value, parent=nuevo_parent)
        else:
            # Si el valor no es un diccionario, agregarlo como un elemento
            tree.insert(parent, 'end', text=str(key), values=(str(value)))
def cap_pedido():
    pass
root = tk.Tk()
root.title("PEDIDITO SYSTEMS TECHNOLOGY by Fernando López V.")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)



# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

e = tk.StringVar(value=option_menu_list[1])




# Notebook
notebook = ttk.Notebook(root)

# Paginas

encabezados = ['Principal','Clientes','Mapa']
paginas = [ttk.Frame(notebook) for i,encabezado in enumerate(encabezados)]
for i,encabezado in enumerate(encabezados):
    notebook.add(paginas[i], text=encabezado)
widget_frames = [ttk.Frame(paginas[i]) for i,encabezado in enumerate(encabezados)]
for i,frame in enumerate(widget_frames):
    frame.grid(row=0,column=0,padx=0,pady=0)
widgets_1 = [
    # Accentbutton
##    [tk.LabelFrame(widget_frames[0], text="Pagina_1")],
    [ttk.Button(widget_frames[0], text="Pagina_1", style="Accent.TButton", command = agregar),(1,0)],
    [ttk.Entry(widget_frames[0]),(0,0)]
    ]

widgets_2 = [
    # Accentbutton
    [ttk.Button(widget_frames[1], text="Pagina_1", style="Accent.TButton", command = agregar),(1,0)],
    [ttk.Entry(widget_frames[1]),(0,0)],
    ]
for i,j in enumerate(widgets_1):
##    j[0].pack()
    j[0].grid(row=j[1][0],column=j[1][1],padx=20,pady=20)
for i,j in enumerate(widgets_2):
    widgets_2[i][0].grid(row=widgets_2[i][1][0],column=widgets_2[i][1][1],padx=20,pady=20)
    
notebook.grid(row=0,column=0,padx=0,pady=0,sticky="we")
# -------------------------------------------------------------------------- FRAMES----------------------------------------------------
opciones_principal = ["Nueva Orden","Ordenes Pendientes"]
labelframes = [tk.LabelFrame(notebook, text=opcion) for i,opcion in enumerate(opciones_principal)]
for i,lb in enumerate(labelframes):
    lb.grid(row = 0, column = i)
nueva_orden_widgets = [tk.Button(labelframes[0],text="(   +   )",command=agregar)]
nueva_orden_widgets[0].grid(row=0,column=0)
pendientes = 0
orden_pendiente = [tk.Button(labelframes[1],text=f"Ordenes Pendientes : {pendientes}")]
orden_pendiente[0].grid(row=0,column=0)
# -------------------------------------------------------------------------- TREEVIEW -------------------------------------------------
# Create a Frame for the Treeview
treeFrame = ttk.Frame(root)
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
print(columnas)
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

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=2,column=2)

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()


"""
Example script for testing the Forest theme

Author: rdbende
License: MIT license
Source: https://github.com/rdbende/ttk-widget-factory
"""


import tkinter as tk
from tkinter import ttk


class Agregar_pedido:
    def __init__(self,root):
        
        ## MAPA JERARQUICO DE WIDGETS
        ## root
        ##     detalles del pedido
        ##         direccion_de_entrega:entry
        ##         nombre:entry
        ##         numero:entry
        ##         metodo de pago
        ##         tarifa
        ##     productos
        ##         orden: text

        ## TODOS LOS WIDGETS A USAR ------------------------------------------------------------------------------------------------------------------------------------
        # Create a Frame for the Checkbuttons
        self.root = tk.Toplevel(root,bg="#046546")# 0
        self.check_frame = ttk.LabelFrame(self.root, text="Detalles del Pedido", padding=(20, 10))
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
        ## Orden
        # Crear un widget Text
        self.orden_text_frame = ttk.LabelFrame(self.root, text="Productos")
        self.orden_text = tk.Text(self.orden_text_frame, height=10, width=40)
        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self.check_frame, text="Metodo de Pago", padding=(20, 10))
        # Radiobuttons
        self.metodos_de_pago = ["Efectivo","Transferencia"]
        self.var_metodos_de_pago = tk.IntVar(value=0) 
        self.radio_metodos_de_pago = [ttk.Radiobutton(self.radio_frame, text=metodo, variable=self.var_metodos_de_pago, value=1) for i,metodo in enumerate(self.metodos_de_pago)]
        # BOTONES
        self.widgets_frame = ttk.Frame(self.check_frame)
        self.botones = ["Guardar","Cancelar"]
        self.botones_button = [ttk.Button(self.widgets_frame, text=i) for i in self.botones]
        ## TARIFA
        self.tarifa_frame = ttk.LabelFrame(self.check_frame, text="Numero celular", padding=(20, 10))
        self.tarifa_entry = ttk.Entry(self.num_cliente_frame)
        self.tarifa_entry.insert(0, "Ej. 5510293483")
        self.tarifa_entry.bind("<Button-1>", lambda event: self.borrar_texto(num_cliente_entry))# Asociar la función borrar_texto al evento clic
        
    def draw(self):
        ## TODO LO QUE DIBUJA A LOS WIDGETS -------------------------------------------------------------------------------------------------------------------------------

        self.check_frame.grid(row=1, column=0, padx=(3), pady=(3), sticky="nsew")

        self.direc_cliente_frame.grid(row=0, column=0, sticky="nsew")
        self.direc_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.nombre_cliente_frame.grid(row=1, column=0, sticky="nsew")
        self.nombre_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.num_cliente_frame.grid(row=1, column=1, sticky="nsew")
        self.num_cliente_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

        self.orden_text_frame.grid(row=0, column=0, sticky="nsew")
        self.orden_text.pack(pady=10)

        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")
        self.tarifa_frame.grid(row=3, column=0, padx=(20, 10), pady=10, sticky="nsew")


        for i,radio in enumerate(self.radio_metodos_de_pago):
            radio.state(["alternate"])
            
            radio.grid(row=i, column=0, sticky="nsew")

        for i,btn in enumerate(self.botones_button):
            btn.grid(row=0, column=i, sticky="nsew")
        self.widgets_frame.grid(row=3, column=0, sticky="nsew")

    def get_data(self,func):
        direccion = self.direc_cliente_entry.get()
        nombre = self.nombre_cliente_entry.get()
        numero = self.num_cliente_entry.get()
        orden = self.orden_text.get()
        data = [direccion, nombre, numero, orden]
        func(data)
    def borrar_texto(self,entry):
        # Borra el texto dentro del Entry al recibir un clic
        entry.delete(0, tk.END)


def agregar():
    agregar_ventana = Agregar_pedido(root)
    agregar_ventana.draw()
def devolver(data):
    return data

def cap_pedido():
    pass
root = tk.Tk()
root.title("Agregar nuevo pedido. PEDIDITO")
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



# Tab #1
tab_1 = ttk.Frame(notebook)# 1)
tab_1.columnconfigure(index=0, weight=1)
tab_1.columnconfigure(index=1, weight=1)
tab_1.rowconfigure(index=0, weight=1)
tab_1.rowconfigure(index=1, weight=1)

notebook.add(tab_1, text="Tab 1")# 2)

# Panedwindow
paned = ttk.PanedWindow(tab_1)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)


# Pane #2
pane_2 = ttk.Frame(paned)
paned.add(pane_2, weight=3)

# Create a Frame for input widgets
widgets_frame = ttk.Frame(tab_1, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# Entry
entry = ttk.Entry(widgets_frame)
entry.insert(0, "Entry")
entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")



### Menubutton
##menubutton = ttk.Menubutton(widgets_frame, text="Menubutton", menu=menu, direction="below")
##menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

# OptionMenu
optionmenu = ttk.OptionMenu(widgets_frame, e, *option_menu_list)
optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

# Accentbutton
accentbutton = ttk.Button(widgets_frame, text="Agregar Pedido", style="Accent.TButton", command = agregar)
accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")





# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_2)
treeFrame.pack(expand=True, fill="both", padx=5, pady=5)

# Scrollbar
treeScroll = ttk.Scrollbar(treeFrame)
treeScroll.pack(side="right", fill="y")

columnas = ["Nombre","Numero","Direccion","Orden"]

# Treeview
treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(x for x,val in enumerate(columnas)), height=12)
treeview.pack(expand=True, fill="both")
treeScroll.config(command=treeview.yview)

for i,col in enumerate(columnas):
    if i == 0:
        treeview.column("#0", width=120)
        treeview.heading("#0", text=col, anchor="center")
    else:
        treeview.column(i, width=120)
        treeview.heading(i, text=col, anchor="center")

# Define treeview data
treeview_data = [
    ("", "end", 1, "Parent", ("Item 1", "Value 1")),
    (1, "end", 2, "Child", ("Subitem 1.1", "Value 1.1")),
    (1, "end", 3, "Child", ("Subitem 1.2", "Value 1.2")),
    (1, "end", 4, "Child", ("Subitem 1.3", "Value 1.3")),
    (1, "end", 5, "Child", ("Subitem 1.4", "Value 1.4")),
    ("", "end", 6, "Parent", ("Item 2", "Value 2")),
    (6, "end", 7, "Child", ("Subitem 2.1", "Value 2.1")),
    (6, "end", 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
    (8, "end", 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
    (8, "end", 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
    (8, "end", 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
    (6, "end", 12, "Child", ("Subitem 2.3", "Value 2.3")),
    (6, "end", 13, "Child", ("Subitem 2.4", "Value 2.4")),
    ("", "end", 14, "Parent", ("Item 3", "Value 3")),
    (14, "end", 15, "Child", ("Subitem 3.1", "Value 3.1")),
    (14, "end", 16, "Child", ("Subitem 3.2", "Value 3.2")),
    (14, "end", 17, "Child", ("Subitem 3.3", "Value 3.3")),
    (14, "end", 18, "Child", ("Subitem 3.4", "Value 3.4")),
    ("", "end", 19, "Parent", ("Item 4", "Value 4")),
    (19, "end", 20, "Child", ("Subitem 4.1", "Value 4.1")),
    (19, "end", 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
    (21, "end", 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
    (21, "end", 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
    (21, "end", 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
    (19, "end", 25, "Child", ("Subitem 4.3", "Value 4.3"))
    ]

# Insert treeview data
for item in treeview_data:
    treeview.insert(parent=item[0], index=item[1], iid=item[2], text=item[3], values=item[4])
    if item[0] == "" or item[2] in (8, 12):
        treeview.item(item[2], open=True) # Open parents

# Select and scroll
treeview.selection_set(10)
treeview.see(7)




# Tab #2
tab_2 = ttk.Frame(notebook)
notebook.add(tab_2, text="Tab 2")

# Tab #3
tab_3 = ttk.Frame(notebook)
notebook.add(tab_3, text="Tab 3")

notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.pack()

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()

5

### Widgets Fer
import openpyxl
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class Excel:
    def __init__(self):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Agregar a PEDIDITO_DATABASE")

        # En que Activity estoy =
        self.activity = "main"
        # SE DEBEN ESCRIBIR TODAS LAS ACTIVITIES AQUI?
        # WIDGETS DE __init__(self)
        self.widgets_ventana_principal = [
            [tk.Label(self.ventana,text="Excel Master",font=("calibri",40)),(0,0)],
            [tk.Button(self.ventana,text="leer_archivo",command=self.leer_archivo),(1,0)]
##            [tk.Button(self.ventana,text="leer_archivo",command=self.crear_archivo),(2,0)]
            ]
        self.nombre_archivo_var = tk.StringVar()
        self.nombre_hoja_var = tk.StringVar()
        self.rango_var = tk.StringVar()
        ## WIDGETS DE leer_archivo
        self.widgets_leer_archivo = [
            [tk.Label(self.ventana,text="leer_archivo",font=("calibri",40)),(0,0)], 
            [tk.Button(self.ventana,text="Regresar",command = self.regresar),(1,0)],
            [tk.Label(self.ventana,text="Ingrese el nombre del archivo",font=("calibri",20)),(0,1)],
            [tk.Button(self.ventana,text="Buscar",font=("calibri",12),command=self.buscar),(1,1)], 
            [tk.Label(self.ventana,text="Ingrese el nombre de la hoja en el archivo",font=("calibri",20)),(2,1)],
            [tk.Entry(self.ventana,text="",font=("calibri",16),textvariable=self.nombre_hoja_var),(3,1)],
            [tk.Label(self.ventana,text="Rango",font=("calibri",20)),(4,1)],
            [tk.Entry(self.ventana,text="",font=("calibri",16),textvariable=self.rango_var),(5,1)], 
            [tk.Button(self.ventana,text="Validar nombre de archivo",font=("calibri",12),command=self.validar_libro),(6,1)]        # Encabezados
            ]
        self.encabezados = ["N° de Pedido","Fecha","Hora del pedido","Nombre del cliente","N° de Contacto","Recoleccion","Entrega","Producto","Paga con…","Costo del pedido","Tarifa","Cobro total","Dinero entregado a repartidor para compra","$ entregado al repartidor para cambio","$ total dado al repartidor","$ total recibido por el repartidor"]  
        self.treeview_widget = []
        self.treeview_widget.append([ttk.Frame(self.ventana),(2,0)])
        self.treeview_widget.append([ttk.Scrollbar(self.treeview_widget[len(self.treeview_widget)-1][0]),("right","y")])
        columnas = [x for x in range(1,len(self.encabezados))]
        self.treeview_widget.append([ttk.Treeview(self.treeview_widget[len(self.treeview_widget)-2][0], selectmode="extended", yscrollcommand=self.treeview_widget[len(self.treeview_widget)-1][0].set, columns=columnas, height=12),(True,"both")])
        
        
        print(self.treeview_widget[len(self.treeview_widget)-1][0])

        # Habrá un boton que te diga que base de datos quieres leer
    def update(self):
        for i,widget in enumerate(self.widgets_ventana_principal):
            widget[0].grid(row = widget[1][0],column = widget[1][1])
    def validar_libro(self):
        self.nombre_hoja = self.nombre_hoja_var.get()
        self.rango = self.rango_var.get()
        # Cargar el libro de trabajo (workbook)
        self.libro = openpyxl.load_workbook(self.archivo)

        # Acceder a una hoja específica
        self.hoja = self.libro[self.nombre_hoja]

        # Extraer información desde el rango especificado
        informacion_extraida = self.extraer_informacion_desde_rango(self.hoja, self.rango)
        pedidos_totales = len(informacion_extraida)
        for i,widget in enumerate(self.widgets_leer_archivo):
            if i == 0:
                pass
            if i == 1:
                pass
            if i == 2:
                pass
            else:
                widget[0].grid_forget()
        for i,widget_list in enumerate(self.treeview_widget):
            
            if isinstance(widget_list[1][0], bool):
                print(f" bool widget:{widget_list[1][0]},{widget_list[1][1]}")
                widget_list[0].pack(expand=widget_list[1][0], fill=widget_list[1][1])
            elif isinstance(widget_list[1][0], str):
                print(f" str widget:{widget_list[1][0]},{widget_list[1][1]}")
                widget_list[0].pack(side=widget_list[1][0], fill=widget_list[1][1])
            elif isinstance(widget_list[1][0], (int,float)):
                print(f" Int widget:{widget_list[1][0]},{widget_list[1][1]}")
                widget_list[0].grid(row=widget_list[1][0],column=widget_list[1][1])
            
        self.treeview_widget[len(self.treeview_widget)-2][0].config(command=self.treeview_widget[len(self.treeview_widget)-1][0].yview)
                # Treeview columns
        for i, j in enumerate(self.encabezados):
            if i == 0:
                self.treeview_widget[len(self.treeview_widget)-1][0].column("#0", width=100)
                self.treeview_widget[len(self.treeview_widget)-1][0].heading("#0", text=j, anchor="center")
            else:
                self.treeview_widget[len(self.treeview_widget)-1][0].heading(i, text=j, anchor="center")
                self.treeview_widget[len(self.treeview_widget)-1][0].column(i, anchor="w", width=100)

        for i,fila in enumerate(informacion_extraida):
            self.mostrar_dicc(self.treeview_widget[len(self.treeview_widget)-1][0],fila)
        
    def buscar(self):
        self.archivo = filedialog.askopenfilename(title="Seleccionar Archivo", filetypes=[("Todos los archivos", "*.*")])
        self.widgets_leer_archivo[2][0].grid_forget()
        self.widgets_leer_archivo.append([tk.Label(self.ventana,text=self.archivo,font=("Helvetica",12)),(1,1)])
        self.widgets_leer_archivo[len(self.widgets_leer_archivo)-1][0].grid(row=self.widgets_leer_archivo[len(self.widgets_leer_archivo)-1][1][0],column=self.widgets_leer_archivo[len(self.widgets_leer_archivo)-1][1][1])
    def mostrar_dicc(self,tree, diccionario, parent=""):
        
        if parent == "btn-add":# 
            tree.insert("", '0',text=diccionario[0], values=diccionario[1:])
        else:
            tree.insert("", 'end',text=diccionario[0], values=diccionario[1:])
            
    def leer_excel(self,ruta_archivo, nombre_hoja, rango):
        # Leer el archivo Excel
        df = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja)
        print(df)
        # Seleccionar el rango específico
        df_rango = df.loc[rango[0]:rango[1]]

        # Convertir el DataFrame a un diccionario
        datos_diccionario = df_rango.to_dict(orient='records')

        return datos_diccionario

    def extraer_informacion_desde_rango(self,hoja, rango):
        datos_extraidos = []

        # Obtener las celdas en el rango especificado
        celdas = hoja[rango]
        
        # Iterar sobre las celdas en el rango
        for fila in reversed(celdas):
            fila_datos = [celda.value for celda in fila]
            datos_extraidos.append(fila_datos)

        return datos_extraidos
    
    def regresar(self):
        ## BORRAR WIDGETS DE LA ACTIVITY ANTERIOR
        if self.activity == "leer_archivo":
            for i,widget in enumerate(self.widgets_leer_archivo):
                widget[0].grid_forget()
        ## PONES LOS WIDGETS DE LA ACTIVITY PADRE
        self.update()
    
    def leer_archivo(self):
        self.activity = "leer_archivo"
        ## BORRAR WIDGETS DE LA ACTIVITY ANTERIOR
        for i,widget in enumerate(self.widgets_ventana_principal):
            widget[0].grid_forget()
        
        ## DIBUJAR LOS WIDGETS DE ESTE ACTIVITY
        for i,widget in enumerate(self.widgets_leer_archivo):
            widget[0].grid(row = widget[1][0],column = widget[1][1])
        
##        # Ejemplo de uso
##ruta_archivo_excel = 'PEDIDITO_DB.xlsx'
##nombre_hoja_excel = 'BASE_PEDIDITO'
##rango_a_extraer = 'A2:K1500'  # Por ejemplo, desde A1 hasta C10
##
### Cargar el libro de trabajo (workbook)
##libro = openpyxl.load_workbook(ruta_archivo_excel)
##
### Acceder a una hoja específica
##hoja = libro[nombre_hoja_excel]
##
### Extraer información desde el rango especificado
##informacion_extraida = extraer_informacion_desde_rango(hoja, rango_a_extraer)
##pedidos_totales = len(informacion_extraida)
##print("ingreso de base de datos a PEDIDITO SOFTWARE")
##for i,fila in enumerate(informacion_extraida):
##    mostrar_dicc(treeview,fila)
##
### Cerrar el libro después de usarlo
##libro.close()
if __name__ == "__main__":
    iniciar_app = Excel()
    iniciar_app.update()
### DOCUMENTACIÓN

## Jerarquia del programa

## Frame: ventana
##    boton: excel_boton - command = leer_archivo
##
##
##
##
##
##
##
##    

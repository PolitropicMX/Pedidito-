def procesar_lista_compras(cadena_lista):
    lista_items = cadena_lista.split(', ')
    resultado = {}

    for item in lista_items:
        partes = item.split(' ')
        if len(partes) >= 2:
            cantidad = int(partes[0])
            producto = ' '.join(partes[1:])
            resultado[producto] = cantidad

    return resultado

# Ejemplo de uso
cadena_lista_compras = "20 cocas, 1 sabritas, 1 L Leche, 1 caja de cigarros"
diccionario_compras = procesar_lista_compras(cadena_lista_compras)
print(diccionario_compras)

mi_tienda = [
    {'codigo': 1, 'nombre' : 'Aceite', 'stock' : 12, 'precio': 1.5 }, 
    {'codigo': 2, 'nombre' : 'Azucar', 'stock' : 20, 'precio': 2.3 },
    {'codigo': 3, 'nombre' : 'Leche', 'stock' : 15, 'precio': 0.85 },
    {'codigo': 4, 'nombre' : 'Queso', 'stock' : 25, 'precio': 2.5 },
    {'codigo': 5, 'nombre' : 'Arroz', 'stock' : 32, 'precio': 0.6 },
    {'codigo': 6, 'nombre' : 'Yogurt', 'stock' : 30, 'precio': 2.8 },
    {'codigo': 7, 'nombre' : 'Sal', 'stock' : 18, 'precio': 1.00 },
    {'codigo': 8, 'nombre' : 'Harina', 'stock' : 29, 'precio': 0.5 },
    {'codigo': 9, 'nombre' : 'Avena', 'stock' : 38, 'precio': 1.25 },
    {'codigo': 10, 'nombre' : 'Pan', 'stock' : 40, 'precio': 0.2 },
]

def presentar_productos(productos):
    print(f'| Código |     Nombre     |     Precio     |      Stock     |\n')
    print(40*'-')
    for i in mi_tienda:
        nombre =i['nombre']
        codigo = i['codigo']
        precio =i['precio']
        stock =i['stock']
        print(f'|    {codigo}   |     {nombre}     |    {precio}       |      {stock}   |\n')

def solicitar_nombre_producto():
    nombre = str(input("Por favor ingrese su nombre: "))
    producto = int(input(f"Estimado {nombre} de la lista de productos, elija por favor uno para su despacho: "))
    producto_nombre = mi_tienda[producto-1]['nombre']
    cantidad = int(input(f"¿Cuánt@s {producto_nombre} desea? "))

    return nombre, producto, cantidad

def realizar_calculos(cantidad, precio, nombre, producto):
    subtotal = cantidad * precio
    print(f"{nombre}: ud debe pagar {subtotal} \n")
    billete = int(input("La tienda solo recibe billetes de 10, 20, 50, 100, ¿De cuánto es su billete?: "))
    suelto, valida = dar_sueltos(billete, subtotal)
    if (valida):
        print(f"Su suelto es {suelto}")
        mi_tienda[producto-1]['stock'] -= cantidad
    else:
        print("La cantidad ingresas es menor al total a pagar")

def dar_sueltos(billete, total):
    valida = True
    if (billete>total):
        suelto = billete - total
    else:
        suelto = 0
        if (billete<total):
            valida = False

    return suelto, valida 

def proceso():
    for i in range(0, 1):
        nombre, producto, cantidad = solicitar_nombre_producto()
        if (cantidad <= mi_tienda[producto-1]['stock']):
            realizar_calculos(cantidad, mi_tienda[producto-1]['precio'], nombre, producto)
        else:
            print(f"Lamentamos informarle {nombre}, la cantidad deseada excede nuestro Stock!\n")
            print(f"¿Desea comprar {mi_tienda[producto-1]['stock']} disponibles?\n")
            respuesta = int(input("1. Si \n2. No \n"))
            if (respuesta==1):
                realizar_calculos(mi_tienda[producto-1]['stock'], mi_tienda[producto-1]['precio'], nombre, producto)

        print(180*"-")

presentar_productos(mi_tienda)
proceso()
presentar_productos(mi_tienda)

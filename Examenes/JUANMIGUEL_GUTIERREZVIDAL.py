nombre = ["panales","teteros","chupones","juguetes"]
invetario = [1,2,3,4]
costocompra=[1.0,1.2,0.5,1.5] # costo unitario
precioventa=[2.3,2.4,0.7,4.0] # a lo que vende cada articulo
ventasmes = [22,30,40,10] # el numero que vende de cada articulo
comprasmes =[24,32,44,12] # el numero de cosas que compra

def promedioventas(ventasmes):
    suma = 0
    for x in ventasmes:
        suma = suma + x
    promedio = float(suma)/float(len(ventasmes))
    print "el promedio de ventas es",promedio
    return promedio

promedioventas(ventasmes)
# -------------------------------------------

def ingresototal(ventasmes,precioventa):
    ingresoxunidad= []
    ingresototal= 0
    for x in range(len(ventasmes)):
        ingresounidad=  ventasmes[x]*precioventa[x]
        ingresoxunidad.append(float(ingresounidad))
    print "la lista de ingreso total por unidad es ",ingresoxunidad
    for x in ingresoxunidad:
        ingresototal= ingresototal + x
    print "El ingreso total del ultimo mes es ",ingresototal
    return ingresototal

# ---------------------------------------------------------
    
def productosfull(nombre,costocompra,precioventa,ventasmes):
    listafull=[]
    for x in range(len(ventasmes)):
        if precioventa[x]>=2*costocompra[x] and ventasmes[x]>20:
            listafull.append(nombre[x])
    print "Los unicos articulos que cumplieron las condiciones son"
    print listafull
    return listafull

productosfull(nombre,costocompra,precioventa,ventasmes)

# --------------------------------------------------------

def integracion():
    print "Bienvenido, usted tendra 3 opciones"
    print "Opcion1 : Verificar el promedio de ventas"
    print "Opcion 2 : Verificar el ingreso total del ultimo mes"
    print "Opcion 3 : Obtener lista de los articulos que vendio tales que el precio de venta sea "
    print "al menos dos veces mayor al costo de compra y las ventas en el ultimo mes hayan sido superiores"
    print "a 20 unidades"
    opcion = int(raw_input("Digite la opcion(1,2,3) que desea que aparezca o (0) para terminar"))
    while opcion!=0:
        if opcion == 1:
            promedioventas(ventasmes)
        elif opcion == 2:
            ingresototal(ventasmes,precioventa)
        elif opcion ==3:
            productosfull(nombre,costocompra,precioventa,ventasmes)
        print " - - - - - - - - - - - - - - - - - - - "
        print " - - - - - - - - - - - - - - - - - - - "
        opcion = int(raw_input("Digite la opcion(1,2,3) que desea que aparezca o (0) para terminar"))
    print "Chao!,gracias por haber utilizado nuestro servicio"
    return opcion

integracion()

# ----------------------------------------------
    

            
                   

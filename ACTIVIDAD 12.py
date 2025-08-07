def quick_sort(lista):
    if len(lista) <=1:
        return lista
    else:
        pivote = lista[0]
        mayores= [x for x in lista[1:]if x[1]["paquetes"]>pivote[1]["paquetes"]]
        iguales = [x for x in lista[1:]if x[1]["paquetes"]==pivote[1]["paquetes"]]
        menores = [x for x in lista [1:]if x[1]["paquetes"]<pivote[1]["paquetes"]]
        return quick_sort(mayores)+ [pivote] + quick_sort(iguales + menores)

repartidores={}
n = input("ingrese el numero de repartidores")

for in range(n):
    while True:
        nombre=input("nombre del repartidor")
        if nombre in repartidores:
            print("nombre repetido")
        elif nombre =="":
            print("nombre no puede estar vacio")
        else:
            break
    while True:
        try:
            paquetes = int(input("cantidad de paquetes entregados"))
            if paquetes <0:
                print("numero incorrecto")
            else:
                break
        except:
            print("ingrese un numero valido")

    while True:
        zona =input("Zona asignada")
        if zona =="":
            print(" la zona no puede quedar vacia")
        else:
            break
    repartidores[nombre] = {"paquetes": paquetes, "zona": zona}

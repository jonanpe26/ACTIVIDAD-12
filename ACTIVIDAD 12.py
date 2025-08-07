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
n = int(input("ingrese el numero de repartidores"))

for _ in range(n):
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
print("repartidores")
ordenados = quick_sort(list(repartidores.items()))
for nombre, datos in ordenados:
    print(f"{nombre}-{datos["paquetes"]}paquetes -Zona: {datos["zona"]}")

buscar=input("buscar repartidor")
encontrado=False
for nombre in repartidores:
    if nombre == buscar:
        print(f"{nombre} entrego {repartidores[nombre]["paquetes"]} paquetes en la zona {repartidores[nombre]["zona"]}")
        encontrado=True
        break
if not encontrado:
    print("repartidor no encontrando")

total = sum(informacion["paquetes"]for informacion in repartidores.values())
promedio = total/len(repartidores)

maximo=max(informacion["paquetes"]for informacion in repartidores.values())
minimo=min(informacion["paquetes"]for informacion in repartidores.values())

print(f"total de paquetes entregados{total}")
print(f"promedio de entregas{promedio}")
print("mayor numero de entregas")
for nombre, informacion in repartidores.items():
    if informacion["paquetes"]==maximo:
        print(f"{nombre}({informacion["paquetes"]})")

print("menor numero de entregas")
for nombre, informacion in repartidores.items():
    if informacion["paquetes"]==minimo:
        print(f"{nombre}({informacion["paquetes"]})")


import WriteValues as w

print(15*'-')
print("Bienvenido a News Exporter")
print(15*'-')
print("\nEs programa lleva más noticias a el portal de radar.")
print(15*'-')
while True:
    print("¿Desde qué portal deseas extraer noticias?")
    print("1 = El Economista")
    response = int(input("Seleccion: "))
    print(15*"-")
    if response == 1:
        w.sendByPortal()
    else:
        print("Opción no disponible")
    
    print("Deseas repetir alguna exportación?")
    print("Si = Cualquier tecla")
    print("No = E")
    value = input("::")
    if value == "E":
        break
import WriteValues as w

print(15*'-')
print("Bienvenido a News Exporter")
print(15*'-')
print("\nEs programa lleva más noticias a el portal de radar.")
print(15*'-')
print("¿Desde qué portal deseas extraer noticias?")
print("1 = El Economista")
response = int(input("Selección"))
print(15*"-")
if response == 1:
    w.sendByPortal()
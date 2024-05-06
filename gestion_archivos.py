import os
def crear_archivo(nom_archivo):
   archivo = open (f"{nom_archivo}.txt","wt")
   archivo.close()
   return menu()
   
def elim_archivo(nom_archivo):
    os.remove(f"{nom_archivo}.txt")
    return menu()

def agr_contenido(nom_archivo,cont_archivo):
    archivo = open(f"{nom_archivo}.txt","at")
    contenido=f"\n{cont_archivo}"
    archivo.write(contenido)
    archivo.close()
    return menu()

def most_contenido(nom_archivo):
    texto = open(f"{nom_archivo}.txt",encoding='utf8')
    datos_texto = texto.read()
    print(datos_texto)
    return menu()

def salir():
    return
def error():
    print("opcion incorrecta")
    return menu()

def menu():
    print(" ")
    print("1.Crear archivo")
    print("2.Eliminar archivo")
    print("3.Agregar contenido")
    print("4.Mostrar contenido de archivo")
    print("5.Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nom_archivo = input("Ingrese el nombre del archivo: ")
        crear_archivo(nom_archivo)
    elif opcion == "2":
        nom_archivo = input("Ingrese el nombre del archivo a eliminar: ")
        elim_archivo(nom_archivo)
    elif opcion == "3":
        nom_archivo = input("Ingrese el nombre del archivo al que desea agregar contenido: ")
        cont_archivo = input("Ingrese el contenido a agregar: ")
        agr_contenido(nom_archivo, cont_archivo)
    elif opcion == "4":
        nom_archivo = input("Ingrese el nombre del archivo cuyo contenido desea mostrar: ")
        most_contenido(nom_archivo)
    elif opcion == "5":
        salir()
    elif opcion not in ['1', '2', '3', '4', '5']:
        error()
        
        
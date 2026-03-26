import json
with open('datos.json', 'r') as f:
    Datos = json.load(f)

temp = {}
for k, j in Datos.items():
    temp[int(k)] = j
Datos = temp

def generar_id(Datos):
    if not Datos:
        return 1
    return max(Datos.keys()) +1

def buscar_id(Datos, entrada):
    try:
        id_num = int(entrada)
        if id_num in Datos:
            return id_num
        else:
            return None
    except ValueError:
        for idx, datos in Datos.items():
            if datos ["name"] == entrada or datos ["last_name"] == entrada:
                return idx
        return None
    
def ajustar_telefono(numero):
    limpio = ""
    for idx in numero:
        if idx.isdigit():
            limpio += idx
    if limpio.startswith("58"):
        limpio = limpio[2:]
    if limpio.startswith("0"):
        limpio = limpio[1:]
    if len(limpio) < 10:
        return "+58 ---"   
    if len(limpio) > 10:
        limpio = limpio[-10:]
    codigo = limpio[:3]
    numero_final = limpio[3:]

    telefono_final = f"+58 {codigo}-{numero_final}"
    return telefono_final

while True:
    try:
        print("\n===Menu de Usuario===")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Editar Usuario")
        print("4. Eliminar Usuario")
        print("5. Base de Datos")
        print("6. Salir")
        opc = int(input("\nSeleccione una opcion: "))

        if opc == 1:
            new_id = generar_id(Datos)
            name = input("\nIngrese el nombre del nuevo Usuario: ").capitalize()
            last_name = input("Ingrese el apellido del nuevo Usuario: ").capitalize()
            correo = input("Ingrese el correo: ").lower()
            estado = input("Ingrese la zona del usuario: ").capitalize()
            numero = input("Ingrese su numero telefonico: ")
            resultado = ajustar_telefono(numero)
            telefono = resultado
            while True:
                try:
                    age = int(input("Ingrese la edad del nuevo Usuario: "))
                    Datos[new_id] = {"name": name, "last_name": last_name, "age": age, "telefono": telefono, "correo": correo, "estado": estado}
                    print(f"\nNuevo Usuario agregado con exito.\n {Datos[new_id]}")
                    with open('datos.json', 'w') as s:
                        json.dump(Datos, s, indent=4)
                    break
                except ValueError:
                    print("\nError: Debe de ingresar un valor entero.")

        elif opc == 2:
            search_id = (input("\nIngrese la ID/Name a buscar: ")).capitalize()
            resultado = buscar_id(Datos, search_id)
            if resultado is None:
                print("Usuario no encontrado")
            else:
                print("Usuario encontrado\n", f"ID: {resultado} → {Datos[resultado]}")

        elif opc == 3:
            search_id = (input("\nIngrese la ID/Name a editar: ")).capitalize()
            resultado = buscar_id(Datos, search_id)
            if resultado is None:
                print("Usuario no encontrado")
            else:
                print("Usuario encontrado\n", Datos[resultado],)
                temp = input("¿Desea modificarlo? (s/n): ").lower()
                if temp == "s":
                    Datos[resultado]["name"] = input("Ingrese el nuevo nombre: ").capitalize()
                    Datos[resultado]["last_name"] = input("Ingrese el nuevo apellido: ").capitalize()
                    Datos[resultado]["correo"] = input("Ingrese el nuevo correo: ").lower()
                    Datos[resultado]["estado"] = input("Ingrese el estado del usuario: ").capitalize()
                    numero = Datos[resultado]["telefono"] = (input("Ingrese el nuevo numero de telefono: "))
                    num = ajustar_telefono(numero)
                    Datos[resultado]["telefono"] = num
                    while True:
                        try:
                            Datos[resultado]["age"] = int(input("Ingrese la nueva edad: "))
                            print("\nUsuario actualizado")
                            with open('datos.json', 'w') as s:
                                json.dump(Datos, s, indent=4)
                            break
                        except ValueError:
                            print("\nError: Debe de ingresar un valor entero.")
                else:
                    print("\nOperacion cancelada")
                      
        elif opc == 4:
            search_id = (input("\nIngrese la ID/Name a editar: ")).capitalize()
            resultado = buscar_id(Datos, search_id)
            if resultado is None:
                print("Usuario no encontrado")
            else:
                print("Usuario encontrado\n", Datos[resultado],)
                temp = input("¿Desea eliminarlo? (s/n): ").lower()
                if temp == "s":
                    del Datos[resultado]
                    print(f"Usuario: {resultado} eliminado")
                    with open('datos.json', 'w') as s:
                        json.dump(Datos, s)
                else:
                    print("\nOperacion cancelada")

        elif opc == 5:
            print("\n===BASE DE DATOS===")
            for id_usuarios, datos in Datos.items():
                print(f"ID: {id_usuarios} → {datos}")

        elif opc == 6:
            print("\nHasta luego.")
            break

        else:
            print("\nError: debe seleccionar una de las opciones mencionadas.")
    except ValueError:
        print("\nError: Debe de ingresar un valor entero.")

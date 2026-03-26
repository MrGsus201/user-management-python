Usuarios = {
    1: {"name": "Carlos", "last_name": "Gonzalez", "age": 28,
        "telefono": "+58 412-1234567", "correo": "carlos.gonzalez@example.com",
        "estado": "Aragua"},

    2: {"name": "Maria", "last_name": "Fernandez", "age": 32,
        "telefono": "+58 414-9876543", "correo": "maria.fernandez@example.com",
        "estado": "Carabobo"},

    3: {"name": "Luis", "last_name": "Ramirez", "age": 25,
        "telefono": "+58 424-5566778", "correo": "luis.ramirez@example.com",
        "estado": "Miranda"},

    4: {"name": "Ana", "last_name": "Torres", "age": 29,
        "telefono": "+58 416-3344556", "correo": "ana.torres@example.com",
        "estado": "Lara"},

    5: {"name": "Jose", "last_name": "Martinez", "age": 35,
        "telefono": "+58 426-7788991", "correo": "jose.martinez@example.com",
        "estado": "Zulia"},

    6: {"name": "Valeria", "last_name": "Soto", "age": 22,
        "telefono": "+58 412-6655443", "correo": "valeria.soto@example.com",
        "estado": "Táchira"},

    7: {"name": "Daniel", "last_name": "Rivas", "age": 31,
        "telefono": "+58 414-2233445", "correo": "daniel.rivas@example.com",
        "estado": "Mérida"},

    8: {"name": "Gabriela", "last_name": "Moreno", "age": 27,
        "telefono": "+58 424-9988776", "correo": "gabriela.moreno@example.com",
        "estado": "Monagas"},

    9: {"name": "Jorge", "last_name": "Paredes", "age": 30,
        "telefono": "+58 416-1122334", "correo": "jorge.paredes@example.com",
        "estado": "Bolívar"},

    10: {"name": "Patricia", "last_name": "Vargas", "age": 26,
        "telefono": "+58 426-3344667", "correo": "patricia.vargas@example.com",
        "estado": "Falcón"},

    11: {"name": "Ricardo", "last_name": "Navarro", "age": 33,
        "telefono": "+58 412-7788445", "correo": "ricardo.navarro@example.com",
        "estado": "Sucre"},

    12: {"name": "Elena", "last_name": "Castro", "age": 24,
        "telefono": "+58 414-5566442", "correo": "elena.castro@example.com",
        "estado": "Guárico"},

    13: {"name": "Miguel", "last_name": "Peña", "age": 29,
        "telefono": "+58 424-6677889", "correo": "miguel.pena@example.com",
        "estado": "Anzoátegui"},

    14: {"name": "Sofia", "last_name": "Mendoza", "age": 21,
        "telefono": "+58 416-8899001", "correo": "sofia.mendoza@example.com",
        "estado": "Yaracuy"},

    15: {"name": "Andres", "last_name": "Salazar", "age": 34,
        "telefono": "+58 426-1122554", "correo": "andres.salazar@example.com",
        "estado": "Portuguesa"},

    16: {"name": "Paola", "last_name": "Rangel", "age": 28,
        "telefono": "+58 412-3344778", "correo": "paola.rangel@example.com",
        "estado": "Nueva Esparta"},

    17: {"name": "Hector", "last_name": "Acosta", "age": 36,
        "telefono": "+58 414-7788990", "correo": "hector.acosta@example.com",
        "estado": "Barinas"},

    18: {"name": "Natalia", "last_name": "Blanco", "age": 23,
        "telefono": "+58 424-2233556", "correo": "natalia.blanco@example.com",
        "estado": "Cojedes"},

    19: {"name": "Samuel", "last_name": "Lopez", "age": 27,
        "telefono": "+58 416-4455667", "correo": "samuel.lopez@example.com",
        "estado": "Trujillo"},

    20: {"name": "Isabel", "last_name": "Rojas", "age": 30,
        "telefono": "+58 426-5566778", "correo": "isabel.rojas@example.com",
        "estado": "Distrito Capital"}
}

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
            new_id = max(Usuarios.keys()) + 1
            name = input("\nIngrese el nombre del nuevo Usuario: ").capitalize()
            last_name = input("Ingrese el apellido del nuevo Usuario: ").capitalize()
            correo = input("Ingrese el correo: ").title()
            estado = input("Ingrese la zona del usuario: ").capitalize()
            telefono = input("Ingrese su numero telefonico: ")
            while True:
                try:
                    age = int(input("Ingrese la edad del nuevo Usuario: "))
                    Usuarios[new_id] = {"name": name, "last_name": last_name, "age": age, "telefono": telefono, "correo": correo, "estado": estado}
                    print(f"\nNuevo Usuario agregado con exito.\n {Usuarios[new_id]}")
                    break
                except ValueError:
                    print("\nError: Debe de ingresar un valor entero.")

        elif opc == 2:
            search_id = (input("\nIngrese la ID/Name a buscar: ")).capitalize()
            try:
                id_num = int(search_id)
                if id_num in Usuarios:
                    print(f"\nUsuario Encontrado: (ID {id_num}): {Usuarios[id_num]}")
                else:
                    print("\nUsuario no encontrado")
            except ValueError:
                encontrado = False
                for idx, datos in Usuarios.items():
                    if datos["name"] == search_id or datos["last_name"] == search_id:
                        print(f"\nUsuario encontrado (ID {idx}): {datos}")
                        encontrado = True
                if not encontrado:
                    print("\nUsuario no encontrado")

        elif opc == 3:
            edit_id = (input("\nIngrese la ID/Name a editar: ")).capitalize()
            try:
                id_num = int(edit_id)
                if id_num in Usuarios:
                    print(f"Datos Actuales: {Usuarios[id_num]}")
                    resp = input("Usuario encontrado, seguro que desea editarlo (s/n): ").lower()
                    if resp == "s":
                        Usuarios[id_num]["name"] = input("Ingrese el nuevo nombre: ").capitalize()
                        Usuarios[id_num]["last_name"] = input("Ingrese el nuevo apellido: ").capitalize()
                        Usuarios[id_num]["correo"] = input("Ingrese el nuevo correo: ").title()
                        Usuarios[id_num]["estado"] = input("Ingrese el estado del usuario: ").title()
                        while True:
                            try:
                                Usuarios[id_num]["age"] = int(input("Ingrese la nueva edad: "))
                                Usuarios[id_num]["telefono"] = int(input("Ingrese el nuevo numero de telefono: "))
                                print("\nUsuario Actualizado")
                                break
                            except ValueError:
                                print("\nError: Debe de ingresar un valor entero.")
                    else:
                        print("Operacion cancelada\n")
                else:
                    print("\nUsuario no encontrado")
            except ValueError:
                encontrado = False
                for idx, datos in Usuarios.items():
                    if datos["name"] == edit_id or datos["last_name"] == edit_id:
                        resp = input("Usuario encontrado, seguro que desea editarlo (s/n): ").lower()
                        if resp == "s":
                            print(f"Datos Actuales: {Usuarios[idx]}")
                            Usuarios[idx]["name"] = input("Ingrese el nuevo nombre: ").capitalize()
                            Usuarios[idx]["last_name"] = input("Ingrese el nuevo apellido: ").capitalize()
                            Usuarios[idx]["correo"] = input("Ingrese el nuevo correo: ").title()
                            Usuarios[idx]["estado"] = input("Ingrese el estado del usuario: ").title()
                            while True:
                                try:
                                    Usuarios[idx]["age"] = int(input("Ingrese la nueva edad: "))
                                    Usuarios[idx]["telefono"] = int(input("Ingrese el nuevo numero de telefono: "))
                                    print("\nUsuario Actualizado")
                                    break
                                except ValueError:
                                    print("\nError: Debe de ingresar un valor entero.")
                        else:
                            print("\nOperacion cancelada\n")
                            
        elif opc == 4:
            delete_id = input("\nIngrese la ID/Name a eliminar: ").capitalize()
            try:
                id_num = int(delete_id)
                if id_num in Usuarios:
                    print(f"Datos Actuales: {Usuarios[id_num]}")
                    resp = input("Seguro que desea eliminarlo (s/n): ").lower()
                    if resp == "s":
                        del Usuarios[id_num]
                        print("Usuario eliminado\n")
                    elif resp == "n":
                        print("Operacion cancelada\n")
                else:
                    print("\nUsuario no encontrado")
            except ValueError:
                encontrado = False
                for idx, datos in Usuarios.items():
                    if datos["name"] == delete_id or datos["last_name"] == delete_id:
                        value = idx
                        resp = input("Usuario encontrado, seguro que desea eliminarlo (s/n): ").lower()
                if resp == "s":
                    del Usuarios[value]
                    print("Usuario eliminado\n")
                else:
                    print("Operacion cancelada\n")

        elif opc == 5:
            print("\n===BASE DE DATOS===")
            for id_usuarios, datos in Usuarios.items():
                print(f"ID: {id_usuarios} → {datos}")

        elif opc == 6:
            print("\nHasta luego.")
            break

    except ValueError:
        print("\nError: Debe de ingresar un valor entero.")
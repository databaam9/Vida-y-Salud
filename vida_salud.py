datos = {}
montos=[1000,1150,1200,1250,1300,1350,1400,1450,1500]
i_monto=0

while True:
    print("\nMENÚ")
    print("[1] Grabar")
    print("[2] Buscar")
    print("[3] Imprimir certificados")
    print("[4] Salir")
    
    try:
        opcion = int(input("Seleccione una de las opciones anteriores: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        continue

    if opcion == 1:
        rut = input("Ingrese el RUT (con guion): ")
        if "-" not in rut:
            print("El RUT debe contener un guion ('-').")
            continue

        nombre = input("Ingrese su nombre: ")
        apellido_P = input("Ingrese su apellido paterno: ")

        while True:
            try:
                edad = int(input("Ingrese su edad: "))
                if edad >= 18:
                    break
                else:
                    print("Debe ser mayor de edad.")
            except ValueError:
                print("Edad inválida, ingrese un número.")

        while True:
            estado_civil = input("Ingrese su estado civil (C=Casado, S=Soltero, V=Viudo): ")
            if estado_civil == "C" or "c":
                estado_civil = "casado"
                break
            elif estado_civil == "S" or "s":
                estado_civil = "soltero"
                break
            elif estado_civil == "V" or "v":
                estado_civil = "viudo"
                break
            else:
                print("Estado civil no válido.")

        while True:
            genero = input("Ingrese su género (M=Masculino, F=Femenino): ")
            if genero == "M" or "m":
                genero = "masculino"
                break
            elif genero == "F" or "f":
                genero = "femenino"
                break
            else:
                print("Género no válido.")

        
        fechaactual = input("Ingrese la fecha actual [dd/mm/aaaa]: ")
            

        datos[rut] = {
            "nombre": nombre,
            "apellido_P": apellido_P,
            "edad": edad,
            "estado_civil": estado_civil,
            "genero": genero,
            "fecha_registro": fechaactual
        }

        print("Datos grabados correctamente.\n")

    elif opcion == 2:
        rut = input("Ingrese el RUT a buscar: ")
        if rut in datos:
            for clave, valor in datos[rut].items():
                print(f"{clave}: {valor}")
        else:
            print("RUT no encontrado.")

    elif opcion == 3:
        rut = input("Ingrese el RUT para imprimir certificado: ")
        
        monto=montos[i_monto]
        i_monto=i_monto+1
        if i_monto>=10:
            i_monto=0
        if rut in datos:
            print("\n--- CERTIFICADO ---")
            print(f"Nombre: {datos[rut]['nombre']} {datos[rut]['apellido_P']}")
            print(f"Edad: {datos[rut]['edad']}")
            print(f"Estado Civil: {datos[rut]['estado_civil']}")
            print(f"Género: {datos[rut]['genero']}")
            print(f"Fecha de Registro: {datos[rut]['fecha_registro']}")
            print(f"el costo del certificado es:${monto}")
            print("--------------------\n")
        else:
            print("RUT no encontrado.")
        

    elif opcion == 4:
        print("Saliendo del programa.(britany carreño,enzo palominos,carlos colonia(version 1.2))")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

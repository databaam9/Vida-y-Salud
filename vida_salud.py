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
        print("Debe ingresar un número válido.(version 1.0)")
        continue

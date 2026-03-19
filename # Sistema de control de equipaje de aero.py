# Sistema de control de equipaje de aeropuerto

while True:

    print("\n===== REGISTRO DE PASAJERO =====")

    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre del pasajero: ").strip()
        if nombre != "":
            break
        else:
            print("Error: El nombre no puede estar vacío.")

    # Validar cantidad de equipajes
    while True:
        try:
            cantidad_equipaje = int(input("¿Cuántos equipajes lleva el pasajero?: "))
            if cantidad_equipaje > 0:
                break
            else:
                print("Error: Debe ingresar un número mayor que 0.")
        except ValueError:
            print("Error: Debe ingresar un número entero.")

    pesos = []
    estados = []
    costos = []

    costo_total = 0

    for i in range(cantidad_equipaje):

        print(f"\nEquipaje {i+1}")

        # Validar peso
        while True:
            try:
                peso = float(input("Ingrese el peso del equipaje en kg: "))
                if peso >= 0:
                    break
                else:
                    print("Error: El peso no puede ser negativo.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        pesos.append(peso)

        # Evaluación del peso
        if peso <= 23:
            estado = "Permitido"
            costo = 0

        elif peso <= 32:
            extra = peso - 23
            costo = extra * 10000
            estado = "Con sobrepeso"

        else:
            estado = "Rechazado"
            costo = 0

        estados.append(estado)
        costos.append(costo)

        costo_total += costo

    # Mostrar resultados del pasajero
    print("\n----- RESUMEN DEL PASAJERO -----")
    print("Nombre del pasajero:", nombre)

    print("\nEquipaje | Peso (kg) | Estado | Costo Extra")

    for i in range(cantidad_equipaje):
        print(f"{i+1} | {pesos[i]} kg | {estados[i]} | ${costos[i]}")

    print("\nTotal a pagar por sobrepeso: $", costo_total)

    # Preguntar si desea registrar otro pasajero
    while True:
        continuar = input("\n¿Desea registrar otro pasajero? (s/n): ").lower()
        if continuar == "s":
            break
        elif continuar == "n":
            print("\nSistema finalizado.")
            exit()
        else:
            print("Error: escriba 's' para sí o 'n' para no.")
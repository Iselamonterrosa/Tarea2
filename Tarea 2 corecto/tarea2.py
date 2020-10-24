saldoinicial = 0.00
while True:
    options = input(
        "ingrese una opcion 0- Salir 1- Ingresar el dinero 2- Retirar el dinero 3-Reporte de Ingresos 4-Reporte "
    )

    if options == "0":
        break
    elif options == "1":
        ingreso = float(input(" Cuanto dinero deseas ingresar a tu cuenta"))
        saldoinicial = saldoinicial + ingreso
        print(f"Su total es de: {saldoinicial} ")
    elif options == "2":
        egreso = float(input(" Cuanto dinero deseas reitirar de tu cuenta"))
        saldoinicial = saldoinicial - egreso
        if egreso > saldoinicial:
            print("No tienes suficiente dinero")
        else:
            saldoinicial < egreso
            print(f"El dinero en su cuenta es: {saldoinicial} ")

    elif options == "3":
        print(f"El dinero en su cuenta es: {saldoinicial} ")
    elif options == "4":
        print(f"El dinero en su cuenta es: {saldoinicial} ")
    elif options == "5":
        transacciones = float(input(" Obtener transacciones"))
        print(f"El dinero en su cuenta es: {saldoingreso} ")
        print(f"El dinero en su cuenta es: {saldodeegreso} ")
    elif options == "6":
        saldoTotal = float(input(" El monto total en su cuenta es"))
        saldoTotal = saldoingreso - saldodeegreso
        print(f"El dinero en su cuenta es: {saldoTotal} ")
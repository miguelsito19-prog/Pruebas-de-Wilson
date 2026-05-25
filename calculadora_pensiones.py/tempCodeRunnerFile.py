# INGRESO DEL SUELDO EN BRUTO
while True:
    try:
        sueldo_bruto = float(input("Ingrese el sueldo en bruto: "))
        if sueldo_bruto > 564:
            break
        else:
            print("El sueldo esta por debajo del minimo en planilla")
    except ValueError:
        print("Ingrese un valor valido")
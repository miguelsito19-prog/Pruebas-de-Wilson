"""CALCULADORA DE PENSIONES"""
# SUELDO EM BRUTO
while True:
    try:
        sueldo_bruto = float(input("Ingrese el sueldo en bruto: "))
        if sueldo_bruto > 0:
            break
        else:
            print("Ingrese un valor valido")
    except ValueError:
        print("Ingrese un valor numerico")

# ELIGIENDO SISTEMA DE PENSIONES
print("Ingrese 0 si esta en el sistema ONP") 
print("Ingrese 1 si esta en el sistema AFP Habitat")
print("Ingrese 2 si esta en el sistema AFP Integra")
print("Ingrese 3 si esta en el sistema Prima AFP")
print("Ingrese 4 si esta en el sistema Profuturo AFP")
while True:
    try:
        sistema = int(input("Ingrese el valor del sistema en que se encuentre: "))
        if 5 > sistema > -1:
            break
        else:
            print("Ingrese in valor valido")
    except ValueError:
        print("Ingrese un valor numerico solicitado")
        
# VALORES UNIVERSALES
prima_seguro = 0.0137
aporte_obligatorio = 0.1
total_universales = prima_seguro + aporte_obligatorio

"""SISTEMAS DE PENSIONES"""

# SISTEMA DE PENSIONES ONP
if sistema == 0:
    aporte_onp = 0.13
    descuento_onp = sueldo_bruto * aporte_onp
    sueldo_neto = sueldo_bruto - descuento_onp
    print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}")

# SISTEMA DE PENSIONES AFP HABITAT
elif sistema == 1:
    print("Usted ingreso al sistema AFP Habitat")
    while True:
        try:
            cuenta = int(input("Ingrese 0 si tiene cuenta flujo, sino 1 si tiene cuenta mixta: "))
            if 2 > cuenta > -1:
                break
            else:
                print("Ingrese un valor solicitado")
        except ValueError:
            print("Ingrese un valor valido")
    if cuenta == 0:
        comision_habitat = 0.0147
        total_habitat = total_universales + comision_habitat
        descuento_habitat = sueldo_bruto * total_habitat
        sueldo_neto = sueldo_bruto - descuento_habitat
        print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}")
    elif cuenta == 1:
       descuento_habitat = sueldo_bruto * total_universales
       sueldo_neto = sueldo_bruto - descuento_habitat
       print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}") 
       
# SISTEMA DE PENSIONES AFP INTEGRA
elif sistema == 2:
    print("Usted ingreso al sistema AFP Integra")
    while True:
        try:
            cuenta = int(input("Ingrese 0 si tiene cuenta flujo, sino 1 si tiene cuenta mixta: "))
            if 2 > cuenta > -1:
                break
            else:
                print("ingrese solo los valores solicitados")
        except ValueError:
            print("Ingrese solo valores numericos")
    if cuenta == 0:
        comision_integra = 0.0155
        total_integra = total_universales + comision_integra
        descuento_integra = sueldo_bruto * total_integra
        sueldo_neto = sueldo_bruto - descuento_integra
        print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}")
    elif cuenta == 1:
        descuento_integra = sueldo_bruto * total_universales
        sueldo_neto = sueldo_bruto - descuento_integra
        print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}")

# SISTEMA DE PENSIONES PRIMA AFP
elif sistema == 3:
    while True:
        try:
            cuenta = int(input("Ingrese 0 si tien cuenta flujo, sino 1 si tien cuenta mixta: "))
            if 2 > cuenta > -1:
                break
            else:
                print("Ingrese un valor solicitado")
        except ValueError:
            print("Ingrese un valor numerico")
    if cuenta == 0:
        comision_prima = 0.016
        total_prima = total_universales + comision_prima
        descuento_prima = sueldo_bruto * total_prima
        sueldo_neto = sueldo_bruto - descuento_prima
        print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}")
    elif cuenta == 1:
        descuento_prima = sueldo_bruto * total_universales
        sueldo_neto = sueldo_bruto - descuento_prima
        print(f"Su sueldo es de S/{sueldo_neto:,.2f}")

# SISTEMA DE PENSIONES PROFUTURO
elif sistema == 4:
    while True:
        try:
            cuenta = int(input("Ingrese 0 si tiene cuenta flujo, sino 1 si tiene cuenta mixta: "))
            if 2 > cuenta > -1:
                break
            else:
                print("Ingrese solo los valores solicitados")
        except ValueError:
            print("Ingrese solo valores numericos")
    if cuenta == 0:
        comision_profuturo = 0.0169
        total_profuturo = comision_profuturo + total_universales 
        descuento_profuturo = sueldo_bruto * total_profuturo
        sueldo_neto = sueldo_bruto - descuento_profuturo
        print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}")
    if cuenta == 1:
        descuento_profuturo = sueldo_bruto * total_universales
        sueldo_neto = sueldo_bruto - descuento_profuturo
        print(f"Su sueldo neto es de S/{sueldo_neto:,.2f}")

"""CALCULADORA DE PENSIONES"""

# SUELDO BRUTO DEL EMPLEADO
while True:
    try:
        sueldo_bruto = float(input("Ingrese el sueldo bruto: "))
        if sueldo_bruto > 0:
            break
        else:
            print("Ingrese un valor valido")
    except ValueError: 
        print("Ingrese un valor numerico")

# DICCIONARIO DE COMISIONES
comisiones_afps = { 
                  "habitat": 0.0147,
                  "integra": 0.0155,
                  "prima": 0.016,
                  "profuturo": 0.0169
                  }
# VALORES UNIVERSALES
aporte_obligatorio = 0.1
prima_seguro = 0.0137
universal = aporte_obligatorio + prima_seguro

# DEFINIENDO CUENTAS EN AFPS
def cuentas(comision):
    while True:
            try:
                cuenta = int(input("Ingrese 0 si esta en cuenta flujo o 1 si esta mixta: "))
                if 2 > cuenta > -1:
                    break
                else:
                    print("Ingrese un valor valido")
            except ValueError:
                print("Ingrese un valor numerico")
    if cuenta == 0:
        descuento_afp = sueldo_bruto * (universal + comision)
        sueldo_neto = sueldo_bruto - descuento_afp
    elif cuenta == 1:
        descuento_afp = sueldo_bruto * universal
        sueldo_neto = sueldo_bruto - descuento_afp
    print(f"El sueldo neto es de S/{sueldo_neto:,.2f}")
 
# ELIGIENOO SISTEMA 
print("Ingrese 0 si esta en el sistema ONP")
print("Ingrese 1 si esta en el sistema AFP Habitat")
print("Ingrese 2 si esta en el sistema AFP Integra")
print("Ingrese 3 si esta en el sistema Prima AFP")
print("Ingrese 4 si esta en el sistema AFP Profuturo")

while True:
    try:
        sistema = int(input("Ingrese el numero de sistema en que se encuentre: "))
        if 5 > sistema > -1:
            break
        else:
            print("Ingrese un valor valido")
    except ValueError:
        print("Ingrese un valor numerico")

# SISTEMAS DE PENSIONES CALCULO
if sistema == 0:
    print("Se encuentra en sistema ONP")
    aporte_onp = 0.13
    descuento_onp = sueldo_bruto * aporte_onp
    sueldo_neto = sueldo_bruto - descuento_onp   
elif sistema == 1:
    print("Se encuentra en sistema AFP Habitat")
    cuentas(comisiones_afps["habitat"])
elif sistema == 2:
    print("Se encuentra en sistema AFP Integra")
    cuentas(comisiones_afps["integra"])
elif sistema == 3:
    print("Se encuentra en sistema Prima AFP")
    cuentas(comisiones_afps["prima"])
elif sistema == 4:
    print("Se encuentra en sistema AFP Profuturo")
    cuentas(comisiones_afps["profuturo"])

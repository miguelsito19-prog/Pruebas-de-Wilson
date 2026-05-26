# DICCIONARIO DE COMISIONES
comisiones = {"ONP":0.13, "Habitat":0.0147, "Integra":0.0155, "Prima":0.016, "Profuturo":0.0169}
 
indice_afp = {1:"Habitat", 2:"Integra", 3:"Prima", 4:"Profuturo"}

# VALORES UNIVERSALES DE LAS AFP
aporte_obligatorio = 0.1
prima_seguro = 0.0137
universal = aporte_obligatorio + prima_seguro

# DEFINICIONES DE SISTEMAS DE PENSIONES, CUENTAS Y SUELDOS

def calculo_bruto():
    while True:
        try:
            sueldo_bruto = int(input("Ingrese el sueldo en bruto: "))
            if sueldo_bruto >= 565:
                break
            print("Error: Ingreso un sueldo por debajo de lo permitido por planilla")
        except ValueError:
            print("Error: Ingreso valores invalidos")
    return sueldo_bruto

sistema_onp = lambda sueldo_bruto: sueldo_bruto - (sueldo_bruto * comisiones["ONP"])

def sistema_afp(sueldo_bruto, comision, cuentas):
    if cuentas == 0:
       sueldo_neto = sueldo_bruto - (sueldo_bruto * (universal + comision))
    elif cuentas == 1:
        sueldo_neto = sueldo_bruto - (sueldo_bruto * universal)
    print(f"El sueldo neto estimado es de S/{sueldo_neto:,.2f}")

def eleccion_cuentas():
    while True:
        try:
            cuenta = int(input("Ingrese 0 si tiene cuenta flujo o 1 si es mixta: "))
            if 2 > cuenta > -1:
                break
            print("Error: Ingreso un numero invalido")
        except ValueError:
            print("Error: Ingreso valores invalidos")
    return cuenta
            
def eleccion_sistemas():
    while True:
        try:
            sistema = int(input("Ingrese el digito del sistema: "))
            if 5 > sistema > -1:
                break
            print("Error: Ingreso un numero invalido")
        except ValueError:
            print("Error: Ingreso valores invalidos")
    return sistema


# CODIGO
sueldo_bruto = calculo_bruto()
for indice, pensiones in enumerate(comisiones):
    print(f"{pensiones} -> [{indice}]")
sistemas = eleccion_sistemas()
if sistemas == 0:
    print(f"El sueldo neto estimado es de S/{sistema_onp(sueldo_bruto):,.2f}")
else:
    nombre_afp = comisiones[indice_afp[sistemas]]
    cuentas = eleccion_cuentas()
    sistema_afp(sueldo_bruto, nombre_afp, cuentas)
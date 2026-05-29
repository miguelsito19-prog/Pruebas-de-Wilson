"""CALCULADORA DE PENSIONES"""

# DICCIONARIO DE COMISIONES
comisiones = {
    "ONP": 0.13,
    "Habitat": 0.0147,
    "Integra": 0.0155,
    "Prima": 0.016,
    "Profuturo": 0.0169,
}

# DICCIONRARIO DE NOMBRES DE PENSIONES
indice_comisiones = {0: "ONP", 1: "Habitat", 2: "Integra", 3: "Prima", 4: "Profuturo"}

# VALORES UNIVERSALES
aporte_obligatorio = 0.1
prima_seguro = 0.0137
universal = aporte_obligatorio + prima_seguro


def calculo_bruto():
    while True:
        try:
            sueldo_bruto = float(input("Ingrese el sueldo en bruto: "))
            if sueldo_bruto >= 565:
                break
            print("Errror: Dede ingresar un sueldo de planilla")
        except ValueError:
            print("Error: Ingreso valores invalidos")
    return sueldo_bruto


def eleccion_sistema():
    while True:
        try:
            sistema = int(input("Ingrese el sistema: "))
            if sistema in indice_comisiones:
                break
            print("Error: Ingreso un valor invalido")
        except ValueError:
            print("Error: Ingreso un valor invalido")
    return sistema


def sistema_onp(sueldo_bruto):
    sueldo_neto = sueldo_bruto - (sueldo_bruto * comisiones["ONP"])
    return sueldo_neto


def cuenta_afp():
    while True:
        try:
            cuenta = int(input("Ingrese el digito de la cuenta: "))
            if cuenta in [0, 1]:
                break
            print("Error: Ingreso un valor invalido")
        except ValueError:
            print("Error: ingreso un valor invalido")
    return cuenta


def sistema_afp(sueldo_bruto, comision, universal, cuentas):
    if cuentas == 0:
        sueldo_neto = sueldo_bruto - (sueldo_bruto * (universal + comision))
    else:
        sueldo_neto = sueldo_bruto - (sueldo_bruto * universal)
    return sueldo_neto


# CODIGO
sueldo_bruto = calculo_bruto()
for indice, nombre in enumerate(comisiones):
    print(f"{nombre} -> [{indice}]")
sistemas = eleccion_sistema()
if sistemas == 0:
    sueldo_onp = sistema_onp(sueldo_bruto)
    print(f"El sueldo neto estimado es de S/{sueldo_onp:,.2f}")
else:
    print("Cuenta Mixta -> [0]")
    print("Cuenta Flujo -> [1]")
    cuentas = cuenta_afp()
    sueldo_afp = sistema_afp(
        sueldo_bruto, comisiones[indice_comisiones[sistemas]], universal, cuentas
    )
    print(f"El sueldo neto estimado es de S/{sueldo_afp:,.2f}")

"""CALCULADORA DE PENSIONES"""
# DICCIONARIO DE COMISIONES
comisiones = {
    "ONP": 0.13,
    "Habitat": 0.0147,
    "Integra": 0.0155,
    "Prima": 0.016,
    "Profuturo": 0.0169
}

# DICCIONRARIO DE NOMBRES DE PENSIONES
indice_comisiones = {0:"ONP", 1:"Habitat", 2:"Integra", 3:"Prima", 4:"Profuturo"}

# VALORES UNIVERSALES
aporte_obliogatorio = 0.1
prima_seguro = 0.0137
universal = aporte_obliogatorio + prima_seguro 

# DEFINIENDO SISTEMA ONP
def sistema_onp(sistema):
    print(f"Se encuentra en el sistema {indice_comisiones[sistema]}")
    sueldo_neto = sueldo_bruto - (sueldo_bruto * comisiones["ONP"])
    print(f"El sueldo neto es de S/{sueldo_neto:,.2f}")
        
# DEFINIENDO CUENTAS
def cuentas(sueldo_bruto, comisiones, sistema):
    print(f"Se encuentra en el sistema {indice_comisiones[sistema]}")
    while True:
        try:
            cuenta = int(input("Ingrese 0 para cuenta flujo o 1 para mixta: "))
            if  2 > cuenta > -1:
                break
            else:
                print("Ingreso un valor invalido")
        except ValueError: 
            print("Ingreso un valor invalido")
    if cuenta == 0:
        sueldo_neto = sueldo_bruto - (sueldo_bruto * (universal + comisiones))
    elif cuenta == 1:
        sueldo_neto = sueldo_bruto - (sueldo_bruto * universal)
    print(f"El sueldo neto es de S/{sueldo_neto:,.2f}")

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
        
# SISTEMAS DE PENSIONES
for indice, pension in enumerate(comisiones):
    print(f"{pension} -> {indice}")

while True:
    try:
        sistema = int(input("Ingrese el sistema: "))
        if sistema in indice_comisiones:
            break
        else:
            print("Ingrese un digito valido")
    except ValueError:
        print("Ingrese un valor valido")

if sistema == 0:
    sistema_onp(sistema)
else:
    nombre_afp = indice_comisiones[sistema]
    cuentas(sueldo_bruto, comisiones[nombre_afp], sistema)
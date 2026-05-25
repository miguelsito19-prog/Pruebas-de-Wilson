"""CALCULADORA DE SUELDO NETO"""

# DATOS DEL USUARIO
nombre = input("Ingresa tu nombre: ")
while True:
    try:
        sueldo_bruto = float(input("Ingresa tu sueldo bruto: "))
        break
    except ValueError:
        input("Por favor, ingrese un valor numerico: ")

# CALCULANDO EL VALOR DE LA AFP
aporte_obligatorio = 0.1
seguro_prima = 0.0135
while True:
    try:
        comision_afp = float(input("Ingrese si esta en cuenta flujo 0.0147 o si esta en cuenta mixta 0: "))
        if comision_afp == 0.0147 or comision_afp == 0:
            break
    except ValueError:
        input("Por favor, ingrese 0.0147 o 0")
afp_total = aporte_obligatorio + seguro_prima + comision_afp
descuento_afp = sueldo_bruto * afp_total

# CALCULANDO EL SUELDO NETO
sueldo_neto = sueldo_bruto - descuento_afp
print(f"Hola {nombre} tu sueldo neto es: {sueldo_neto}")
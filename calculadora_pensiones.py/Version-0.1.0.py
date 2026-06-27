""""Calculadora de sueldo"""
"""Nombre del trabajador"""
nombre = input("Ingrese el nombre: " )
"""Sueldo en bruto"""
sueldo_bruto = float(input("Ingrese el sueldo bruto: "))
"""Parametros de AFP Habitat"""
Aporte_obligatorio = 0.10
Prima_seguro = 0.0135
Comision_AFP = float(input("Ingrese 0.0147 si tiene cuenta flujo, si tiene cuenta saldo ponga 0: "))
AFP_total = Aporte_obligatorio + Prima_seguro + Comision_AFP
AFP_descuento = sueldo_bruto * AFP_total
"""Calculando sueldo neto"""
sueldo_neto = sueldo_bruto - AFP_descuento
print(f"Hola, {nombre}, su sueldo neto es {sueldo_neto:.2f} ")

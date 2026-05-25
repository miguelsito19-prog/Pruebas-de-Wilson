"""CALCULADORA DE SUELDO NETO"""

# DATOS DEL USUARIO
while True:
    try:
        salario_bruto = float(input("Ingrese su salario en bruto: "))
        if salario_bruto > 0:
            break
        elif salario_bruto < 0:
            print("Debe ingresar un valor positivo")
    except ValueError:
        print("Por favor, ingrese un valor numerico")

# VALORES UNIVERSALES
aporte_obligatorio = 0.1
prima_seguro = 0.0137 # PRIMA SEGURO NO ES DE PRIMA AFP, ASI SE LE LLAMA AL SEGURO POR INVALIDEZ, DESEMPLEO, ETC

# ELIGIENDO EL SISTEMA DE PENSIONES
while True:
    try:
        system = int(input("Ingrese 0 si es ONP, 1 si es AFP Habitat, 2 si es AFP Integra, 3 si es Prima AFP, 4 si es Profututro AFP: "))
        if system == 0 or system == 1 or system == 2 or system == 3 or system == 4:
            break
        elif system != 0 or system != 1 or system != 2 or system != 3 or system != 4:
            print("Digite los valores solicitados")
    except ValueError:
        print("Debe digitar solo los valores solicitados")

# SISTEMA DE PENSIONES: ONP
if system == 0:
    print("Usted esta en el sistema de pensiones: ONP")
    aporte_ONP = 0.13
    salario_neto = salario_bruto - (salario_bruto * aporte_ONP)
    print(f"Su salario neto es de {salario_neto}")
    
# SISTEMA DE PENSIONES: AFP Habitat
elif system == 1:
    while True:
        try:
            print("Usted pertenece al sistema de pensiones AFP: En AFP Habitat")
            cuenta = int(input("Ingrese 0 si tiene cuenta flujo o 1 si tiene cuenta mixta: "))
            if cuenta == 0 or cuenta == 1:
                if cuenta == 0:
                    comision_AFP_Habitat = 0.0147
                    total_habitat = aporte_obligatorio + prima_seguro + comision_AFP_Habitat
                    descuento_habitat = salario_bruto * total_habitat
                    salario_neto = salario_bruto - descuento_habitat
                    print(f"Su salario neto es de {salario_neto}")
                    break
                elif cuenta == 1:
                    total_habitat = aporte_obligatorio + prima_seguro
                    descuento_habitat = salario_bruto * total_habitat
                    salario_neto = salario_bruto - descuento_habitat
                    print(f"Su salario neto es de: {salario_neto}")
                    break
        except ValueError: 
            print("Digite solo los valores solicitados")
        
# SISTEMA DE PENSIONES AFP: AFP Integra
elif system == 2:
    while True:
        try:
            print("Usted pertenece al sistema de pensiones AFP: En AFP Integra")
            cuenta = int(input("Ingrese 0 si tiene cuenta flujo o 1 si tiene cuenta mixta: "))
            if cuenta == 0 or cuenta == 1:
                if cuenta == 0:
                    comision_AFP_integra = 0.0155
                    total_integra = aporte_obligatorio + prima_seguro + comision_AFP_integra
                    descuento_integra = salario_bruto * total_integra
                    salario_neto = salario_bruto - descuento_integra
                    print(f"Su salario neto es de {salario_neto}")
                    break
                elif cuenta == 1:
                    total_integra = aporte_obligatorio + prima_seguro
                    descuento_integra = salario_bruto * total_integra
                    salario_neto = salario_bruto - descuento_integra
                    print(f"Su salario neto es de: {salario_neto}")
                    break
        except ValueError:
            print("Digite solo los valores solicitados")
        
# SISTEMA DE PENSIONES AFP: Prima AFP
elif system == 3:
    while True:
        try:
            print("Usted pertence al sistema de pensiones AFP: Prima AFP")
            cuenta = int(input("Ingrese 0 si tiene cuenta flujo o 1 si tiene cuenta mixta: "))
            if cuenta == 0 or cuenta == 1:
                if cuenta == 0:
                    comision_PrimaAFP = 0.016
                    total_PrimaAFP = comision_PrimaAFP + aporte_obligatorio + prima_seguro
                    descuento_PrimaAFP = total_PrimaAFP * salario_bruto
                    salario_neto = salario_bruto - descuento_PrimaAFP
                    print(f"Su salario neto es de: {salario_neto}")
                    break
                elif cuenta == 1:
                    total_PrimaAFP = aporte_obligatorio + prima_seguro
                    descuento_PrimaAFP = salario_bruto * total_PrimaAFP
                    salario_neto = salario_bruto - descuento_PrimaAFP
                    print(f"Su salario neto es de: {salario_neto}")
                    break
        except ValueError:
            print("Digite solo los valores solicitados")

# SISTEMA DE PENSIONES AFP: Profuturo AFP
elif system == 4:
    while True:
        try:
            print("Usted pertenece al sistema de pensiones AFP: Profuturo AFP")
            cuenta = int(input("Ingrese 0 si su cuenta es flujo o 1 si su cuenta es mixta: "))
            if cuenta == 0 or cuenta == 1:
                if cuenta == 0:
                    comision_ProfuturoAFP = 0.0169
                    total_ProfuturoAFP = aporte_obligatorio + prima_seguro + comision_ProfuturoAFP
                    descuento_ProfuturoAFP = salario_bruto * total_ProfuturoAFP
                    salario_neto = salario_bruto - descuento_ProfuturoAFP
                    print(f"Su salario neto es de: {salario_neto}")
                    break
                elif cuenta == 1:
                    total_ProfuturoAFP = aporte_obligatorio + prima_seguro
                    descuento_ProfuturoAFP = salario_bruto * total_ProfuturoAFP
                    salario_neto = salario_bruto - descuento_ProfuturoAFP
                    print(f"Su salario neto es de: {salario_neto}")
                    break
        except ValueError:
            print("Digite solo los valores solicitados")

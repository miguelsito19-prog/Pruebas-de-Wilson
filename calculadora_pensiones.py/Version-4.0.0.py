class GestionPensiones:
# INFORMACION EN ESTRUCTURA DE DATOS
    COMISIONES = {
    0: {"nombre": "ONP", "porcentaje": 0.13},
    1: {"nombre": "Habitat", "porcentaje": 0.0147},
    2: {"nombre": "Integra", "porcentaje": 0.0155},
    3: {"nombre": "Prima", "porcentaje": 0.016},
    4: {"nombre": "Profuturo", "porcentaje": 0.0169}
    }
    CUENTAS_AFP = {0:"Flujo", 1:"Sobre Saldo"}
# INFORMACION EN VARIABLES
    APORTE_OBLIGATORIO, PRIMA_SEGURO, SUELDO_MINIMO = 0.1, 0.0137, 565
    UNIVERSAL = APORTE_OBLIGATORIO + PRIMA_SEGURO
# FUNCION MEMORIA
    def __init__(self):
        self.sueldo_bruto = 0
        self.sistema = None
        self.cuenta = None
        self.sueldo_neto = 0 
# FUNCION GENERICA DE VALIDACION DE ENTRADA DE DATOS
    def validacion(self, mensaje, mensaje_error, tipo_variable=None, condicion=None, valor_minimo=None):
        while True:
            try:
                variable = tipo_variable(input(mensaje))
                if condicion is not None and variable in condicion:
                    return variable
                elif valor_minimo is not None and variable >= valor_minimo:
                    return variable
                print(mensaje_error)    
            except ValueError:
                print("Error: Ingreso un valor invalido")
# FUNCION DE INGRESO DE SUELDO EN BRUTO            
    def ingreso_sueldo_bruto(self):
        self.sueldo_bruto = self.validacion("Ingrese el sueldo en bruto: ", "Error: Ingreso un sueldo por debajo del minimo en planilla", float, None, self.SUELDO_MINIMO)
# FUNCION DE ELECCION DE SISTEMA DE PENSIONES    
    def eleccion_sistema(self):
        self.sistema = self.validacion("Ingrese el digito de su sistema de pension: ", "Error: Ingreso un digito no registrado", int, range(len(self.COMISIONES)), None)
# FUNCION DE CALCULO DEL SISTEMA ONP     
    def sistema_onp(self):
        self.sueldo_neto = self.sueldo_bruto - (self.sueldo_bruto * self.COMISIONES[0]["porcentaje"])
# FUNCION DE ELECCION DEL SISTEMA AFP    
    def eleccion_afp(self):
        self.cuenta = self.validacion("Ingrese el digito de la cuenta: ", "Error: Ingreso un digito no registrado", int, self.CUENTAS_AFP, None)
# FUNCION DE CALCULO DEL SISTEMA AFP SEGUN CUENTA FLUJO O SOBRE SUELDO     
    def sistema_afp(self):
        if self.cuenta == 0:
            self.sueldo_neto = self.sueldo_bruto - (self.sueldo_bruto * (self.UNIVERSAL + self.COMISIONES[self.sistema]["porcentaje"]))
        else:
            self.sueldo_neto = self.sueldo_bruto - (self.sueldo_bruto * self.UNIVERSAL)
# EJECUCION DEL CODIGO            
if __name__ == "__main__":
    usuario = GestionPensiones()
    usuario.ingreso_sueldo_bruto()
    for indice, datos in usuario.COMISIONES.items():
        print(f"[{indice}] -> {datos['nombre']}")
    usuario.eleccion_sistema()
    match usuario.sistema:
        case 0:
            usuario.sistema_onp()
        case _:
            for indice, nombre in usuario.CUENTAS_AFP.items():
                print(f"[{indice}] -> {nombre}")
            usuario.eleccion_afp()
            usuario.sistema_afp()   
    print(f"El sueldo estimado es de S/{usuario.sueldo_neto:,.2f}")
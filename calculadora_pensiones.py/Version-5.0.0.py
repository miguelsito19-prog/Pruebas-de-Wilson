class GestionPensiones:
    # INFORMACION EN ESTRUCTURA DE DATOS
    COMISIONES = {"ONP":0.13, "Habitat":0.0147, "Integra":0.0155, "Prima":0.016, "Profuturo":0.0169}
    INDICES = {indice: sistema for indice, sistema in enumerate(COMISIONES)}
    CUENTAS_AFP = {0:"Flujo", 1:"Sobre Saldo"}
    # INFORMACION EN VARIABLES
    APORTE_OBLIGATORIO, PRIMA_SEGURO = 0.1, 0.0137
    UNIVERSAL = APORTE_OBLIGATORIO + PRIMA_SEGURO
    SUELDO_MINIMO = 565
    # FUNCION GENERICA DE VALIDACION DE ENTRADA DE DATOS
    def validacion(self, mensaje, mensaje_error, tipo_variable=None, diccionario=None, constante=None):
        while True:
            try:
                variable = tipo_variable(input(mensaje))
                if diccionario is None and variable >= constante:
                    return variable
                elif constante is None and variable in diccionario:
                    return variable
                print(mensaje_error)    
            except ValueError:
                print("Error: Ingreso un valor inválido")
    # FUNCION DE INGRESO DE SUELDO EN BRUTO            
    def ingreso_sueldo_bruto(self):
        return self.validacion("Ingrese el sueldo en bruto: ", "Error: Ingreso un sueldo por debajo del minimo en planilla", float, None, self.SUELDO_MINIMO)
    # FUNCION DE ELECCION DE SISTEMA DE PENSIONES    
    def eleccion_sistema(self):
        return self.validacion("Ingrese el digito de su sistema de pension: ", "Error: Ingreso un digito no registrado", int, self.INDICES, None)
    # FUNCION DE CALCULO DEL SISTEMA ONP     
    def sistema_onp(self, sueldo_bruto):
        return sueldo_bruto - (sueldo_bruto * self.COMISIONES["ONP"])
    # FUNCION DE ELECCION DEL SISTEMA AFP    
    def eleccion_afp(self):
        return self.validacion("Ingrese el digito de la cuenta: ", "Error: Ingreso un digito no registrado", int, self.CUENTAS_AFP, None)
    # FUNCION DE CALCULO DEL SISTEMA AFP SEGUN CUENTA FLUJO O SOBRE SUELDO     
    def sistema_afp(self, cuenta, sueldo_bruto, constante, comision):
        if cuenta == 0:
            return sueldo_bruto - (sueldo_bruto * (constante + comision))
        else:
            return sueldo_bruto - (sueldo_bruto * constante)
    # EJECUCION DEL CODIGO            
if __name__=="__main__":
    Empleado = GestionPensiones()
    sueldo_bruto = Empleado.ingreso_sueldo_bruto()
    for indice, nombre in enumerate(Empleado.COMISIONES):
        print(f"[{indice}] -> {nombre}")
    sistema = Empleado.eleccion_sistema()
    if sistema == 0:
        sueldo_neto = Empleado.sistema_onp(sueldo_bruto)
    else:
        for indice, nombre in Empleado.CUENTAS_AFP.items():
            print(f"[{indice}] -> {nombre}")
        cuentas = Empleado.eleccion_afp()
        sueldo_neto = Empleado.sistema_afp(cuentas, sueldo_bruto, Empleado.UNIVERSAL, list(Empleado.COMISIONES.values())[sistema])
    print(f"El sueldo estimado es de S/{sueldo_neto:,.2f}")
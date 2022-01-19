class CuentaBancaria:
    cuentas = []
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance= balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print('balance: $%d'%(self.balance))
        return self

    def generar_interes(self):
        self.balance=self.balance*( 1 +self.tasa_interes/100)
        return self 
    @classmethod
    def imprimir_todas_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()
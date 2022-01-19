from CuentaBancaria import CuentaBancaria
cuenta1=CuentaBancaria(3,1000)
cuenta2=CuentaBancaria(5,2000)

cuenta1.deposito(200).deposito(200).deposito(200).retiro(100).generar_interes()
cuenta1.mostrar_info_cuenta()

cuenta2.deposito(300).deposito(300).retiro(200).retiro(200).retiro(500).retiro(500).generar_interes()
cuenta2.mostrar_info_cuenta()
print("********** imprimir_todas_cuentas **********")
CuentaBancaria.imprimir_todas_cuentas()
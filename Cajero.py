class CuentaBancaria:
    def __init__(self, nombre,saldo, banco, contraseña ):
        self.nombre = nombre
        self.saldo = saldo
        self.banco = banco
        self.contraseña = contraseña

    def atributos(self):
        print(f"{self.nombre}: ")
        print(f".Saldo: ${self.saldo}")
        print(f".Banco: {self.banco}")
        print(f".Contraseña: {self.contraseña}")

    def cambiar_contraseña(self):
        self.contraseña = str(input("Digite su nueva contraseña: "))
        



mi_cuenta = CuentaBancaria("Felipe", 30000, "Bancolombia", "1234")
mi_cuenta.cambiar_contraseña()
mi_cuenta.atributos()
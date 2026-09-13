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
        while True:
            self.contraseña = str(input("Digite su nueva contraseña: "))
            if len(self.contraseña) >=8:
                if not self.contraseña.isalnum():
                    break
                else:
                    print("Su contraseña debe tener como minimo un caracter especial")
            else:
                print("Su contraseña no puede ser menor a 8 digitos")

    def retirar(self):
        while True:
            retiro = int(input("Digite cuanto va a retirar: "))
            if retiro > 0:
                if retiro <= self.saldo:
                    print(f"Usted a retirado ${retiro} COP")
                    self.saldo -= retiro
                    return self.saldo
                    break
                else:
                    print("Error, usted no puede retirar mas de lo que tiene")
            else:
                print("Error, usted no puede retirar una cantidad menor a $0 COP")
            

    def depositar(self):
        while True:
            deposito = int(input("Digite cuanto va a depositar: "))
            if deposito >= 0:
                print(f"Usted ha depositado ${deposito} COP")
                self.saldo += deposito
                return self.saldo
                break
            else:
                print("Error, usted no puede depositar una cantidad menor a $0 COP")
            
                    
                    

    def saludar():
        print("hola")
        



mi_cuenta = CuentaBancaria("Felipe", 30000, "Bancolombia", "1234")
mi_cuenta.retirar()
mi_cuenta.atributos()

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

    def comprobador(self, mensaje):
        while True:
            try:
                monto = float(input(mensaje))
                if monto <0:
                    print("Error, no puede digitar una cantidad menor a 0")
                elif monto == 0:
                    print("Operacion cancelada por el usuario")
                    return 0
                else:
                    return monto
            except ValueError:
                print("ERROR: no puede digitar un caracter diferente a entero/decimal")

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
        retiro = self.comprobador("Digite cuanto va a retirar( o 0 para salir ): ")
        if retiro == 0:
            return
        
        elif retiro <= self.saldo:
            print(f"Usted a retirado ${retiro} COP")
            self.saldo -= retiro
        else:
            print("Error, usted no puede retirar mas de lo que tiene")
            
    def depositar(self):
        deposito = self.comprobador("Digite cuanto va a depositar( o 0 para salir ): ")
        if deposito == 0:
            return

        print(f"Usted ha depositado ${deposito} COP")
        self.saldo += deposito
        
    def InicioSesion(self):
        while True:
            contraseña_usuario = str(input("Bienvenido! digite su contraseña: "))
            if contraseña_usuario == self.contraseña:
                print(f"Bienvenido señor/a {self.nombre}")
                return True
            else:
                print("Error: digite su contraseña denuevo") 

    def MenuInteractivo(self):
        while True:
            menu = int(input("""
            Bienvenido asu menu interactivo, digite una opcion:
            1 para consultar estado de la cuenta
            2 para retirar saldo
            3 para depositar saldo
            4 para cambiar la contraseña
            5 para salir :)
            """))
            match menu:
                case 1:
                    self.atributos()
                case 2:
                    self.retirar()
                case 3:
                    self.depositar()
                case 4:
                    self.cambiar_contraseña()
                case 5:
                    print("Hazta luego!")
                    break
                case _:
                    print("Error, intentelo denuevo")

                
    def FlujodeControl(self):
        if self.InicioSesion() == True:
            self.MenuInteractivo()
        
    def saludar():
        print("hola")

mi_cuenta = CuentaBancaria("Felipe", 30000, "Bancolombia", "1234567$")
mi_cuenta.FlujodeControl()
        
            
        
                
            
        
        
        
                    
            

                    
                
                








        




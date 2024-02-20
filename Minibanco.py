#Clase hereditaria
class Usuario:
    
    #Uso de metodo constructor para añadir parametrosSergio
    #Objetos de Clase Usuario
    #Uso de def para definir una nueva funcion
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

#Clase heredada de usuario
class RegistroCuenta(Usuario):
    pass

    #Objetos de Clase RegistroCuentas
    def __init__(self, nombre, apellido, cedula,tipo_cuenta, numero_cuenta, valor_consignado):
        
        #Uso de función super para "traer" información de la clase hereditaria
        super().__init__(nombre, apellido, cedula)
        self.tipo_cuenta = tipo_cuenta
        self.numero_cuenta = numero_cuenta
        self.valor_consignado =  valor_consignado

    #Uso de metodo get para obtener la información de las clases Usuario y RegistroCuentas
    #Uso de return para conocer la información ingresada por el cliente
    def get_user_info(self):
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Cedula: {self.cedula}
        Tipo de cuenta: {self.tipo_cuenta}
        Numero de cuenta: {self.numero_cuenta}
        Valor consignado: {self.valor_consignado}
        """

#Creación de formulario para que el cliente ingrese su información
nombre = input("Nombre del cliente: ")
apellido = input("Apellido del cliente: ")
cedula = input("Cedula del cliente: ")
tipo_cuenta = input("Tipo de cuenta del cliente: ")
numero_cuenta = input("Numero de cuenta del cliente: ")
valor_consignado = input("Valor consignado por el cliente: ")

Cuenta_nueva = RegistroCuenta(nombre, apellido, cedula,tipo_cuenta, numero_cuenta, valor_consignado)

print(Cuenta_nueva.get_user_info())
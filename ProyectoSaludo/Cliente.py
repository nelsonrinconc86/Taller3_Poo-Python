# ***** zona de clase ****
#se crea la clase
class Cliente:
    #se crea el metodo constructo de la clase
    def __init__(self):
        # se crean los atributos de la clase
        self.nombre_cliente = ""
        self.apellido_cliente = ""
    
    # crear metodos get y set por atributos
    def get_nombre(self):
        return self.nombre_cliente
    
    def get_apellido(self):
        return self.apellido_cliente
    
    def set_nombre(self, dato_nombre):
        self.nombre_cliente = dato_nombre
    
    def set_apellido(self, dato_apellido):
        self.set_apellido = dato_apellido
    
    # se crean metodos normales de la clase
    
    def tomar_datos(self):
        pass
    
    def procesar_datos():
        pass
    
    def mostrar_info():
        pass
    
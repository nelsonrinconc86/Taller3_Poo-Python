from Cliente import Cliente
from Saludo import Saludo
# ++++ Codigo Principal +++

# Creando objetos
objCliente = Cliente()
objSaludo = Saludo()
# uso los metodos de los objetos
objCliente.tomar_datos()
aux_mensaje = objSaludo.hacer_saludo_formal()
objCliente.hacer_saludo(aux_mensaje)


# llamo a los metodos del objeto

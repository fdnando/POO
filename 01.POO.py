class Ser_vivo():


	def __init__(self,vida,h2o,carbono):

		self.vida=vida
		self.h2o=h2o
		self.carbono=carbono


	def alimentacion(self):
		print("Obtengo nutrientes para seguir con vida")
	def respiracion(self):
		print("Obtengo oxígeno para seguir con vida")




class Mamíferos(Ser_vivo):

	def __init__(self,extremidades,columna_vertebral):

		self.extremidades=extremidades
		self.columna_vertebral=columna_vertebral

	def movilidad(self):
		print("Puedo desplazarme")



class Persona(Mamíferos):

	def pensar(self):
		print("Hago uso de la razón")	


niño=Persona(4,1)

print(niño.extremidades)










class Ser_vivo():


	def__init__(self,vida,h2o,carbono):

		self.vida=True
		self.h2o=True
		self.carbono=True


	def alimentacion(self):
		print("Obtengo nutrientes para seguir con vida")
	def respiracion(self):
		print("Obtengo oxígeno para seguir con vida")




class Mamíferos(Ser_vivo):

	def__init__(self,extremidades,columna_vertebral):

		self.extremidades=4
		self.columna_vertebral=True

	def movilidad(self):
		print("Puedo desplazarme")



class Persona(Ser_vivo,Mamíferos):

	def pensar(self):
		print("Hago uso de la razón")	



niño=Persona()

print(niño.extremidades)









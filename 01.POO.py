

class Ser_vivo():

	# método mágico (constructor)


	def __init__(self,vida,edad):

		self.vida=vida
		self.edad=edad

	def alimentacion(self):
		print("Obtengo nutrientes para seguir con vida")	


	#método estático

	@staticmethod
	def respiracion():
		print("Siempre respiro")

	def cumplir_años(self):

		print("Ha cumplido otro años más, ahora tiene " + str(self.edad+1))	




class Mamiferos(Ser_vivo):

	def __init__(self,vida,edad,extremidades):


		#hereda de Ser_vivo

		Ser_vivo.__init__(self,vida,edad)

		self.extremidades=extremidades
		

	def movilidad(self):
		print("Puedo desplazarme con mis " + str(self.extremidades) + " extremidades")


	#sobre carga de operadores	

	def __add__(self,otros):

		total_extremidades= self.extremidades + otros.extremidades

		return total_extremidades	



class Persona(Mamiferos):


	def __init__(self,vida,edad,extremidades,pensar,identificador):

		
		Mamiferos.__init__(self,vida,edad,extremidades)

		self.pensar=pensar

		#visibilidad (privado entre comillas)

		self.__identificador=identificador




	def pensando(self):

		if self.pensar==True:

			print("Este humano piensa")

		else:
			
			print("Este humano no piensa ")	



	#método mágico

	def __repr__(self):
		return f"<identificador persona (DNI) : {self.__identificador}>"		


#instancio clases			

niño1=Persona(True,5,4,True,33)

niño2=Persona(True,7,4,False,45)





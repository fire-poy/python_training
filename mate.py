class Mate:
	def __init__(self, marca_yerba, q_azucar, q_agua, temp_agua): 
		self.yerba = marca_yerba
		self.azucar = q_azucar	
		self.agua = q_agua	
		self.temperatura = temp_agua
		self.cebado = 0

	def cebar(self):
		while self.agua > 0:
			if self.azucar > 0:
				print("para dulce esta la vida... amargo!")
				print("Cebando mate con yerba " + self.yerba + " y " + self.azucar + "gramos de azucar")
			else:
				print("Cebando mate con yerba " + self.yerba)
			print(f"Agregando {self.agua} de agua a {self.temperatura} grados")
			# print(f"Agregando " + self.agua + " de agua a " + self.temperatura + " grados")
			print("Disfrutar!")
			self.agua -= 30
			self.cebado += 30
			if self.cebado > 100:
				print("El mate esta lavado")
				break

		
		

# funcion que separa la variable de entorno PATH en una lista de directorios
# Autor: Javier Ramos <javier.ramos at uam.es>
# 2019 EPS-UAM

import os

def split_path(path):
	return path.split(os.pathsep)

if __name__ == "__main__":#si se ejecuta como programa principal, no como modulo
	print("El nombre del sistema operativo es: " + os.name + '\n')
	print("La variable de entorno PATH contiene los siguientes directorios:\n")
	paths = split_path(os.environ["PATH"])
	for path in paths:
		print(path)




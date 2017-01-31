#!/usr/bin/python3

fichero = open("/etc/passwd","r")

lineas = fichero.readlines()
fichero.close()

for linea in lineas:
	User = linea.split(':')[0]
	Shell = linea.split(':')[-1][:-1]
	print(User, Shell)
	
print("Hay " + str(len(lineas)) + " usuarios")	
	

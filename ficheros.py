#!/usr/bin/python3

fichero = open("/etc/passwd","r")

lineas = fichero.readlines()
fichero.close()

for linea in lineas:
	Shell = linea.split(":")
	print(Shell[0])
	
print("Hay " + str(len(lineas)) + " usuarios")	
	

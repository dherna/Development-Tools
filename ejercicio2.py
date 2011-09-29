#!/usr/bin/env python
usuario=raw_input("¿Qué usuairo comprobamos?")

try:
	fichero = file('/etc/passwd','r')
except IOError:
	print "Esto no es un sistama Linux"
else:
   while True:
     linea = fichero.readline()
     if not linea: break
     dato = linea.split(":")
     #shell=
    if shell.has_key(usuario):
        print "El usuario " + usuario + " tiene el shell: " + shell[usuario]
    else:
        print "El usuario " + usaurio + " no está en el sistema"

print "fin del ejercicio2" 


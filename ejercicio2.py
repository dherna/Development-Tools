#!/usr/bin/env python
usuario=raw_input("Que usuairo comprobamos?")

try:
   fichero = file('/etc/passwd','r')
except IOError:
   print "Esto no es un sistama Linux"
else:
   shell={}
   while True:
     linea = fichero.readline()
     if not linea: break
     dato = linea.split(":")
     shell[dato[0]] = dato[6]
   if shell.has_key(usuario):
     print "El usuario " + usuario + " tiene el shell: " + shell[usuario]
   else:
     print "El usuario " + usuario + " no esta en el sistema"

print "fin del ejercicio2" 


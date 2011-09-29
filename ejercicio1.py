#!/usr/bin/env python
try:
        fichero = file('/etc/passwd','r')
except IOError:
        print "Esto no es un sistama Linux"
else:

 while True:
     linea = fichero.readline()
     if not linea: break
     dato = linea.split(":")
     print dato[0]+" --> "+dato[6]
 print "fin del ejercicio1"


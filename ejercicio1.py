#!/usr/bin/env python

fichero = file('/etc/passwd','r')
while True:
     linea = fichero.readline()
     if not linea: break
     dato = linea.split(":")
     print dato[0]+" --> "+dato[6]
print "fin del ejercicio1"


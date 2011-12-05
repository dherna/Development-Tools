#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **
# * ejercicio3.py
# *
# * Copyright 2011 Diego Hernandez <diego.herna@gmail.com>
# * Licencia http://www.gnu.org/copyleft/gpl.html GNU GPL v3 o posterior
# * 
import sys
#    
if __name__ == '__main__':
	if len(sys.argv) != 4:
	    print "Faltan parametros"
	else:
	    pass
	   
	operador1=int(sys.argv[1])
	operacion=sys.argv[2]
	operador2=int(sys.argv[3])

	if operacion=='-':
#     	resta=operador1-operador2
#	print resta
		solucion=operador1-operador2
		print 'el resultado es:',solucion
#	print  ("("+str(operador1)+"-"+str(operador2)")
	elif operacion == '+':
		solucion=operador1+operador2
		print 'el resultado es:',solucion
#        print "se suma"
	elif operacion == '/':
		solucion=operador1/operador2
		print 'el resultado es:',solucion
#        print "se divide"
	elif operacion == '*':
#        print "multiplica"
		solucion=operador1*operador2
		print 'el resultado es:',solucion

 	else:
		print "El operador ingresado no es correcto"


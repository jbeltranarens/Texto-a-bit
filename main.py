#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Codigo que convierte la wea
#ocupe raw_iput porque con string me daba problemas (string=palabras no numeros) en cambio input funciona solo numeros creo

st = raw_input("ingrese algun text :")

print (' '.join(format(ord(x), 'b') for x in st))

#Pd:el nacho se la come xD

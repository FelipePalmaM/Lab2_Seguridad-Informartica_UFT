# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:55:44 2022

@author: elias
"""

with open("mensajedeentrada.txt") as archivo:
    lectura=archivo.read()
    
def split(lectura):
    part=lectura.replace(' ','')
    return part.upper()


mensaje_original=split(lectura)
mensajehash=hash(split(lectura))

alfabeto="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key='FINISPASSWD'

letra_indice=dict(zip(alfabeto,range(len(alfabeto))))
indice_letra=dict(zip(range(len(alfabeto)),alfabeto))

def vigenere(mensaje,key):
    cifrado =""
    split=[mensaje[i:i+len(key)]for i in range(0,len(mensaje),len(key))]
    
    for particiones in split:
        i=0
        for letra in particiones:
            numero=(letra_indice[letra] + letra_indice[key[i]]) % len(alfabeto)
            cifrado += indice_letra[numero]
            i+=1
            
    
    return cifrado

def rot(mensaje,n):
    diccionario="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    auxiliar=""
    for i in mensaje:
        auxiliar= auxiliar + diccionario[(diccionario.find(i)+n)%26]
    
    
    return auxiliar 



cifrado1=vigenere(mensaje_original,key)
cifrado2=rot(cifrado1,8)

archivo2= open("mensajeseguro.txt",'w')
archivo2.write(cifrado2)
archivo2.close()



with open("mensajeseguro.txt") as archivodes:
    lectura2=archivodes.read()

def desrot(mensaje,n):
    diccionario="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    auxiliar=""
    for i in mensaje:
        auxiliar= auxiliar + diccionario[(diccionario.find(i)-n)%26]
    
    
    return auxiliar 

def desvig(cifra,key):
    decifrado=""
    split=[cifra[i:i + len(key)] for i in range(0,len(cifra), len(key))]
    
    for particiones in split:
        i=0
        for letra in particiones:
            numero=(letra_indice[letra]-letra_indice[key[i]]) % len(alfabeto)
            decifrado += indice_letra[numero]
            i+=1
            
    return decifrado

decifrado1=desrot(lectura2, 8)
decifrado2=desvig(decifrado1, key)

decifradohash=hash(decifrado2)

if(mensajehash==decifradohash):
    print('MENSAJE RECIBIDO')



# decifradosiquesi=desvig(mensaje,key)

# print(decifradosiquesi)
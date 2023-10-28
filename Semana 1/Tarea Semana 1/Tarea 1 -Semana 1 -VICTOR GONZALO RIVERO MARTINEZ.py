#!/usr/bin/env python
# coding: utf-8

# In[ ]:


TAREA SEMANA 1 : FUNDAMENTOS DE PYTHON
Nombre : Nombre Completo


# In[ ]:


#Ejercicio 1
#Crea un programa que tome un número ingresado por el usuario y determine si es par o impar.


# In[4]:


numero=int(input())
if numero%2==0:
    print('Es par')
else:
   print('Es impar')


# In[ ]:


#Tuve dificultades en la entrada de datos, convetirlo a entero. Tambien en la operacion modulo a realizar no me
#quedaba claro pero ya le entendi mejor


# In[ ]:


#Ejercicio 2
#Escribe un programa que convierta una cadena de texto en mayúsculas.


# In[7]:


nombre ='victor gonzalo rivero martinez'
nombre_mayusculas = nombre.upper()
print(nombre_mayusculas)


# In[ ]:


#Se utilizo la funcion upper para convertir la cadena a mayusculas


# In[ ]:


#Ejercicio 3
#Crea un programa que lea una cadena de texto ingresada por el usuario y que cuente cuántas 
#veces aparece una letra específica en ella.


# In[110]:


cadena=str(input())
letra=['a']
count=0
i=0
for n in cadena:
    if cadena[i]==letra[0]:
       count+=1
    i+=1
print(count)


# In[ ]:


#Se utilizo un contador, un ciclo for y un if para comparar con la letra especifica. La dificultad estuvo en la comparacion 
#de tipos


# In[ ]:


#Ejercicio 4
#Escribe un programa que determine si un número es primo o no.


# In[101]:


numero= 7
lista= [2,3,4,5,6]
cont = 0
for i in lista:
  if numero==1:
    print("El nÚmero es primo")
    break;
  if numero % i == 0:
    cont +=1
if cont == 0 :
  print("El nÚmero es primo")
else:
  print("El número no es primo" )


# In[ ]:


#La dificultad de este ejercicio esta en establecer los posibles divisores del numero, excepto el 1 y el mismo. 
#se utilizo la funcion if y un contador para verificar si es primo o no


# In[ ]:


#Ejercicio 5
#Crea un programa que calcule el área de un triángulo a partir de la base y la altura ingresadas por el usuario.


# In[13]:


base= float(input('Ingresa la base'))
altura= float(input('Ingresa la altura'))
area=base*altura/2
print(area)


# In[ ]:


#La dificultad esta en darse cuenta de establecer el tipo flotante y los pasos para la formula. Se utilizo el 
#operador multiplicacion y division


# In[14]:


#Ejercicio 6
#Escribe un programa que tome una lista de números y devuelva la suma de todos ellos.


# In[ ]:


lista=[1,2,3]
suma=lista[0]+lista[1]+lista[2]
print(suma)


# In[ ]:


#Se utilizaron listas e indexacion. Saber como sumar cada elemento fue lo dificil


# In[ ]:


#Ejercicio 7
#Crea un programa que reciba una lista de nombres y que imprima solo aquellos 
#que comiencen con una letra específica dada por el usuario.


# In[18]:


lista=['armando','bernado','catalina', 'diego','dantus']
letra=input('Ingresa la letra')
for nombre in lista:
    cad=list(nombre)
    if letra ==cad[0]:
        print(nombre)


# In[ ]:


#La principal dificultad estuvo en identificar la primera letra del nombre


# In[ ]:


#Ejercicio8
#Escribe un programa que determine si una cadena de texto es un palíndromo o no.


# In[37]:


cadena='ana'
lista=list(cadena)
lista2=list(cadena)
pal=[]
pal.append(lista.pop(2))
pal.append(lista.pop(1))
pal.append(lista.pop(0))
print(lista2)
print(pal)
if lista2==pal:
    print('Es un palindromo')
else:
    print('No es un palindromo')


# In[ ]:


#la dificultad esta en como establecer la comparacion de la cadena y la misma al reves. Para ello se utilizo la funcion pop


# In[ ]:


#Ejercicio 9
#Crea un programa que tome una lista de números y elimine todos los duplicados.


# In[44]:


lista=[1,1,2,2,3,4,4,5]
nueva=[]
for n in lista:
    if n not in nueva:
       nueva.append(n)
print(nueva)


# In[ ]:


#Lo dificil es identificar los elementos repetidos y como no agregarlos en la nueva lista. Para ello se utilizo un ciclo for y un ciclo if
# para agregar los nuevos elementos a la lista. posiblemente se pueda realizar con la funcion remove


# In[ ]:


#Ejercicio 10
#Escribe un programa que tome una lista de números y devuelva el valor máximo.


# In[52]:


lista=[1,2,3,4,5]
mayor=lista[0]
for n in lista:
    if n > mayor:
        mayor=n
print(mayor)


# In[ ]:


#La dificultad estuvo en establecer la comparacion para dar con el mayor. Se utilizo un ciclo for y un ciclo if para comparar 
#el numero mayor


# In[ ]:


#Ejercicio 11
#Crea un programa que solicite al usuario su edad y que determine en que etapa de la vida se encuentra:
#Primera Infancia (0-5 años)
#Infancia (6 - 11 años)
#Adolescencia (12 - 18 años)
#Juventud (14 - 26 años)
#Adultez (27- 59 años)
#Persona Mayor (60 años o más).


# In[71]:


edad=int(input('¿Cual es tu edad?'))
if 0<=edad<=5:
    print('Primera Infancia')
elif 6<=edad<=11:
    print('Infancia')
elif 12<=edad<=18:
    print('Adolescencia')
elif 14<=edad<=26:
    print('Juventud')
elif 27<=edad<=59:
    print('Adultez')
elif edad >=60:
    print('Persona Mayor')
    


# In[ ]:


#La difucultad estuvo en establecer los intervalos para verificar la etiqueta correspondiente


# In[72]:


#Ejercicio 12
#Escribe un programa que tome una cadena de texto y que la divida en palabras, eliminando los espacios en blanco.
cadena='victor gonzalo rivero martinez'
nueva = cadena.split()
print(nueva)









# In[ ]:


#En esta ejercicio se utilizo la funcion split para dividir una cadena en palabras separadas por un espacio en blanco


# In[ ]:


#Ejercicio 13
#Crea un programa que tome dos listas de números y que devuelva una tercera lista con los elementos comunes a ambas.


# In[74]:


lista1=[1,2,3,4,5]
lista2=[2,3,6,7,8]
conjunto1=set(lista1)
conjunto2=set(lista2)
elementos_comunes=conjunto1 & conjunto2
print(elementos_comunes)


# In[ ]:


#En este ejercicio se aplico la interseccion a dos conjuntos de numeros


# In[ ]:


#Ejercicio 14
#Escribe un programa que tome una cadena de texto y que cuente cuántas palabras hay en ella.


# In[75]:


cadena=cadena='victor gonzalo rivero martinez'
nueva = cadena.split()
cont=0
for n in nueva:
    cont+=1
print(cont)


# In[ ]:


#En este ejercicio primero se dividio la cadena en palabras y despues se contaron con un ciclo for y un contador


# In[ ]:


#Ejercicio 15
#Crea un programa que calcule el área de un círculo a partir del radio ingresado por el usuario.


# In[77]:


radio=float(input('ingresa el radio:'))
area=3.14*(radio**2)
print(area)


# In[ ]:


#En este ejercicio se utilizo el operador potencia ** y el de multiplicacion para calcular el area del circulo


# In[78]:


#Ejercicio 16
#Escribe un programa que tome una lista de números y que devuelva la media aritmética.


# In[ ]:


lista=[1,2,3,4,5]
cont=0
suma=0
for n in lista:
    cont+=1
for n in lista:
    suma+=n
media=suma/cont
print(media)
    


# In[ ]:


#En este ejercicio se calculo la media, calculando la suma de los elemntos y dividiendo entre el numero de elementos


# In[ ]:


#Ejercicio 17
#Crea un programa que reciba dos número4s ingresados por el usuario y que devuelva su producto.


# In[81]:


numero1=float(input('Ingresa el primer numero:'))
numero2=float(input('Ingresa el segundo numero:'))
producto=numero1*numero2
print(producto)


# In[ ]:



#En este ejercicio se multiplicaron dos numeros aplicando el operador producto


# In[ ]:


#Ejercicio 18
#Escribe un programa que tome una lista de palabras y que devuelva una lista con todas las palabras en mayúsculas.


# In[82]:


lista='victor gonzalo rivero martinez'
palabras=lista.split()
mayusculas=[]
for n in nueva:
    mayusculas.append(n.upper())
print(mayusculas)
    


# In[ ]:


#En este ejercicio se utilizaron las funciones split para dividir la cadena en palabras y postariormente con un ciclo for
#y upper para devolver la lista con las palabras mayusculas


# In[ ]:


#Ejercicio 19
#Crea un programa que tome una lista de números y que devuelva la suma de aquellos que son mayores a un valor específico 
#ingresado por el usuario.


# In[84]:


lista=[1,2,3,4,5]
nueva=[]
numero=int(input('ingresa el numero:'))
for n in lista:
    if n > numero:
        nueva.append(n)
print(nueva)


# In[ ]:


#En este ejercicio se añadieron los numeros mayores al dado por el usuario con la funcion append


# In[ ]:


#Ejercicio 20
#Escribe un programa que tome una cadena de texto y que devuelva una nueva cadena con todas las 
#letras en mayúsculas excepto la primera letra de cada palabra, que debe ser en minúsculas.


# In[89]:


cadena='victor'
may=cadena.upper()
minuscula=may[0]
mayuscula=may[1:6]
nueva=minuscula.lower()+mayuscula
print(nueva)
    


# In[ ]:


#En este ejercicio se aplico la concatenacion de cadenas y la funcion lower. Lo complicado fueron los pasos para
#Obtener la nueva cadena


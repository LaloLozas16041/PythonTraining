#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#TAREA SEMANA 3 : FUNDAMENTOS DE PYTHON
#Nombre : Jose Juan Razo Escamilla
#DISCULPE SI TIENE PROBLEMAS AL EJECUTAR, LO HICE EN ANACONDA


# In[ ]:


#Ejercicio 1
#Escribir dos funciones que simulan una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano o natural (logaritmo en base euler). 


# In[1]:


#A. La función uno preguntará al usuario el intervalo donde quiere aplicar la función matemática y la función a aplicar, y mostrará por pantalla una tabla donde la primera columna será los valores del intervalo dado (x) y la columna 2 tendrá los resultados de el resultado de aplicar la función a este intervalo (y).
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print("calculadora, introduzca en funcion: 'coseno', 'seno', 'tangente', 'exponencial' o 'logaritmo'")
funcion=str(input('introduca que funcion desea llevar a cabo en la calculadora: '))
controlador=True
while controlador:
    if funcion=="coseno" or funcion=="seno" or funcion=="tangente" or funcion=="exponencial" or funcion=="logritmo":
        controlador=False
    else:
        print("esa funcion no es correcta, vuelva a introducir el texto")
        funcion=str(input('introduca que funcion desea llevar a cabo en la calculadora: '))
        
a=float(input('introduza el numero de inicio del dominio de x: '))
b=float(input('introduza el numero de final del dominio de x: '))

print("solo introduzca: funcion_a() o funcion_b() de acuerdo al inciso")
def funcion_a(funcion=funcion,a=a,b=b):
    x=np.arange(a,b+1)
    diccionario={'valores x':[], 'valores y':[]}
    if funcion == 'coseno':
        y = np.cos(x)
        x=list(x)
        y=list(y)
        for i in range(len(x)):
                diccionario["valores x"].append((x[i]))
                diccionario["valores y"].append((y[i]))
                
        print(pd.DataFrame(diccionario))
    
        
    elif funcion == 'seno':
        y=np.sin(x)
        x=list(x)
        y=list(y)
        for i in range(len(x)):
                diccionario["valores x"].append((x[i]))
                diccionario["valores y"].append((y[i]))
                
        print(pd.DataFrame(diccionario))
      
    elif funcion == 'tangente':
        y = np.tan(x)
        x=list(x)
        y=list(y)
        for i in range(len(x)):
                diccionario["valores x"].append((x[i]))
                diccionario["valores y"].append((y[i]))
                
        print(pd.DataFrame(diccionario))
        
    elif funcion == 'exponencial':
        y = np.e**(x)
        x=list(x)
        y=list(y)
        for i in range(len(x)):
                diccionario["valores x"].append((x[i]))
                diccionario["valores y"].append((y[i]))
                
        print(pd.DataFrame(diccionario))
    elif funcion == 'logaritmo':
        y = np.log(x)
        x=list(x)
        y=list(y)
        for i in range(len(x)):
                diccionario["valores x"].append((x[i]))
                diccionario["valores y"].append((y[i]))
                
        print(pd.DataFrame(diccionario))


# In[ ]:


#este ejercicio fue un tanto fácil para mí porque estoy acostumbrado a usar Py para esto
#debido que en mi carrera lo usé mucho para realizar ecuaciones y graficar.
#Sin embargo, tuve que buscar las especificaciones de la librería Numpy porque no me
#acordaba como referenciar las operaciones como seno, coseno, logaritmo en 
#esta librería, la razón es que utilizaba google Collab donde las operaciones solo
#se escriben así, sin np.


# In[ ]:


#B La función dos graficara con matplotlib el resultado de función anterior y la mostrará en pantalla. Recuerden poner los títulos ejes y demás configuraciones de las gráficas para que queden de la mejor manera posible.
def funcion_b(funcion=funcion,a=a,b=b):
    x=np.arange(a,b+1)
    if funcion == 'coseno':
        y = np.cos(x)
        plt.plot(x, y)
        plt.title('Gráfico de funcion coseno(x)')
        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.show()
        
    elif funcion == 'seno':
        y=np.sin(x)
        print (y)
        plt.plot(x, y)
        plt.title('Gráfico de funcion seno(x)')
        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.show()
      
    elif funcion == 'tangente':
        y = np.tan(x)
        print (y)
        plt.plot(x, y)
        plt.title('Gráfico de funcion tangente(x)')
        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.show()
        
    elif funcion == 'exponencial':
        y = np.e**(x)
        print (y)
        plt.plot(x, y)
        plt.title('Gráfico de funcion exponencial')
        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.show()
    elif funcion == 'logaritmo':
        y = np.log(x)
        print (y)
        plt.plot(x, y)
        plt.title('Gráfico de funcion logaritmo')
        plt.xlabel('Eje x')
        plt.ylabel('Eje y')
        plt.show()


# In[ ]:


##Otro problema que tuve fue con el dominio, específicamente en el límite superior,
#pues Py es raro al no tomar el ultimo valor del arange, por eso lo tuve que “compensar”
#sumando una unidad
#El orden de la lógica también fue un tema a tratar porque el problema estaba separado
#en incisos y el A pide solo valores y el B las gráficas, por lo que tuve que separar los if


# In[ ]:


#Ejercicio 2
#Escribir un programa para ver los beneficios de una empresa en un periodo de años.
#El programa debe cumplir los siguientes requisitos:


# In[ ]:


#A. El programa tiene que preguntar al usuario por un año inicial y otro final, y después preguntar por los ingresos y egresos de cada año desde el año inicial hasta el año final.
#Debe garantizar que por lo menos haya 5 años entre el año inicial y el final.
import pandas as pd
import numpy as np

print("beneficios de la empresa en un periodo de al menos 5 años")
year1=int(input(("ingresa el año inicial del analisis: ")))
year2=int(input("ingresa el año final del analisis: "))
contador=True
while contador:
    if (year2-year1)>=5:
        contador=False
    else:
        print("lo siento, debe haber al menos 5 años de diferencia para el analisis")
        year1=int(input(("ingresa el año inicial del analisis: ")))
        year2=int(input("ingresa el año final del analisis: "))
diccionario={'año':[], 'ingresos':[], 'egresos':[]}


# In[ ]:


#Para este problema, pensé que iba a tardarme más porque tuve bastantes problemas en la
#otra tarea al usar lista y tener que moverlas para sincronizar columnas y renglones, sin
#embargo, mi ventaja aquí es que ya sabía más como utilizar diccionarios que son muy 
#convenientes y prácticos al quererlos mostrar con Pandas y al realizar operaciones 
#matemáticas con Numpy.


# In[ ]:


#B. Con los datos introducidos se deben crear un dataframe, con las columnas fecha, ingresos y egresos.
for i in range ((year2-year1)+1):
    year=year1+i
    diccionario['año'].append((year))
    diccionario['ingresos'].append(float(input(f'ingresa los ingresos del año {year}: ')))
    diccionario['egresos'].append(float(input(f'ingresa los ingresos del año {year}: ')))
print('inciso B')
print(pd.DataFrame(diccionario))


# In[ ]:


#Para este problema, pensé que iba a tardarme más porque tuve bastantes problemas en la
#otra tarea al usar lista y tener que moverlas para sincronizar columnas y renglones, sin
#embargo, mi ventaja aquí es que ya sabía más como utilizar diccionarios que son muy 
#convenientes y prácticos al quererlos mostrar con Pandas y al realizar operaciones 
#matemáticas con Numpy. Aqui usé un for para navegar entre renglones


# In[ ]:


#C. El programa debe generar otra columna con el beneficio de cada año (ingresos menos egresos) y mostrarla por pantalla.

nuevo_diccionarioc={'año':[], 'ingresos':[], 'egresos':[], 'beneficio':[]}
lista_ingresos=np.array(list(diccionario['ingresos']))
lista_egresos=np.array(list(diccionario['egresos']))
lista_beneficio=lista_ingresos-lista_egresos
for i in range (len(list(lista_ingresos))):
    nuevo_diccionarioc['año'].append(diccionario['año'][i])
    nuevo_diccionarioc['ingresos'].append(diccionario['ingresos'][i])
    nuevo_diccionarioc['egresos'].append(diccionario['egresos'][i])
    nuevo_diccionarioc['beneficio'].append((list(lista_beneficio))[i])
print('inciso c')
print(pd.DataFrame(nuevo_diccionarioc))


# In[ ]:


#En la anterior tarea se me complicó mucho juntar listas
#para hacer las tablas, pero con los diccionarios fue sumamente fácil. Mi único problema
#aquí fue el de hacer doble indexación dentro de los diccionarios para añadir datos, como
#en nuevo_diccionariod['egresos'].append(diccionario['egresos'][i]), pero con prueba
#y error lo logré. 


# In[ ]:


#D. El programa debe crear otra columna llamada ganancia la cuál indique para cada año si ha habido beneficios o no de manera booleana y mostrarla por pantalla.
#inciso D
nuevo_diccionariod={'año':[], 'ingresos':[], 'egresos':[], 'beneficio':[], 'hay_beneficio?':[]}
lista_ingresos=np.array(list(diccionario['ingresos']))
lista_egresos=np.array(list(diccionario['egresos']))

for i in range (len(list(lista_ingresos))):
    nuevo_diccionariod['año'].append(diccionario['año'][i])
    nuevo_diccionariod['ingresos'].append(diccionario['ingresos'][i])
    nuevo_diccionariod['egresos'].append(diccionario['egresos'][i])
    nuevo_diccionariod['beneficio'].append(nuevo_diccionarioc['beneficio'][i])
    if nuevo_diccionarioc['beneficio'][i]>0:
        nuevo_diccionariod['hay_beneficio?'].append(True)
    else:
        nuevo_diccionariod['hay_beneficio?'].append(False)
print('inciso d')
print(pd.DataFrame(nuevo_diccionariod))



# In[ ]:


#En la anterior tarea se me complicó mucho juntar listas
#para hacer las tablas, pero con los diccionarios fue sumamente fácil. Mi único problema
#aquí fue el de hacer doble indexación dentro de los diccionarios para añadir datos, como
#en nuevo_diccionariod['egresos'].append(diccionario['egresos'][i]), pero con prueba
#y error lo logré. 


# In[ ]:


#E. Finalmente el programa debe mostrar por pantalla la lista de los años con pérdidas.
#inciso E
lista_perdidas=[]
for i in range (len(list(lista_ingresos))):
    year=year1+i
    if nuevo_diccionariod['hay_beneficio?'][i]==False:
        lista_perdidas.append(year)
    else:
      pass
print('inciso e')
print(f'la lista de años con perdidas es la siguiente {lista_perdidas}')


# In[ ]:


#En la anterior tarea se me complicó mucho juntar listas
#para hacer las tablas, pero con los diccionarios fue sumamente fácil. Mi único problema
#aquí fue el de hacer doble indexación dentro de los diccionarios para añadir datos, como
#en nuevo_diccionariod['egresos'].append(diccionario['egresos'][i]), pero con prueba
#y error lo logré. 


# In[ ]:


#Ejercicio 3
#El fichero horas-trabajo.csv contiene el número de horas mensuales trabajadas por los empleados de una empresa durante el primer cuatrimestre. Crear un programa que realice las siguientes operaciones utilizando la librería Pandas:


# In[ ]:


#A. Crea una columna con el número total de horas trabajadas para cada operador.
import pandas as pd
import numpy as np
df=pd.read_csv('horas-trabajo.csv', index_col=0)

#para los valores nulos NaN considero valor fijo de 0, inplace para cambios en el mismo df
df.fillna(0.00, inplace=True)
#inciso A
total_horas=pd.DataFrame()
total_horas['total_horas']=df['Enero']+df['Febrero']+df['Marzo']+df['Abril']
print('inciso A')
print(total_horas)
#se añade axis=1 para alinear rows al concatenar dataframes
df1 = pd.concat([df, total_horas], axis=1)
print(df1)


# In[ ]:


#Como este problema es el primero donde uso más herramientas pandas, se me complicó un poco
#especialmente en la parte de aplicar las condiciones para mostrar los datos que las cumplan
#ya sea por columna o por renglón


# In[ ]:


#B. Muestra cual es el promedio de horas trabajadas en total en la empresa durante el mes Marzo
#Inciso B
print(f'el promedio de la columna de hrs trabajadas en Marzo es {df["Marzo"].mean()} hrs')


# In[ ]:


#Como este problema es el primero donde uso más herramientas pandas, se me complicó un poco
#especialmente en la parte de aplicar las condiciones para mostrar los datos que las cumplan
#ya sea por columna o por renglón


# In[ ]:


#C. Muestra cuántos operadores hay por cada departamento de la empresa.
#Inciso C
print('Tabla que contabiliza la contidad de empleados por departamento')
print(df.groupby('Departamento')['Enero'].nunique())
print('la cantidad de empleados en Marketing es de', df['Departamento'].str.contains('Marketing').value_counts()[True])
print('la cantidad de empleados en IT es de', df['Departamento'].str.contains('IT').value_counts()[True])
print('la cantidad de empleados en Proveedores es de', df['Departamento'].str.contains("Proveedores").value_counts()[True])
print('la cantidad de empleados en Ventas es de', df['Departamento'].str.contains('Ventas').value_counts()[True])


# In[ ]:


#pero después de este problema puedo decir que usar
#pandas es mucho más cómodo que usar la librería csv pues es muy intuitiva y de lógica
#fácil de entender. Otro gran problema que tuve fue en el inciso final, donde pide la condición 
#de detectar que empleados trabajaron al menos una hr en cada mes. Para esto yo ya 
#había cambiado los valores NaN por 0 para evitar problemas en las sumas o lecturas
#de anteriores incisos. En este inciso lo que hice fue emplear una función lambda al
#usar un dataframe, dentro del lambda puse unas condiciones ligadas y lo malo es que
#el dataframe después de este proceso lógico contenía únicamente una columna booleana
#la cual tiene comandos u operaciones un tanto raras, para poder contar los True de mi 
#dataframe tuve que buscar en Internet una metodología para hacerlo. 


# In[ ]:


#D. Muestra el número de empleados que han trabajado todos los meses, es decir, que tienen un número de horas todos los meses del cuatrimestre.
#Inciso D
registro=df.apply(lambda x: x['Enero'] > 0 and x['Febrero'] > 0 and x['Marzo'] > 0 and x['Abril'] > 0, axis=1)
print(registro)
#uso con Numpy
#print(f'el numero de trabajadores con hrs trabajadas todos los meses es: {np.count_nonzero(registro)}')
suma=0
for i in range(len(registro)):
    if registro[i]==True:
        suma=1+suma
    else:
        pass
print(suma)
print(f'el numero de trabajadores con hrs trabajadas todos los meses es: {suma}')


# In[ ]:


#Me costó mucho
#trabajo completar este último inciso, pero al final me di cuenta que el df al ser una lista, 
#pues puede usarse un for para analizar cada elemento del df (como en pasadas tareas). Otra cosa importante 
#es que dentro de lambda si se reconoce el and, pero si es dentro de un [] en pd se usa el &


# In[ ]:


#Ejercicio 4
#Crear un programa utilizando la librería Pandas y Matplotlib que realice lo siguiente:



# In[ ]:


#A. Crear el siguiente DataFrame indexado: NO MOSTRADO AQUI LOL
import pandas as pd
import matplotlib.pyplot as plt
#Inciso A
df=pd.DataFrame({"Dia":["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"], "Calorias":[420,380,390, 490, 300], "Tiempo":[60, 40, 75, 55, 45]})
print("Inciso A")
print(df)




# In[ ]:


#Este problema tuvo un montón de incisos que obstaculizaron un poco su realizado, pero que #fomenta la práctica de pandas. El inciso A fue fácil al hacer desde 0 el dataframe con #diccionarios como en pasados problemas


# In[ ]:


#B. Calcular la media, mediana y desviación típica de ambas columnas.
#Inciso B
suma_calorias=df["Calorias"].sum()
suma_tiempo=df["Tiempo"].sum()
promedio_calorias=df["Calorias"].mean()
promedio_tiempo=df["Tiempo"].mean()
desv_est_calorias=df["Calorias"].std()
desv_est_tiempo=df["Tiempo"].std()
print("Inciso B")
print(f'la suma de columna Calorias es de {suma_calorias}, para la columna Tiempo es de {suma_tiempo}')
print(f'el promedio de columna Calorias es de {promedio_calorias}, para la columna Tiempo es de {promedio_tiempo}')
print(f'la desviacion estandar muestral de columna Calorias es de {desv_est_calorias}, para la columna Tiempo es de {desv_est_tiempo}')


# In[ ]:


#el inciso B fue más sobre aprender de operaciones #matemáticas sobre dataframes, vistas en el video de 30 min


# In[ ]:


#C. Añadir otra columna booleana al DataFrame para ver si se ha cumplido el reto de quemar más de 400 calorías por hora. La nueva columna debe generarse aplicando una fórmula a las otras columnas. 
#Inciso C
cumplimiento=df.apply(lambda x: x['Calorias'] > (400/(x["Tiempo"]/60)), axis=1)
dfc=df
dfc["Cumplió?"]=cumplimiento
print("Inciso C")
print(dfc)


# In[ ]:


#sin embargo en el C sí tuve que consultar internet y aprender #a cómo realizar funciones lambda para dataframes, traté de hacer ciclos for aprovechando #que los df son como listas, pero involucran más línea de código y más errores en el análisis de #tipo de dato, descubrí que es difícil usar for con dfs al tener booleanos o str, lo mejor y más #práctico es usar funciones lambda, además aprendí más a usar el axis=1 haciendo referencia #al enfoque en los renglones del df. 


# In[ ]:


#D. Filtrar el DataFrame y devolver otro DataFrame con las filas pares que cumplan que el número de calorías es mayor de 400.
#inciso D
df_pares = df.iloc[::2]
dfd = df_pares[df_pares['Calorias'] > 400]
print("Inciso D")
print(dfd)


# In[ ]:


#Con este ejemplo reconocí lo intuitivo que es trabajar con #pandas, sobre todo al hacer condicionales. Más tarde, tuve que buscar en línea como #seleccionar renglones pares (uso de [::2]) porque de otra forma no me salía.


# In[ ]:


#E. Añadir otra columna con los porcentajes de días que se ha conseguido el reto y los que no.
#Inciso  E

suma = 0
conteo=[]
def contar(row):
    if row['Calorias'] > (400 / (row['Tiempo'] / 60)):
        global suma
        suma =suma+1
  
    conteo.append(suma)
dfc.apply(contar, axis=1)

dfc['Conteo'] = conteo
dfc['Porcentaje_cumplido'] = 0
for i in range(len(conteo)):
    dfc.loc[i, 'Porcentaje_cumplido'] = dfc.loc[i, 'Conteo'] / (i+1) * 100
    print(dfc.loc[i, 'Conteo'] / (i+1))
dfc["Porcentaje_no_cumplido"]=(dfc['Porcentaje_cumplido']-100)*-1
print("Inciso E")
print(dfc)


# In[ ]:


#Definitivamente #el inciso más pesado y difícil fue el E porque al inicio no entendí lo que se pedía, pero luego #pensé que quería un análisis por renglón para ir contando y dividiendo de acuerdo al #resultado de True o False relacionado con el reto del problema. Yo entendí que para cada #renglón teníamos que sumar si el número de True´s iba creciendo y dividirlo de acuerdo al #número del renglón analizado para llevar una “cuenta en tiempo real” de los éxitos o fracasos #del reto. Para ello tuve que declarar una función contadora y utilizarla en cada renglón del df #de interés, tal vez la operación fue fácil, pero el pensar la metodología me llevó al menos 40 #min. 


# In[ ]:


#F. Crear un gráfico donde se  muestre la progresión de las calorías y tiempo durante la semana.
#Inciso F
fig, ax = plt.subplots()
ax.plot(dfc['Dia'], dfc['Calorias'], label='Calorias')
ax.plot(dfc['Dia'], dfc['Tiempo'], label='Tiempo', color="red")
ax.set_title('Progresión de Calorias y Tiempo durante la semana')
ax.set_xlabel('Días de la semana')
ax.set_ylabel('Cantidad')
ax.legend()
print("Inciso F")
plt.show()


# In[ ]:


#Al final, la gráfica del inciso F fue mucho más fácil porque de hecho se tenían que #graficar todos los elementos del df, solo que decidí corregir el color de las líneas para evitar #tener un gráfico en amarillo. 


# In[ ]:


#Ejercicio 5
#El fichero coches.csv contiene información sobre los modelos de coches vendidos en USA durante un determinado año. Se pide:


# In[ ]:


#A.Crear un DataFrame a partir del fichero anterior.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Inciso A
df=pd.read_csv("coches.csv")
print("Inciso A")
print(df)


# In[ ]:


#Con la práctica de los demás ejercicios y con el video de cómo usar Pd en Py pude hacer los #primeros 4 incisos en 20 minutos, realmente es un uso muy básico del pd.


# In[ ]:


#B. Eliminar las filas con valores desconocidos y mostrar el número de filas del DataFrame resultante.
#Inciso B
dfb=df.dropna()
print("Inciso B")
numero_filas_sin_desconocidos=len(dfb)
print(f'el numero de filas sin valores desconocidos es de {numero_filas_sin_desconocidos}')


# In[ ]:


#Solo quiero #destacar el uso tan fácil de dropna() pues al principio quería jamar emplearlo por su poder de #eliminación, pero mientras uno sea cuidadoso al manejar variables backup del df original, uno #puede disfrutar de su aplicación tan directa y cómoda. Por cierto, en estas instancias decidí #sustituir NaN por 0 para el futuro cálculo de la grafica precio – potencia.


# In[ ]:


#C. Crear una columna con el precio en euros (cambio 1$ = 0.94€)
#Inciso C
#hay NaN en la columna de Precio, por eso uso df.fillna
df.fillna(0.00, inplace=True)
dfc=df
dfc["Precio_Euros"]=dfc["Precio"]*0.94 #El Precio original está en $
print("Inciso C")
print(dfc)



# In[ ]:


#aqui solo un producto directo de un df por 0.94 e incluir la nueva columna 


# In[ ]:


#D. Mostrar las 10 últimas filas del DataFrame.
#Inciso D
dfd=df.tail(10)
print("Inciso D")
print(dfd)



# In[ ]:


#lol solo tail(10)


# In[ ]:


#E. Mostrar el número de marcas de coches que contiene el DataFrame.
#Inciso E
dfe=df.groupby("Marca").first()
cantidad_marcas=len(dfe)
print("Inciso E")
print(f'La cantidad de marcas en la columna "Marca" es de {cantidad_marcas}')


# In[ ]:


#No obstante, el #problema llegó en el incisio E al querer usar ese groupby(), pues como vimos en clase, ese #groupby no puede ir solo, siempre debe llevar consigo un método u otra operación; usé #groupby sin dudarlo para obtener todas las marcas del df.


# In[ ]:


#F. Mostrar el número de modelos de cada marca que hay en el DataFrame, de mayor a menor frecuencia.
#Inciso F
dff = df.groupby("Marca")["Modelo"].nunique().sort_values(ascending=False)
#contar es para el futuro inciso I
contar=dff.sum()
print("Inciso F")
print(dff)


# In[ ]:


#Para el inciso F tuve muchos #problemas para conceptualizar esta línea “dff = #df.groupby("Marca")["Modelo"].nunique().sort_values(ascending=False)” pues nuevamente #se tiene la necesidad de usar groupby, sin embargo se le adicionan otros métodos como el . #sort y el nunique que nunca los había empleado antes, esta línea de código la obtuve después #de leer en la pagina de Pd. Quiero solo decir que el inciso F y H son muy parecidos solo que #uno implica una operación matemática y el otro el orden de los datos


# In[ ]:


#G Mostrar cuál es la marca y el modelo del coche más caro.
#Inciso G
dfg=df.loc[df['Precio'].idxmax(), ['Marca', 'Modelo']]
print("Inciso G")
print("La marca y el modelo del auto mas caro son: ")
print(dfg)


# In[ ]:


#Inciso G fue algo #complicado también porque en (dfg=df.loc[df['Precio'].idxmax(), ['Marca', 'Modelo']]) yo solo #ponía .max() y no me ejecutaba el programa por error de identificación de numero (me salía #un int), fue hasta que vi en línea que ese método idxmax se debe de usar al emplear .loc[], la #otra parte de añadir la columna de Marca y Modelo es sumamente intuitiva. 


# In[ ]:


#H. Mostrar el precio medio en euros de los coches agrupando por marca y ordenando de menor a mayor precio.
#Inciso H
dfh = dfc.groupby("Marca")["Precio_Euros"].mean().sort_values(ascending=True)
print("Inciso H")
print(dfh)


# In[ ]:


#Para el inciso F tuve muchos #problemas para conceptualizar esta línea “dff = #df.groupby("Marca")["Modelo"].nunique().sort_values(ascending=False)” pues nuevamente #se tiene la necesidad de usar groupby, sin embargo se le adicionan otros métodos como el . #sort y el nunique que nunca los había empleado antes, esta línea de código la obtuve después #de leer en la pagina de Pd. Quiero solo decir que el inciso F y H son muy parecidos solo que #uno implica una operación matemática y el otro el orden de los datos


# In[ ]:


#I. Gráfica el diagrama de barras del porcentaje de modelos de cada marca.
#Inciso I
#Como ya sabemos cuantos modelos hay por marca, lo cual se hizo en F, por eso agarro contar y dff
#porcentaje=(cantidad de modelos por marca)/(cantidad de modelos, sin repetirse total)*100
fig1 = plt.figure()
(dff/contar*100).plot(kind="bar", title="Porcentaje de modelos por marca", 
                      xlabel="Marca de autos", ylabel="Porcentaje de modelos (%)")


# In[ ]:


#Al final, para #inciso I y J hacer las graficas fue muy sencillo por la experiencia previa de la tarea, sin #embargo, me salían ambas graficas fucionadas, para separarlas y que se vieran mejor usé el #método fig1 y fig2 con plt.figure(). Cabe resaltar que estaba usando “import matplotlib as plt” #pero no podía ejecutar el código por error con los plt´s. busqué en línea y vi que en Anaconda #se debe usar “import matplotlib.pyplot as plt”


# In[ ]:


#J. Gráfica el diagrama de dispersión de la potencia y el precio.
#Inciso J
#De este inciso solo tomo el df sin valores NaN, esa es la razon del porque hay potencia 0
fig2 = plt.figure()
plt.scatter(df["Potencia"], df["Precio"])
plt.xlabel('Gráfico Precio vs Potencia')
plt.xlabel('Potencia')
plt.ylabel('Precio')
plt.show()


# In[ ]:


#Al final, para #inciso I y J hacer las graficas fue muy sencillo por la experiencia previa de la tarea, sin #embargo, me salían ambas graficas fucionadas, para separarlas y que se vieran mejor usé el #método fig1 y fig2 con plt.figure(). Cabe resaltar que estaba usando “import matplotlib as plt” #pero no podía ejecutar el código por error con los plt´s. busqué en línea y vi que en Anaconda #se debe usar “import matplotlib.pyplot as plt”


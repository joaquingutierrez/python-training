# Restricción Vehicular

La ciudad de Babilonia tiene una alta congestión de vehículos circulando por sus calles.
Las autoridades han decidido aplicar restricción vehicular para descongestionar la
ciudad en base a las patentes de los vehículos.  
La patente de un vehículo es un string de cuatro letras y dos dígitos, y la restricción
depende sólo del penúltimo dígito. Por ejemplo, para la patente GEEA78, el dígito 7 es
el utilizado para evaluar la restricción.

La restricción vehicular de los días hábiles de la semana se encuentra ingresada en el
diccionario dígitos, cuyas llaves son los días de la semana, y cuyos valores son tuplas de
cuatro enteros que representan los dígitos con restricción de ese día.  
* Implemente la función estaConRestriccion(digitos,dia, patente), que indique si el
vehículo está o no con restricción.
* Implemente la función diasConRestriccion(digitos,patente), que retorne la lista
de los días en que el vehículo no puede circular.
* Implemente la función diasSinRestriccion(digitos,patente), que retorne el
conjunto de los días en que el vehículo sí puede circular.

## Ejemplo:
digitos = {'lunes': (3, 4, 5, 6), 'martes': (7, 8, 9, 0),...,'miercoles': (1, 2, 3, 4), 'jueves':
(5, 6, 7, 8), ... , 'viernes': (9, 0, 1, 2)}

estaConRestriccion(digitos, 'lunes', 'BBDT35') ---> True  
diasConRestriccion(digitos, 'BBDT35') ---> ['lunes', 'miercoles']  
diasSinRestriccion(digitos, 'BBDT35') ---> set(['jueves', 'martes', 'viernes'])
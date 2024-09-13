# Encontrar Sospechoso mediante DNA
Debido a la gran cantidad de crímenes y casos sin resolver, la policía local ha decidido 
implementar su propio sistema de reconocimiento de sospechosos con la técnica basada 
en el uso del DNA.  
Para esto la policía mantiene dos listas de información; la primera contiene el nombre 
de las personas registradas en la región (nombre y apellido), la otra, un cromosoma 
representativo del DNA de cada una de esas personas. 

Por simplicidad, un cromosoma se considera como una cadena de 0 (ceros) y 1 (unos), 
de largo 20. 

El método para determinar el sospechoso, es el siguiente: 

* Se obtiene una muestra del cromosoma del autor del delito (20 caracteres) 
* Se busca en la lista de cromosomas, aquel cromosoma que es más parecido a la muestra. El más parecido se define como el cromosoma que tiene más genes (caracteres) iguales a la muestra. 
* Al terminar la búsqueda, se muestra el nombre de la persona cuyo cromosoma es sospechoso, con el porcentaje de parentesco.

La información inicial del programa se debe ingresar directamente en el código, es 
decir, nombres y cromosomas, en cambio la secuencia encontrada en la escena del 
crimen, debe ser ingresada por el usuario. 

Desarrolle un programa que lleve a cabo la búsqueda descrita a partir de una muestra de 
entrada. 

## Ejemplo: 
Consideremos, personas como Pedro, Juan y Diego. Sus secuencias serán 
* 00000101010101010101 
* 00101010101101110111 
* 00100010010000001001 

Ingrese secuencia: 01010101000011001100  
El culpable es Pedro con un parentesco de 60%
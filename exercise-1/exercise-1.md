# Mensajes Cifrados

El agente 0069 lleva años utilizando un método de codificación de mensajes secretos. Si 
X es el mensaje original, éste se codifica en dos etapas:

1. X se transforma en X' reemplazando cada sucesión de caracteres consecutivos 
que no sean vocales por su imagen especular. 
2. X' se transforma en la sucesión de caracteres X'' obtenida al ir tomando sucesivamente:
el primer carácter de X', luego el último, luego el segundo, luego el penúltimo, etc.

Por ejemplo, para X = "Bond, James Bond",  
resultan: X' = "BoJ ,dnameB sodn"  
y  
X'' = "BnodJo s, dBneam" 

Lo que el pobre agente 0069 no sabe es que el señor Fon Noiman ha analizado algunos 
mensajes cifrados y ha dado con el mecanismo que está utilizando. Lo único que le 
queda a Fon Noiman es hacer el programa que, dado un mensaje cifrado, lo descifre. 

## Entrada del Programa 
Un mensaje cifrado según el algoritmo anterior. El agente 0069 utiliza un teclado inglés, 
por lo que ninguna vocal tendrá tilde y no tiene ñ. 

## Salida del Programa 
Se mostrará el mensaje cifrado leído de la entrada y a continuación aparecerá "=>"entre 
dos espacios y el mensaje original descifrado. 

### Entrada de ejemplo 
#### Ejemplos:  
BnodJo s, dBneam  
aueoi  
E. .n.ualn cnhuag aMda rle  
Aauirnedleiua nBo  

#### Salida de ejemplo 
BnodJo s, dBneam => Bond, James Bond  
aueoi => aeiou  
E. .n.ualn cnhuag aMda rle => En un lugar de la Mancha...  
Aauirnedleiua nBo => Aureliano Buendia 
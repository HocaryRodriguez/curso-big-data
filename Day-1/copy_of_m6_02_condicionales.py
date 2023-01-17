# -*- coding: utf-8 -*-


# Condicionales

En esta sección veremos la sentencia condicional `if` y las distintas variantes que puede asumir, pero antes de eso introduciremos algunas cuestiones generales de escritura de código.

### Operadores de comparación

A continuación se muestra la tabla de los operadores de comparación en Python:

Operador | Símbolo
--- | ---
Igualdad | `==`
Desigualdad | `!=`
Menor que | `<`
Menor o igual que | `<=`
Mayor que | `>`
Mayor o igual que | `>=`

Estos operadores devuelven valores booleanos `True` o `False`. Veamos un ejemplo:
"""

x == 5

x == 7

5 < x

x < 10

"""Podemos escribir condiciones más complejas usando los operadores lógicos `and`, `or` y `not`:"""

(5 < x) or (x > 10)    # se recomienda el uso de paréntesis

(5 < x) and (not (x > 10))

(5 < x) and (x < 10)

"""Esta última comparación también se pueden escribir en Python de la siguiente forma:"""

5 < x < 10

"""## ¿Qué es cierto?

Python considera `False` a todo lo que está en la siguiente tabla:

Elemento | Representación
--- | ---
Booleano | `False`
Nulo | `None`
Cero entero | `0`
Cero flotante | `0.0`
Cadena vacía | `''`
Tupla vacía | `()`
Diccionario vacío | `{}`
Conjunto vacío | `set()`

✅ Cualquier otra cosa se considera `True`

Ejemplo de verificación de lista vacía:
"""

lista = []

if lista:
    print('Hay algo en la lista')
else:
    print('La lista está vacía')

"""## Ejercicios

### Ejercicio 1

Simula el siguiente diagrama de flujo de personajes Marvel utilizando sentencias condicionales:

!

# Escriba aquí su solución
if can_fly == True: 
  if is_human == True:
   if has_mask== True:
      print("Ironman")
if can_fly and is_human:
  print("Captain Marvel")
if can_fly and has_mask:
  print("Ronan Accuser")
if can_fly:
  print("Vision")
if is_human and has_mask:
  print("spiderman")
if is_human:
  print("Hulk")
if has_mask:
  print("Black Bolt")
else:
  print("Thanos")

#Si introducimos:
can_fly = True
is_human = False
has_mask = False
#Debe devolver: "Vision"

"""### Ejercicio 2

Dada una variable `year` con un valor entero, comprueba si dicho año es bisiesto o no.

*   Pista: Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100. O si es divisible entre 400.

*    Puedes hacer la comprobación en [esta lista de años bisiestos](https://kalender-365.de/leap-years.php).
"""

# Escriba aquí su solución
anyo = 2020


anyo ==

"""### Ejercicio 3



#Input:
sentence = 'Ella te da detalle'
# Escriba aquí su solución
def is_palindrome(sentence):
    
    sentence = sentence.lower()
   
    sentence = ''.join(e for e in sentence if e.isalnum())
   
    sentence_reverse = sentence[::-1]
   
    if sentence == sentence_reverse:
        return True
    else:
        return False

sentence = 'Ella te da detalle'
print(is_palindrome(sentence))
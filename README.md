# 2021-S1-Laboratorio-8

El laboratorio consiste en una serie de ejercicios para practicar la resolución de problemas usando el método visto en la clase de **Introducción a la Programación**, listas y matrices.

El laboratorio es **individual**, deberán subir un archivo con el nombre **laboratorio8.py**.  Se entrega el **viernes 28 de mayo hasta las 10 pm**. Para estas funciones haremos del uso del **While y For**


## encontrarNumerosDivisibles(matriz, num)

Escriba una función **encontrarNumerosDivisibles(matriz, num)**. Esta función recibe una **matriz** de tamaño mxn, consiste en hacer el recorrido columna por columna, si en dicho recorrido se encuentra un número que es divisible por el parámetro **num** **NO** modificar dicho número, de lo contrario sustituirlo por **CERO**. La función debe comportarse de la siguiente manera:

```python
m = [[1,5,3,7],[2,43,6,8],[11,23,3,4],[7,8,9,10]]

>>>encontrarNumerosDivisibles(m, 2) 
[[0,0,0,],[2,0,6,8],[0,0,0,4],[0,8,0,10]]
```

## convertirBinarioDecimal(num)

Escriba una función **convertirBinarioDecimal(num)** que reciba un parámetro denominado “**num**”, el cual es una representación **binaria** y deberá **convertir** a su representación con **base a 10**. La función debe comportarse de la siguiente manera:
```python
>>> convertirBinarioDecimal (1100)
12
>>> convertirBinarioDecimal (1108)
‘No corresponde a una representación binaria’
>>> convertirBinarioDecimal (0)
0
```

## convertirDecimalHex (num)

Escriba una función **convertirDecimalHex(num)** que reciba un parámetro denominado “**num**”, el cual es una representación en **base 10** y deberá **convertir** a su representación con **base a 16**. La función debe comportarse de la siguiente manera:

```python
>>> convertirDecimalHex (16)
10
>>> convertirDecimalHex (31)
1F
>>> convertirDecimalHex (7000)
1B58
```

import laboratorio8.py;
import pytest;

m = [[1,5,3,7],[2,43,6,8],[11,23,3,4],[7,8,9,10]]
n = [[1,5,7],[2,43,6,8],[11,23,3,4],[7,8,9,10]]

#Pruebas para encontrarNumerosDivisibles
def test_encontrarNumerosDivisibles_1():
    assert laboratorio8.encontrarNumerosDivisibles(n, 2) == "Error: existen vectores de diferente tamaño"

def test_encontrarNumerosDivisibles_2():
    assert laboratorio8.encontrarNumerosDivisibles(m, 2) == [[0,0,0,],[2,0,6,8],[0,0,0,4],[0,8,0,10]]
    
#Pruebas para convertirBinarioDecimal    
def test_convertirBinarioDecimal_1():
    assert laboratorio8.convertirBinarioDecimal(1100) == 10
    
def test_convertirBinarioDecimal_2():
    assert laboratorio8.convertirBinarioDecimal(1108) ==  'Error: No corresponde a una representación binaria'
    
def test_convertirBinarioDecimal_3():
    assert laboratorio8.convertirBinarioDecimal(0) == 0
    
#Pruebas para convertirDecimalHex
def test_convertirDecimalHex_1():
    assert laboratorio8.convertirDecimalHex (16) == '10'
    
def test_convertirDecimalHex_2():
    assert laboratorio8.convertirDecimalHex (31) == '1F'
    
def test_convertirDecimalHex_3():
    assert laboratorio8.convertirDecimalHex (16) == '1B58'    

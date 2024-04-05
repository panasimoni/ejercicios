import pytest 
from prueba import Calculadora


# Pruebas unitaria
def test_resta_regresion(calculadora):
    assert calculadora.resta(0, 0) == 0


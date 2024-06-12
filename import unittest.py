import unittest
def PromedioDeConjunto(conjunto):
    suma = 0
    cantidad = 0
    for numero in conjunto:
        suma += numero
        cantidad += 1
    promedio = suma / cantidad
    return promedio


class TestPromedio(unittest.TestCase):
    def testPromedioConjunto(self):
        arregloNum= [5, 7, 12]
        resultado = PromedioDeConjunto(arregloNum)
        promedioEsperado = 8
        self.assertEqual(resultado, promedioEsperado)


if __name__ == '__main__':
    unittest.main()

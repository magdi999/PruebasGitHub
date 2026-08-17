import unittest
from calculadoraPy import sumar, restar, multiplicar, dividir, potencia


class TestCalculadora(unittest.TestCase):

    # Pruebas para sumar
    def test_sumar_positivos(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_sumar_con_negativo(self):
        self.assertEqual(sumar(-1, 1), 0)

    def test_sumar_ceros(self):
        self.assertEqual(sumar(0, 0), 0)

    def test_sumar_decimales(self):
        self.assertEqual(sumar(2.5, 1.5), 4.0)

    # Pruebas para restar
    def test_restar_positivos(self):
        self.assertEqual(restar(5, 2), 3)

    def test_restar_resultado_negativo(self):
        self.assertEqual(restar(2, 5), -3)

    def test_restar_ceros(self):
        self.assertEqual(restar(0, 0), 0)

    def test_restar_decimales(self):
        self.assertEqual(restar(5.5, 0.5), 5.0)

    # Pruebas para multiplicar
    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_multiplicar_con_negativo(self):
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_multiplicar_por_cero(self):
        self.assertEqual(multiplicar(0, 5), 0)

    def test_multiplicar_decimales(self):
        self.assertEqual(multiplicar(2.5, 2), 5.0)

    # Pruebas para dividir
    def test_dividir_exacta(self):
        self.assertEqual(dividir(10, 2), 5.0)

    def test_dividir_con_decimal(self):
        self.assertEqual(dividir(7, 2), 3.5)

    def test_dividir_con_negativo(self):
        self.assertEqual(dividir(-6, 3), -2.0)

    def test_dividir_cero_entre_numero(self):
        self.assertEqual(dividir(0, 5), 0.0)

    def test_dividir_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_dividir_cero_entre_cero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(0, 0)

    # Pruebas para potencia
    def test_potencia_normal(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_potencia_exponente_cero(self):
        self.assertEqual(potencia(5, 0), 1)

    def test_potencia_exponente_negativo(self):
        self.assertEqual(potencia(2, -1), 0.5)

    def test_potencia_base_cero(self):
        self.assertEqual(potencia(0, 5), 0)

    def test_potencia_de_10(self):
        self.assertEqual(potencia(10, 2), 100)


if __name__ == "__main__":
    unittest.main()
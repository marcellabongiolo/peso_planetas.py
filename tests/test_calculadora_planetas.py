import unittest

from calculadora_planetas import calcular_pesos


class TestCalculadoraPlanetas(unittest.TestCase):
    def test_calcula_peso_em_marte(self):
        resultados = calcular_pesos(60)
        self.assertAlmostEqual(resultados["Marte"], 22.8)

    def test_calcula_peso_na_terra(self):
        resultados = calcular_pesos(60)
        self.assertAlmostEqual(resultados["Terra"], 60.0)

    def test_rejeita_peso_zero(self):
        with self.assertRaises(ValueError):
            calcular_pesos(0)

    def test_rejeita_peso_negativo(self):
        with self.assertRaises(ValueError):
            calcular_pesos(-10)


if __name__ == "__main__":
    unittest.main()

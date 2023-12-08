import math
import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Pieczemy ciastka. Mamy do dyspozycji płaskie ciasto bazowe o powierzchni `area` z którego
chcemy wyciąć okrągłe kawałki o promieniach podanych w liście `small_cakes`, przy czym
w przypadku gdyby _geometrycznie_ nie dało się tego zrobić, ciasto możemy przeformować i znowu
rozpłaszczyć (zachowując powierzchnię). Proszę sprawdzić czy wystarczy nam ciasta na wycięcie wszystkich
`small_cakes`. 
"""

# funkcja sprawdza, czy można wyciąć wszystkie małe ciastka o zadanych promieniach z danego płaskiego ciasta bazowego o określonej powierzchni, przy założeniu, 
# że można je ułożyć na płasko bez zmiany ich całkowitej powierzchni.
def cut_cakes(area: float, small_cakes: list[float]) -> bool:
    required_area = sum(math.pi * radius**2 for radius in small_cakes)
    return required_area <= area
    pass


class TestEngine5(unittest.TestCase):

    def test_1(self):
        # powierzchnia jedynego small_cake to math.pi * 0.99**2 = 3.0791.. < 3.14
        self.assertEqual(cut_cakes(3.14, [0.99]), True)

    def test_2(self):
        # 10 small cakes, każdy o powierzchni math.pi
        self.assertEqual(cut_cakes(315, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), True)

    def test_3(self):
        self.assertEqual(cut_cakes(315, [1, 2, 3, 4, 5, 6]), True)

    def test_4(self):
        self.assertEqual(cut_cakes(315, [1, 2, 3, 4, 5, 6, 7]), False)

    def test_5(self):
        # duuże ciasta
        self.assertEqual(cut_cakes(10 ** 6, [10 ** 1, 10 ** 2, 10 ** 3]), False)


if __name__ == '__main__':
    unittest.main()
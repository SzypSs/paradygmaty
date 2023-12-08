import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Liczbę nazywamy "parzyście-piękną" jeśli każda z jej cyfr występuje w niej dokładnie dwa razy. 
Np. liczby 2121, 2211, 321123 są parzyście piękne, choć np. 121, 2222, 33441156 już nie. 
Napisać funkcję która sprawdzi, czy podana liczba `number` jest parzyście piękna. 

"""

# funkcja sprawdza, czy podana liczba jest "parzyście-piękną" zgodnie z opisanym warunkiem. funkcja sprawdza, czy każda cyfra w liczbie występuje dokładnie 2 razy i zwraca True,
# jeśli tak jest, oraz False w przeciwnym przypadku. Testy jednostkowe (unittest) zostały dostarczone, aby zweryfikować poprawność działania funkcji dla różnych przypadków.
def is_even_beautiful(number: int) -> int:
    number_str = str(number)    
    digit_count = {}
    for digit in number_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    for count in digit_count.values():
        if count != 2:
            return False

    return True
    pass


class TestEngine6(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_even_beautiful(2233), True)

    def test_2(self):
        self.assertEqual(is_even_beautiful(11), True)

    def test_3(self):
        self.assertEqual(is_even_beautiful(1212), True)

    def test_4(self):
        self.assertEqual(is_even_beautiful(1221), True)

    def test_5(self):
        self.assertEqual(is_even_beautiful(121), False)

    def test_6(self):
        self.assertEqual(is_even_beautiful(33441156), False)

    def test_7(self):
        self.assertEqual(is_even_beautiful(2222), False)


if __name__ == '__main__':
    unittest.main()
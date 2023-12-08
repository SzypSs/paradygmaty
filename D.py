import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Mamy podany napis `line`, który zawiera cyfry i litery. Wybieramy cyfry z tego napisu, i 
układamy z nich liczbę całkowitą. Funkcja ma podać jaką największą liczbę całkowitą można ułożyć. 
"""

# funkcja ma na celu znalezienie największej liczby całkowitej, która może zostać utworzona poprzez ułożenie cyfr z danego napisu line. 
def find_greatest_number(line: str) -> int:
    digits = [digit for digit in line if digit.isdigit()]
    print('przed sortowaniem')
    print(digits)
    digits.sort(reverse=True)
    print('po sortowaniu')
    print(digits)
    return int("".join(digits))
    pass


class TestEngine4(unittest.TestCase):

    def test_1(self):
        self.assertEqual(find_greatest_number("abc123abc"), 321)

    def test_2(self):
        self.assertEqual(find_greatest_number("aeqf9adasde9awdadae0adaed9"), 9990)

    def test_3(self):
        self.assertEqual(find_greatest_number("12345678"), 87654321)

    def test_4(self):
        self.assertEqual(find_greatest_number("2233x"), 3322)



if __name__ == '__main__':
    unittest.main()
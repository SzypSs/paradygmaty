import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Drapieżnik morski poluje na ryby; z jego rewirze pojawiła się pewna grupa ryb; ich wielkości zadane są
listą `fishes`. Wiadomo, że drapieżnik może zjeść tylko ryby o wielkości >= min_size, i <= max_size. 
Funkcja powinna obliczyć na ile ryb z grupy drapieżnik może zapolować. 

"""

# definiuje funkcję o nazwie eat_small_fish, która przyjmuje trzy argumenty: fishes (lista liczb całkowitych reprezentująca wielkości ryb), 
# min_size (minimalna wielkość ryb, które drapieżnik może zjeść) i max_size (maksymalna wielkość ryb, które drapieżnik może zjeść). 
# Funkcja zwraca liczbę ryb z grupy, które spełniają warunek, że ich wielkość mieści się pomiędzy min_size a max_size a drapieznik moze na nie zapolowac.
def eat_small_fish(fishes: list[int], min_size: int, max_size: int) -> int:
    return sum(min_size <= fish_size <= max_size for fish_size in fishes)
    pass


class TestEngine1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(eat_small_fish([1, 2, 3, 4, 5], 2, 3), 2)

    def test_2(self):
        self.assertEqual(eat_small_fish([1, 1, 1, 2, 2], 2, 3), 2)

    def test_3(self):
        self.assertEqual(eat_small_fish([1, 10], 2, 3), 0)


if __name__ == '__main__':
    unittest.main()
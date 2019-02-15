## M2A07
# Fizbuzzer

""""Regras do fizz buzz:
Se posicao multipla de 3: fizz
Se posicao for multipla de 5: buzz
Se posicao for multipla de 3 e 5: fizzbuzz
Para qualquer outra posicao: numero
"""

from functools import partial
import unittest

multiple_of = lambda base, num: num % base == 0
multiple_of_5 = partial(multiple_of, 5)
multiple_of_3 = partial(multiple_of, 3)


def robot(pos):
    say = str(pos)
    if pos % 3 == 0 and pos % 5 == 0:
        say = 'fizzbuzz'
    elif multiple_of_5(pos):
        say = 'buzz'
    elif pos % 3 == 0:
        say = 'fizz'
    return say

class FizzbuzzTest(unittest.TestCase):
    def test_say_1_when_1(self):
        self.assertEqual(robot(1), '1')

    def test_say_2_when_2(self):
        self.assertEqual(robot(2), '2')

    def test_say_4_when_4(self):
        self.assertEqual(robot(4), '4')


    def test_say_fizz_when_3(self):
        self.assertEqual(robot(3), 'fizz')

    def test_say_fizz_when_6(self):
        self.assertEqual(robot(6), 'fizz')

    def test_say_fizz_when_9(self):
        self.assertEqual(robot(9), 'fizz')


    def test_say_buzz_when_5(self):
        self.assertEqual(robot(5), 'buzz')

    def test_say_buzz_when_10(self):
        self.assertEqual(robot(10), 'buzz')

    def test_say_buzz_when_20(self):
        self.assertEqual(robot(20), 'buzz')


    def test_say_fizzbuzz_when_15(self):
        self.assertEqual(robot(15), 'fizzbuzz')

    def test_say_fizzbuzz_when_30(self):
        self.assertEqual(robot(30), 'fizzbuzz')

    def test_say_fizzbuzz_when_45(self):
        self.assertEqual(robot(45), 'fizzbuzz')

if __name__ == '__main__':
    unittest.main()
"""
def assert_equal(result, expected):
    from sys import _getframe

    msg = 'fail: Line {} got {} expecting {}'

    if not result == expected:
        current = _getframe() # current pq estamos pegando o frame da funcao;
        caller = current.f_back # agora, sim pegando o caller da funcao
        line_no = caller.f_lineno

        print(msg.format(line_no, result, expected))


if __name__ == '__main__':
    assert_equal(robot(1), '1')
    assert_equal(robot(2), '2')
    assert_equal(robot(4), '4')

    assert_equal(robot(3), 'fizz')
    assert_equal(robot(6), 'fizz')
    assert_equal(robot(9), 'fizz')

    assert_equal(robot(5), 'buzz')
    assert_equal(robot(10), 'buzz')
    assert_equal(robot(20), 'buzz')

    assert_equal(robot(15), 'fizzbuzz')
    assert_equal(robot(30), 'fizzbuzz')
    assert_equal(robot(45), 'fizzbuzz')
"""
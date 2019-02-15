## M2A07
# Fizbuzzer

""""Regras do fizz buzz:
Se posição multipla de 3: fizz
Se posição for multipla de 5: buzz
Se posição for multipla de 3 e 5: fizzbuzz
Para qualquer outra posição: numero
"""

from functools import partial

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

if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
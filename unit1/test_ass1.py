def test0():
    assert 1 == 1


# add 2 to an argument
def add_two(x):
    return x + 2


# print n lines of arguments
# return None
def print_n(x, n):
    line = str(x) * 10
    i = 0

    print('start:')

    while i < n:
        print(line)
        i = i + 1


print_n('*', 3)

line = 'a'

for i in range(5):
    line = ' ' * i + line
    print(line)

s = '*'
n = 5
marign = n

for i in range(n):
    line = ' ' * marign + s
    print(line)
    marign = marign - 1
    s = s + '*' * 2

s = '*'
n = 5
m = 4
top = '*' * n
print(top)

for i in range(m):
    line = '*' + ' ' * (n - 2) + '*'
    print(line)
print(top)

line = ''

for i in range(5):
    line = line + 'a'
    print(line)

import unittest


class TestDemo(unittest.TestCase):
    """Example of how to use unittest in Jupyter."""

    def test(self):
        self.assertEqual('foo'.upper(), 'FOO')

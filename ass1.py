allergen = 'diary'
food = input("Enter the name of the food : ")
print('It is ',
      allergen.lower() in food.lower(), ' that ', food, ' contains ', allergen)

import numpy as np

a = [[1, 2], [3, 4]]
a = np.array([[1, 2], [3, 4]])
a[:, 0]
[x for x in 'some']

s = "soma omes miss else"
[[x for x in [y for y in s.split()]]]
a = np.array([[row[i] for row in s.split()] for i in range(4)])
a[:, 1]
a[:, 0]
a[0, :]


def contains(arr, word):
    # return [x for x in word] in arr

    return word == ''.join(arr)


a
a[0]
a[1]
contains(a[0], 'some')
contains(a[1], 'some')
contains(a[:, 0], 'some')
contains(a[:, 0], 'soma')

word = 'soma'


def solution(a, word):
    return any([contains(x, word)
                for x in a]) or any([contains(x, word) for x in a.transpose()])
    # return any([x == w for x in a]) or any([x == w for x in a.transpose()])


solution(a, 'some')
solution(a, 'soma')
solution(a, 'else')
solution(a, 'elsx')

[1, 2] == [1, 2]

x = 4
28 / (x - 2) + 12 == 19 + 14 / (x - 2)
888888 / 7
999999 / 7

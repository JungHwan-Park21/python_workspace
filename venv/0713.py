data = list(range(1, 46))

import random


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


for i in range(1, 7):
    print(random_pop(data))
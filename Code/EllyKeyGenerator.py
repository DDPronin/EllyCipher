import random


def key_generation():
    k = []
    n = []
    for i in range(20):
        h = random.randint(48, 127)
        k.append(chr(h))
        n.append(h)
    return ''.join(k), n


print(key_generation())
print([chr(i) for i in range(48, 127)])

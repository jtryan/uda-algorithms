import math


def time(n):
    return 3 + 2 * math.ceil(n/5.0)

print time(50)


# divide by 5
def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y

countdown(50)


# counting steps in naive as a function of a
def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

'''
def time(a):
    return 2 * a + 3
# 3 steps in then a * 2 line in while loop
'''





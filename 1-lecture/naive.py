def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x -= 1
    return z

# print naive(63,12)
# print naive(230002939474, 28263628393203)
# print naive(4,4)
#
def rec_naive(a,b):
    if a == 0:
        return 0
    return b + rec_naive(a-1,b)

print rec_naive(17,6)
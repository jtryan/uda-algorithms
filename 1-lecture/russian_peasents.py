# multiply 2 numbers very fast
def russian(a,b):
    x = a
    y = b
    z = 0

    while x > 0:
        if x % 2 == 1:
            z = z + y
        y <<= 1
        x >>= 1
    return z


# Russian, recursive
def rec_russian(a,b):
    if a == 0: return 0
    if a % 2 == 0: return 2 * rec_russian(a/2,b)
    return b + 2 * rec_russian((a-1)/2,b)


print russian(63, 12)
# print russian(54, 83)
print russian(20, 7)
print rec_russian(230002939474, 28263628393203)


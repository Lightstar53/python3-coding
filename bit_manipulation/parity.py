# Compute parity of a very large number of 64-bit words?
# Parity of a binary word is 1 if the number of 1s in the word is odd, ow 0
# Ex: parity of 1011 is 1, parity of 1000100 is 0

# O(n) number of bits in x
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# O(k) number of 1's in x
def better_parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # Drops the lowest set bit of x

    return result

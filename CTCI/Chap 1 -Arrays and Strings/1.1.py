def is_unique_bruteforce(str):
    if len(str) == 0:
        return False

    for i in range(0, len(str)):
        for j in range(i + 1, len(str)):
            if str[i] == str[j]:
                return False
    return True

# assume 128 char alphabet
def is_unique(str):
    if len(str) == 0 or len(str) > 128:
        return False
    map_chars = {}

    for c in str:
        if map_chars.get(c) is not None:
            return False
        map_chars[c] = True
    return True

# assume 128 char alphabet
def is_unique_ary(str):
    if len(str) == 0 or len(str) > 128:
        return False
    ary = [False] * 128

    for c in str:
        val = ord(c)
        if ary[val]:
            return False
        ary[val] = True
    return True


# O(n^2)
print(is_unique_bruteforce("aceghxcvbc"))
# O(n) time, O(n) space
print(is_unique("abmcnslkj"))
# O(n) time, O(1) space
print(is_unique_ary("abmcnslkj"))

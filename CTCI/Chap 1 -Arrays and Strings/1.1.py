def is_unique_bruteforce(str):
    if len(str) == 0:
        return False

    for i in range(0, len(str)):
        for j in range(i + 1, len(str)):
            print(str[i], str[j])
            if str[i] == str[j]:
                return False
    return True

# assume 128 char alphabet
def is_unique(str):
    if len(str) == 0 or len(str) > 128:
        return False

    map_chars = {}

    for c in str:
        if map_chars[c]:
            return False
        map_chars[c] = True
    print(map_chars)
    return True


# O(n^2)
print(is_unique_bruteforce(""))
print(is_unique_bruteforce("aceghxcvbc"))

print(is_unique("aceghxcvbc"))



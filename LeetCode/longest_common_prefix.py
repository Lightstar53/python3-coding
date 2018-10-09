def horizontal_scanning(strs):
    if not strs:
        return ""
    prefix = strs[0]    # Get whole first word

    for i in range(len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Time: O(S) s = sum of all characters in all strings
print(horizontal_scanning(["heslo", "help", "hell"]))

def vertical_scanning(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]

# Time: O(S) s = sum of all characters in all strings
print(vertical_scanning(["heslo", "help", "hell"]))
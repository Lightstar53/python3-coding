import sys

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


def vertical_scanning(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    return strs[0]


def divide_and_conquer(strs, l=0, r=None):
    if r is None:
        r = len(strs) - 1

    if l == r:
        return strs[l]
    else:
        mid = (l + r) // 2
        lcp_left = divide_and_conquer(strs, l, mid)
        lcp_right = divide_and_conquer(strs, mid + 1, r)
        return common_prefix(lcp_left, lcp_right)


def common_prefix(left, right):
    minimum = min(len(left), len(right))
    for i in range(minimum):
        if left[i] != right[i]:
            return left[0:i]
    return left[0:minimum]


def binary_search(strs):
    if not strs:
        return ""

    min_len = sys.maxsize
    for str in strs:
        min_len = min(min_len, len(str))

    low = 1
    high = min_len

    while low <= high:
        middle = (low + high) // 2
        if is_common_prefix(strs, middle):
            low = middle + 1
        else:
            high = middle - 1
    return strs[0][0:(low+high)//2]


def is_common_prefix(strs, length):
    str1 = strs[0][0:length]
    for i in (1, len(strs) - 1):    # Should be len(strs) but somehow error?
        if not strs[i].startswith(str1):
            return False
    return True


strs = ["flower","flow","flight"]
# Time: O(S) s = sum of all characters in all strings
# Space: O(1)
print(horizontal_scanning(strs))

# Time: O(S) s = sum of all characters in all strings
# Space: O(1)
print(vertical_scanning(strs))

# Time: O(s) s = sum of all char in all strings
# Space: O(m*log(n)), m=space to store result, log(n) recursive calls
print(divide_and_conquer(strs))

# Time: O(s*log(n)), s = sum of all char in all strings, takes log(n) iterations
# Space: O(1)
print(binary_search(strs))
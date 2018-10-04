def isPalindromeString(x):
    """
    :type x: int
    :rtype: bool
    """
    string = str(x)
    if x < 0:
        return False
    for i in range(len(string) // 2):
        if string[i] != string[~i]:
            return False

    return True

def isPalindromeSoln(x):
    """
    :type x: int
    :rtype: bool
    """
    # if x is negative, or ends with 0
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverse = 0
    while x > 0:
        remainder = x % 10
        reverse = reverse * 10 + remainder
        x = x // 10
    return x == reverse or x == reverse / 10

# Works, but uses string. O(N)
print(isPalindromeString(10))

print(isPalindromeSoln(101))
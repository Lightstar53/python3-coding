def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))

# return True if all() elements of iterable are true
# // is integer division
# O(n) time, O(1) space


print(is_palindromic("racecar"))


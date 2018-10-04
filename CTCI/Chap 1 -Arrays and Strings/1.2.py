def is_permutation_bruteforce(s1, s2):
    if len(s1) > len(s2):
        return perm_calc(s2, s1)
    else:
        return perm_calc(s1, s2)

def perm_calc(shorter, longer):
    for i in range(0, len(shorter)):
        has_match = False
        for j in range(0, len(longer)):
            if shorter[i] == longer[j]:
                has_match = True
            if j == len(longer) - 1 and not has_match:
                return False
            if j == len(longer) - 1 and i == len(shorter) - 1:
                return True

def ctci_solution_1(s1, s2):
    if len(s1) != len(s2):
        return False
    return sort_string(s1) == sort_string(s2)

def sort_string(s):
    return ''.join(sorted(s))

def ctci_solution_2(s1, s2):
    if len(s1) != len(s2):
        return False

    letters = [0] * 128 # assuming ASCII

    for c1 in s1:
        letters[ord(c1)] += 1
    for c2 in s2:
        val = ord(c2)
        letters[val] -= 1
        if letters[val] < 0:
            return False
    return True

string1 = "god"
string2 = "dog"
# O(n^2), wrong according to leetcode
print(is_permutation_bruteforce(string1, string2))
# O(nlogn)
print(ctci_solution_1(string1, string2))
# O(n)
print(ctci_solution_2(string1, string2))
def roman_to_int(numeral):
    l = len(numeral)
    sum = 0
    for i in range(l):
        if l - i == 2:
            if numeral[i] == 'I' and numeral[i + 1] != "I":
                sum += to_int(numeral[i + 1]) - 1
                break
        sum += to_int(numeral[i])

    print(sum)
    return sum


def to_int(roman):
    if roman == 'I':
        return 1
    elif roman == 'V':
        return 5
    elif roman == 'X':
        return 10
    elif roman == 'L':
        return 50
    elif roman == 'C':
        return 100
    elif roman == 'D':
        return 500
    elif roman == 'M':
        return 1000

roman_to_int("MCMXCIV")

def roman_to_int_lc(s):
    rome_to_int = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500,
                   'M': 1000}
    num = 0
    for idx in range(len(s) - 1):
        if rome_to_int[s[idx]] < rome_to_int[s[idx + 1]]:
            num -= rome_to_int[s[idx]]
        else:
            num += rome_to_int[s[idx]]
    num += rome_to_int[s[-1]]
    return num

print(roman_to_int_lc("MCMXCIV"))
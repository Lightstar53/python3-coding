test_string = "abcdefghijklmnop"
print(test_string[0:5])  # abcde
print(test_string[-1])   # p
print(len(test_string))
test_string += "q"
print(test_string)
print(test_string[3:-5])  # start from index 3 to 5 from end
print(test_string[-3:])   # 3 from end to end
print(test_string[1:5:2]) # go from index 1-5, and skip by 2
print(test_string[::-1])  # reverse order
print(test_string[1:] + test_string[:1]) # rotate string by 1 to the left
copy = test_string[:]   # shallow copy
print(copy)
string_spaces = "    i have a lot of spaces!!   "
print(string_spaces.strip())

upper = "UIPER"
print(upper.lower())
print("abc".startswith("a"))
print("abc".endswith("c"))

print(string_spaces.strip().split(" "))

name = "joe"
print("Name: {name}".format(name = name))
print("Name: {}".format(name))
print(f"Name: {name}")

joined = "!".join(["12","h","s"])
print(joined)   # join a sequence with string separators

print(ord("3"))
print(chr(97))
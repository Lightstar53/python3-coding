l = list(range(20))
print(l)
print([1] + [5,2,3])
print([0] * 10)
l.append(20)
print(l)
l.insert(3, 80)
print(l)
l.remove(80)
print(l)

print(20 in l)

list = [x**2 for x in range(6) if x % 2 == 0]
print(list)
print(min(list))
print(max(list))

unsorted = [3,1,5]
unsorted.sort()
print(unsorted)
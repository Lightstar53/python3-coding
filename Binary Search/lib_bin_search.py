from bisect import *

sorted_list = [1, 3, 5]
left = bisect_left(sorted_list, 3)
# 1st element < targeted value (index)
print(left)

right = bisect_right(sorted_list, 10)
# 1st element > targeted value (index)
print(right)

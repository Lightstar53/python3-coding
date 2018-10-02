def bubble_sort(ary):
    is_sorted = False
    last_unsorted = len(ary) - 1
    while not is_sorted:
        is_sorted = True
        for i in range(0, last_unsorted):
            if ary[i] > ary[i + 1]:
                swap(ary, i, i + 1)
                is_sorted = False
        last_unsorted -= 1
    return ary


def swap(ary, i, j):
    tmp = ary[i]
    ary[i] = ary[j]
    ary[j] = tmp


list = [1, 5, 2, 10, 3, 5, 1, 7]
print(bubble_sort(list))
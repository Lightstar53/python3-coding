def quicksort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left >= right:
        return

    pivot = array[left + right // 2]
    index = partition(array, left, right, pivot)
    quicksort(array, left, index - 1)
    quicksort(array, index, right)


def partition(array, left, right, pivot):
    while left <= right:
        while array[left] < pivot:
            left += 1

        while array[right] > pivot:
            right -= 1

        if left <= right:
            swap(array, left, right)
            left += 1
            right -= 1
    return left


def swap(ary, i, j):
    tmp = ary[i]
    ary[i] = ary[j]
    ary[j] = tmp

def merge_sort(array, tmp=[], left_start=0, right_end=None):
    if right_end is None:
        right_end = len(array) - 1
    if left_start >= right_end:
        return

    middle = left_start + right_end // 2
    merge_sort(array, tmp, left_start, middle)
    merge_sort(array, tmp, middle + 1, right_end)
    merge_halves(array, tmp, left_start, right_end)


def merge_halves(array, tmp, left_start, right_end):
    left_end = right_end + left_start // 2
    right_start = left_end + 1
    size = right_end - left_start + 1

    left = left_start
    right = right_start
    index = left_start

    while left <= left_end and right <= right_end:
        if array[left] <= array[right]:
            tmp[index] = array[left]
            index += 1
            left += 1
        else:
            tmp[index] = array[right]
            right += 1
        index += 1

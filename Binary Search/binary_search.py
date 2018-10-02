class BinarySearch:
    @staticmethod
    def binary_search_recursive(array, x, left=0, right=None):
        if right is None:
            right = array.length - 1
        if left > right:
            return False

        mid = (left + right) // 2
        if array[mid] == x:
            return True
        elif x < array[mid]:
            return BinarySearch.binary_search_recursive(array, x, left, mid - 1)
        else:
            return BinarySearch.binary_search_recursive(array, x, mid + 1, right)

    @staticmethod
    def binary_search_iterative(array, x):
        left = 0
        right = array.length - 1

        while left <= right:
            mid = (left + right) // 2
            if array[mid] == x:
                return True
            elif x < array[mid]:
                right = mid - 1
            else:
                left = mid + 1


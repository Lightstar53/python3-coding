class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_negative = False

        if x < 0:
            is_negative = True
            x = x * -1

        reverse = 0
        while x > 0:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x = x // 10

        if is_negative:
            if (-1 * reverse) < (-2 ** 31):  # Watch bounds
                return 0
            return reverse * -1
        else:
            if reverse > (2 ** 31 - 1):  # Watch bounds
                return 0
            return reverse



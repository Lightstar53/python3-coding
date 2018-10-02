def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


# O(n) space
def fib_cache(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fib_cache(n - 1) + fib_cache(n - 2)
    return cache[n]


# O(1) space
def fib_iterative(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


fib = memoize(fib)
print(fib(10))
print(fib_cache(10))
print(fib_iterative(10))

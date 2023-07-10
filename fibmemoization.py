def fib(n, memo: {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


result = []
for i in range(10):
    result.append(fib(i, {}))
print(result)

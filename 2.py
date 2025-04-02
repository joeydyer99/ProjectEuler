memo = {1: 1, 2:2}
def fib(n):
    if(n in memo): return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
sum = 0
for i in range(1, 1000000):
    x = fib(i)
    print(x)
    if(x > 4000000):break
    if(fib(i) % 2 ==0):sum+=fib(i)
print(sum)
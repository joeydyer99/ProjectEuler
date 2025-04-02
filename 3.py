from math import sqrt
num = 600851475143
for i in range(int(sqrt(num)), 2, -1):
    if(num % i == 0):
        isPrime = True
        for j in range(2, int(sqrt(i))):
            if(i % j == 0):
                isPrime = False
                break
        if(isPrime): print(i)
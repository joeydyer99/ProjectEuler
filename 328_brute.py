import sys
import matplotlib.pyplot as plt
import numpy as np
from functools import reduce
from math import sqrt

INF = sys.maxsize

memo = {(1,1): 0, (1,2): 2}
memoFirst = {}
memoSecond = {}
memoHigher = {}
memoLower = {}
memo2 = {}

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))


def minGuess(start, end):
    if(end-start in memo2): return memo2[(end-start)]
    if(start >= end): return 0
    if(end - start == 0): return 0
    if(end - start == 1): return 1
    if(end - start == 2): return 1
    mminbest = INF
    val = 0
    for i in range(start, end+1, 1):
        worstcase = 0
       # lowWorstcase = 1+ lowestCost(start, i-1)
        #highWorscase = 1+lowestCost(i+1, end)
        worstcase = 1 + max(minGuess(start, i-1), minGuess(i+1, end))

        if(worstcase < mminbest):
            mminbest = worstcase
            val = i
        #worstcase = 1 + max(minGuess(start, i-1), minGuess(i+1, end))
        mminbest = min(worstcase, mminbest)
    #print(i)
    memo2[(end-start)] = mminbest
    return mminbest
def addToFirst(end, val):
    if(end not in memoFirst):
        memoFirst[end] = set()
    memoFirst[end].add(end-val)
    
def addToSecond(end,start, val):
    if(end not in memoSecond):
        memoSecond[end] = set()
    memoSecond[end].add(val+start)

#def lowestCostBrute(start, end):
  
def lowestCost(start, end):
   # print(start, end)
   # if((start, end) in memo): return memo[(start, end)]
    if(start >= end): return 0
    if(end - start == 0): 
        memo[(start, end)] = 0
    if(end - start == 1): 
        #memoFirst[(start, end)] = start
        addToFirst(end, start)
        addToSecond(end, start, start)
        memo[(start, end)] = start
    if(end - start == 2): 
        addToSecond(end, start, end-1)
        addToFirst(end, end-1)
       # memoFirst[(start, end)] = end-1
        memo[(start, end)] = end-1
    if((start, end) in memo): return memo[(start, end)]

    mminbest = INF
    val = start
    val2 = start
    #for i in range(start, end+1, 1):
    j = 2
    while j <= end-start:
        i = end-j+1
        x = start+j-1
        #print(start, end, i, x)
        j = j<<1
        worstCaseX = INF
        worstCaseI = INF
        if(i < end and i > start):
              worstCaseI = i + max(lowestCost(start, i-1), lowestCost(i+1, end))
        if(x < end and x > start):
            worstCaseX = x + max(lowestCost(start, x-1), lowestCost(x+1, end))
        worstcase= min(worstCaseI, worstCaseX)
    #for i in range(start, end+1):
        #print(i)
        #worstcase = 0
        #lowWorstcase = i+ lowestCost(start, i-1)
        #highWorscase = i+lowestCost(i+1, end)
        #worstcase = i + max(highWorscase, lowWorstcase)
    #print(i , worstcase)
        if(worstcase < mminbest):
            #print(start, end , i, worstcase)
            #if((start, end) not in memoFirst): memoFirst[start, end] = []
            val = i
            if(worstCaseX < worstCaseI):
                val = x
            #val2 = x
      
            #if(worstcase > lowWorstcase):
            #    memoHigher[(start,end)] = highWorscase
            #    if((start, end) in memoLower): del memoLower[(start,end)]
            #else:
            #    memoLower[(start, end)] = lowWorstcase
            #    if((start, end) in memoHigher): del memoHigher[(start,end)]
            mminbest = worstcase
        #
        # mminbest = min(mminbest, i + max(lowestCost(start, i-1), lowestCost(i+1, end)))
   # print(mminbest)
    if(end not in memoFirst):
        memoFirst[end] = set()
    memoFirst[end].add(end-val)
    addToSecond(end, start, val)
    memo[(start, end)] = mminbest
    return mminbest
#sum = 3
z=  []
y= []
setAdds = set()
mul2 = set()
x = 900
j = 2
#for i in range(901):
#    print( i, minGuess(1, i))
while j < x:
    i = j-1
    j=j<<1
    toAdd = set()
    mul2.add(j)
    for v in mul2:
        if(v < i):
            toAdd.add(v+i)
    setAdds.update(toAdd)
    setAdds.add(i)
#print(setAdds)  
     
#print(lowestCost(1, 100))
sum = 0
for i in range(1, 201):
   # z.append(i)
    sum+=lowestCost(1, i)
    print(i)
print(sum)
   # y.append(memoFirst[(1, i)])
#    x = (1, i)
    #if(i > 4) : print(x, memo[x], memoFirst[x], memoFirst[((1, i-1))])
    #if((1, i)  in memoLower): print((1,i), memoLower[(1,i)])
for x in memoFirst:
    print(x, memoFirst[x], minGuess(1, x))
#print(memoHigher)
#print(memoLower)
   # print(i)
#for x in memoFirst:
#    print(x, memoFirst[x])
#print(memoFirst)
#fig, ax = plt.subplots()
#ax.scatter(np.array(z), np.array(y))
#plt.show()
#for x in memo:
#    z,y = x
   # print(x, y- memoFirst[x])
        #sum += memo[x]
    #if(z==1 and x in memoLower): print(x, memoFirst[x], memoLower[x], lowestCost(z, memoFirst[x]-1), minGuess(memoFirst[x]+1, y))
    #if(z==1 and x in memoHigher): print("Higher", x, memoFirst[x], memoHigher[x], lowestCost(z, memoFirst[x]-1), minGuess(memoFirst[x]+1, y))

    #if(z == 1 and y > 5 and memoFirst[x] < memoFirst[(z, y-1)]+1 ):
    #    print(x, memo[x], memoFirst[x], memoFirst[((z, y-1))], factors(y), minGuess(memoFirst[x]+1, y) )
   # print(x, memo[x], memoFirst[x], factors(y))

print(sum)
dist = {}
#for i in range(1, 200001):
#    for j in range(1, 200001):
#        dist[(i,j)] = INF

#print(memo[16,19])
#print(memo[(17,20)])# 36
#print(memo[(1, 17)]) #38
#print(memo[(1,12)])# 21
#print(memo[(14, 20)]) # 36 (memo is higher than other)
#print(memo[(14,20)]) #24+36
#print(memoFirst[(1,20)], memoFirst[(1,16)])
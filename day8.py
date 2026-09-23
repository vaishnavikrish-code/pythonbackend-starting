#dp memo or tabu
#first example in fabonacci
#naive resusion
def fab(n):
    if n <= 1:
        return n
    return fab(n-1)+fab(n-2)
#for i in range (10):
    #print(f"{fab(i)}")
num = fab(7)
result= fab(num)
print(f"num:{result}")

#app(2):memo
def fab(n,memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n 
    memo[n] = fab(n-1,memo)+fab(n-2,memo)
    return memo[n]
for i in range(10):
    print(f"{fab(i)}")
print()
#app4
def fib(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b

#climbing staPROBLEM: Can climb 1 or 2 steps at a time
#How many distinct ways to reach n stairs?

#Example: n=3
#-1 + 1 + 1
#- 1 + 2
#- 2 + 1  ans 3 ways  ways(n) = ways(n-1)+ways(n-2)
def clmbs(n , memo={}):
    if n <=2:
        return n
    if n in memo:
        return memo[n]
    memo[n]=clmbs(n-1,memo)+clmbs(n-2,memo)
    return memo[n]

n = 5
print(clmbs(n))



#dp
def cs(n):
    if n <= 2:
        return n
    dp =  [0] *(n+1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
for n in [1,2,3,4,5]:
    result = cs(n)
    print(f"cs({n})={result}")
print()

#coin change:

#PROBLEM: Given coins [1, 2, 5], minimum coins to make amount=5?
#Answer: 1 (one 5-coin)
#approch dp[i] = min(dp[i],1+dp[i-coin])
def coin(coins,amount):
    dp = [float('inf')]*(amount + 1)
    dp[0]=0

    for i in range(1,amount+1):
        for coin in coins:
            if coin <= i:
                dp[i]= min(dp[i],1+dp[i-coin])
    return dp[amount] if dp[amount] != float('inf') else-1

result =coin([1,2,5],5)
print(f"{result}")
result=coin([2],3)
print(f"{result}")
result=coin([10],1)
print(f"{result}")


#recusive 
def cc(coins,amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')
    minu = float('inf')

    for coin in coins:
        result = cc(coins,amount-coin)

        if result != float('inf'):
            minu=min(minu,1+result)
    return minu

result =cc([1,2,5],5)
if result == float('inf'):
    print(-1)
else:
    print(result)
    
    
def rob(nums):
    if not nums:
        return 0
    if len(nums)==1:
        return nums[0]
    dp = [0]*len(nums)
    dp[0] =  nums[0]
    dp[1] = max(nums[0],nums[1])

    for i in range(2, len(nums)):
        dp[i]=max(dp[i-1],nums[i]+dp[i-2])
    return dp[-1]

test_cases = [
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1],
    [5],
    [2, 1],
]
for  nums in test_cases:
    result = rob(nums)
    print(f"rob({nums})={result}")  
print()


def lengthlis(nums):
    if not nums:
        return 0
    n  = len(nums)
    dp = [1] * n

    for i in range(1,n):
        for j in range(i):
            if nums[j]<nums[i]:
                dp[i]=max(dp[i],dp[j]+1)
    return max (dp)
test_cases = [
    [10, 9, 2, 5, 3, 7, 101, 18],
    [0, 1, 0, 4, 4, 4, 3, 5, 1],
    [3, 10, 2, 1, 20],
]

for nums in test_cases:
    result = lengthlis(nums)
    print(f"{nums}={result}")
print()


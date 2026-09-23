#cal factorial

def fac(n):
    if  n == 0:
        return 1
    return n * fac(n-1)
result=fac(5)
print(f"{result}")

    
#sum of two num
def sumofnum(n):
    if n == 0:
        return 0
    return n + sumofnum(n-1)
result=sumofnum(5)
print(f"{result}")

#power
def power(base,exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)
    #base = num power = power of num ex 3power4 = 3 * 3power3  (4-1=3)
result=power(2,4)
print(f"{result}")

#fibonacci
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+ fib(n-2)
result =fib(7)
print(f"{result}")

#(0, 1, 1, 2, 3, 5, 8, 13) it get last num 

def fibonacci_generator(n):
    """Yields Fibonacci numbers one by one up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
result=list(fibonacci_generator(6))
print(f"{result}") #this get the[0,1,1,2,3,5]

#permutaion

def per(nums):
    result = []

    def backtracking(current,remaining):
        if not remaining:
            result.append(current[:])
            return
        for i in range (len(remaining)):
            val =remaining[i]
            current.append(val)

            backtracking(current,remaining[:i]+remaining[i+1:])

            current.pop()

    backtracking([],nums)
    return result
perms=per([1,2,3])
for perm in perms:
    print(f"{perm}")


def combinations(nums,K):
    result = []
    def backtracking(start,current):
       if len(current)==K:
          result.append(current[:])
          return
       for i in range(start,len(nums)):
           current.append(nums[i])
           backtracking(i+1,current)

           current.pop()
    backtracking(0,[])
    return result
combos=combinations([1,2,3],2)
for combo in combos:
    print(f"{combo}")



def wordfind(board,word):
    if not board or not word:
        return False
    def dfs(i,j,index):
        if index==len(word):
            return True

        if i < 0 or i >=len(board) or j < 0 or j >= len(board[0]):
            return False
        if board[i][j] != word[index]:
            return False
        original = board[i][j]
        board[i][j] = '#'

        found  =  (dfs(i+1,j,index + 1) or
                  dfs(i-1,j,index+1) or
                  dfs(i,j+1,index+1) or
                  dfs(i,j-1,index+1))

        board[i][j] = original
        return found
    for  i in range(len(board)):
        for j in range(len(board[0])):
            if dfs (i,j,0):
                return True
    return False
board = [
    ['B', 'O', 'A', 'T'],
    ['O', 'A', 'T', 'S'],
    ['A', 'B', 'A', 'T'],
    ['T', 'A', 'C', 'T']
]

wordsearch=["BOAT", "CATS", "BOAST", "BAT"]
print("board:")
for row in board:
    print(f" {row}")

for word in wordsearch:
    found = wordfind([row[:] for row in board],word)
    print(f"'{word}':{found}")
print()
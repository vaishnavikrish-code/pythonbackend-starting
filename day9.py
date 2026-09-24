#lcs longest common subsequence

#s1="abcde",s2="ace"
#lcs = "ace" length 3

def longest(text1,text2):
    m,n=len(text1),len(text2)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1, n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j]= dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1],dp[i][j-1])
    return dp[m][n]
result = longest("abcde","ace")
print = (f"{result}")

def edit(word1,word2):
    m, n = len(word1),len(word2)
    dp=[[0]*(n+1)for _ in range(m + 1)]

    for i in range(m+1):
        dp[i][0]=i
    for j in range(n+1):
        dp[0][j]=j

    for i in range(1,m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]= 1+min(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1]

                )
    return dp[m][n]
result=edit("hores","ros")
print(f"{result}")


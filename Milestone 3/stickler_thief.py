def FindMaxSum(a, n): #first row is not included, second row is included 
    dp=list()
    # for i in range(2):
    #     dp.append([0]*n)
    # dp[0][0]=0
    # dp[1][0]=a[0]
    # for i in range(1,n):
    #     dp[0][i]=dp[1][i-1]  
    #     dp[1][i]=max(dp[0][i-1]+a[i],dp[0][i-1])
    dp=[0]*(n+1)
    for i in range(1,n):
        if i==1:
            dp[i]=a[i-1]
        if i==2:
            dp[i]=max(dp[i-1],a[i-1])
        else:
            dp[i]=max(dp[i-2]+a[i-1],dp[i-1],a[i-1]+dp[i-3])
    return max(dp[0][-1],dp[1][-1])

print(FindMaxSum([5,5,10,100,10,5],6))

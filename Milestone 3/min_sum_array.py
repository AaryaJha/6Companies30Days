def minDifference(arr,n):
    m=sum(arr)
    dp=list()
    for i in range(len(arr)+1):
        dp.append([0]*(m+1))
    dp[0][0]=1
    # print(dp)
    for i in range(1,len(arr)+1):
        for j in range(m+1):
            if dp[i-1][j]==1:
                dp[i][j]=1
            else:
                if j>=arr[i-1]:
                    if dp[i-1][j-arr[i-1]]:
                        dp[i][j]=1
    total=m
    m=m+2
    # print(dp[-1])
    for j in range(total // 2, -1, -1):
        if dp[n][j] == True:
            m = total - (2 * j)
            break
    return m  

print(minDifference([1,6,11,15],4))
	
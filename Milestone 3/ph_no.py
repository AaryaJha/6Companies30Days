def possibleWords(arr,n):
    d2l={0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    arr=list(reversed(arr))
    dp=[[] for i in range(n)]
    dp[0].extend(d2l[arr[0]])
    for i in range(1,n):
        if arr[i]==0 or arr[i]==1:
            dp[i]=dp[i-1][:]
        else:
            if len(dp[i-1])==0:
                dp[i].extend(d2l[i])
            for c in d2l[arr[i]]:
                dp[i]+=[c+ch for ch in dp[i-1]]
            
    return dp[i-1]
# l=[1,2,3]
# ll=list(reversed(l))
# d=[[] for i in range(len(l))]
# d[0].extend("bgh")
# c="xyz"
# d[1]=[j+i for j in c for i in d[0] ]
# print(d)
print(possibleWords([2,1,2],3))




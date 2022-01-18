def fourSum(arr,k):
    dp={}
    for j in range(k+1):
        dp[j]=[]    
    for i in range(len(arr)):
        if arr[i]>k:
            continue
        for j in range(k+1):
            if arr[i]<=j:
                l=dp[j-arr[i]]
                ans=[]                
                if len(l)==0 and arr[i]==j:                    
                    dp[j].append([arr[i]])
                    continue
                elif len(l)!=0:
                    for el in l:
                        if len(el)>=4:
                            continue
                        ll=el[:]+[arr[i]]
                        if ll not in dp[j] and ll not in ans:
                            ans.append(ll)
                    dp[j].extend(ans)
        for el in dp[k]:
            if len(el)!=4:
                dp[k].remove(el)
        print(dp[k])
    return dp
            
    

fourSum([0,0,2,1,1],3)



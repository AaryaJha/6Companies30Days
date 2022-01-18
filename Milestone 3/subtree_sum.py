def countSubtreesWithSumX(root, x,flag=1):
    if root==None:
        return [0,0] #sum,count
    else:
        ra=countSubtreesWithSumX(root.right,x,0)
        la=countSubtreesWithSumX(root.left,x,0)
        s=root.value+ra[0]+la[0]
        count=ra[1]+la[1]
        if flag==1:
            if s==x:
                count+=1
            return count
        if s==x:
            return [s,count+1]
        else:
            return [s,count]

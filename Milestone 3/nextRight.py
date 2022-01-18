def connect(root):
    
    pq=[root]     
    q=list()
    while(len(pq)!=0):
        el=pq.pop(0)
        if len(pq)!=0:
            el.nextRight=pq[0]
        else:
            el.nextRight=None
        if el.right!=None:
            q.append(el.right)
        if el.left!=None:
            q.append(el.left)
        if len(pq)==0:
            pq=q[:]
            q=[]
    return root
    

    
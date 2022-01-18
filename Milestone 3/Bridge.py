#to detect if given edge is a bridge in a graph 
#if after removing edge numberof components increase, it is an edge 
#or after removing the edge c,d there's a way to go from c to d then it is not a bridge
def isBridge(self, V, adj, c, d):
        # code here
        c1=0
        visited={}
        examined={}
        for c in range(V):
            visited[c]=False
            examined[c]=False
        stack=list()
        
        while(False in visited.values()):
            if False in visited.values():
                for i in range(V):
                    if visited[i]==False:
                        examined[i]=True
                        stack.append(i)
                        break
            while (len(stack)!=0):
                el=stack.pop()
                visited[el]=True
                for child in adj[el]:
                    if examined[child]==False:
                        examined[child]=True
                        stack.append(child)
            
            c1+=1
        
        adj[c].remove(d)
        adj[d].remove(c)
        c2=0
        for c in range(V):
            visited[c]=False
            examined[c]=False
        stack=[]
       
        while(False in visited.values()):
            if False in visited.values():
                for i in range(V):
                    if visited[i]==False:
                        examined[i]=True
                        stack.append(i)
                        break
            while (len(stack)!=0):
                el=stack.pop()
                visited[el]=True
                for child in adj[el]:
                    if examined[child]==False:
                        examined[child]=True
                        stack.append(child)
            
            c2+=1
        
        if c2==c1:
            return 0
        else:
            return 1


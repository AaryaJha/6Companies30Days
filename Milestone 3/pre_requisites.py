def isPossible(N,prerequisites):
    graph=dict()
    for i in range(N):
        graph[i]=[]
    for [m,n] in prerequisites:        
        graph[n].append(m)
    #finding a task which has no pre req 
    start=-1
    for i in range(N):
        flag=0
        for node,dependency in graph.items():
            if i in dependency:
                flag=1
                break
        if flag==0 and len(graph[i])!=0:
            start=i
            break
    #carrying out bfs 
    visited=dict()
    for i in range(N):
        visited[i]=False
    visited[start]=True
    
    examined=[]
    queue=[start]
    while len(queue)!=0:
        examined.append(queue.pop(0))
        for dep in graph[examined[-1]]:
            if visited[dep]==False:
                visited[dep]=True
            if dep not in examined:
                queue.append(dep)
    
    if False in visited.values():
        return False 
    else:
        return True  
    





print(isPossible(4,[[1,0],[2,1],[3,2]]))




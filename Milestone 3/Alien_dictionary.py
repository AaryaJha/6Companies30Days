def findOrder(dict, N, K):    
    graph={}
    alpha="abcdefghijklmnopqrstuvwxyz"    
    for i in range(K):
        graph[alpha[i]]=[]
        
    for i in range(N):        
        if i>0:
            a,b=dict[i-1],dict[i]
            print(a,b)
            diff=[i for i in range(min(len(a),len(b))) if a[i]!=b[i]]
            if dict[i][diff[0]] not in graph[dict[i-1][diff[0]]]:
                graph[dict[i][diff[0]]].append(dict[i-1][diff[0]])
                
    #topological sort 
    start="z"
    visited=[]
    print(graph)    
    while(len(visited)<K):
        for key in graph:
            if len(graph[key])==0 and key not in visited:
                start=key
                break
        visited+=[start]
        for parents in graph.values():
            if start in parents:
                parents.remove(start)
    print(visited)

    

findOrder(["baa","abcd","abca","cab","cad"],5,4)


            
# for j in range(len(dict[i])):
#             if j+1<len(dict[i]) and dict[i][j]!=dict[i][j+1]:
#                 graph[dict[i][j]].append(dict[i][j+1])
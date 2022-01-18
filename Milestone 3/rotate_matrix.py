def rotate(matrix): 
    #code here
    for i in range(len(matrix[0])):
        for j in range(0,len(matrix[0])//2):
            temp=matrix[i][j]
            matrix[i][j]=matrix[i][-j-1]
            matrix[i][-j-1]=temp
    for i in range(len(matrix[0])):
        for j in range(i,len(matrix[0])):
            temp=matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=temp
    return matrix

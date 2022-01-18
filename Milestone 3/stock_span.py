prc=[10,4,5,90,120,80]
rec=[[0,0] for i in range(len(prc))]
rec[0]=[prc[0],0]
for i in range(1,len(prc)):
    if prc[i-1]>prc[i]:
        rec[i]=[prc[i-1],i-1]
    else:
        if rec[i-1][0]>prc[i]:
            rec[i]=[rec[i-1][0],rec[i-1][1]]
        else:
            index=rec[i-1][1]
            while index!=0:
                if prc[index]<prc[i]:
                    if rec[index][0]<prc[i]:
                        index=rec[index][1]
                        continue
                    else:
                        rec[i]=[rec[index][0],rec[index][1]]
                        break
                else:
                    rec[i]=[prc[index],index]
                    break
answer=[0]*len(prc)
answer[0]=1
for i in range(1,len(rec)):
    if rec[i][0]!=0:
        answer[i]=i-rec[i][1]
    else:
        answer[i]=i+1


print(answer)

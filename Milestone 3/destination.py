#minimum numer of ways of reaching destination
# important  
def min_steps(d):
    s=0
    count=1
    step=0
    while (s!=d):
        print(s,count)
        if s<d:
            s=s+count
        else:
            count=count-1
            s=s-2*count
            step-=1
        step+=1
        count+=1
    return step

print("Answer: ",min_steps(5))


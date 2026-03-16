#Question
'''Given two integers n and k, find k integers such that their product is n and each integer is greater than 1.'''

n,k=map(int,input().split())
if k==1:
    print(n)
else:
    factors=[]
    temp_n=n
    d=2
    while d*d<=temp_n:
        while temp_n%d==0:
            factors.append(d)
            temp_n//=d
            if len(factors)==k-1:
                break
        if len(factors)==k-1:
            break
        d+=1
    if len(factors)==k-1 and temp_n>1:
        factors.append(temp_n)
        print(*factors)
    else:
        print(-1)


def is_danjo(n): ## n이 2345면
    k=n%10   ### 1의자리 5
    m=int(n/10) ### 10의자리부터.. 234
    while not m==0:
        if m%10>k: ## 앞숫자가 뒷보다 클 경우 False
            return False
        k=m%10
        m=int(m/10)
    return True

c = 0
for g in range(int(input())):
    N=int(input())
    c+=1
    a = list(map(int,input().split()))
    res = -1
    for i in range(N):      
        for j in range(i+1,N):    ## 1-2,1-3,1-4
            if a[i]*a[j] > res:
                if is_danjo(a[i]*a[j]):
                    res=a[i]*a[j]

    print(f'#{c} {res}')
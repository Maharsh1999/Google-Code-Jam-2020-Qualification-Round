def checkRepeat(arr):
    seen = set(arr)
    if(len(seen)!=len(arr)):
    	return 1
    return 0

T=int(input())
output=[]
for i in range(T):
	rr=0
	cr=0
	trace=0
	N=int(input())
	arr = [[0]*N]*N
	for i in range(N):
		arr[i] = list(map(int, input().split(' ')))
		rr+=checkRepeat(arr[i])
	for j in range(N):
		tarr=[]
		for i in range(N):
			tarr.append(arr[i][j])
			if(i==j):
				trace+=arr[i][j]
		cr+=checkRepeat(tarr)
	output.append([trace,rr,cr])
for i in range(T):
	print("Case #%d: %d %d %d" %(i+1,output[i][0],output[i][1],output[i][2]))


//------------------------------------------------------------



	T=int(input())
output=[]
for _ in range(0,T):
    N=int(input())
    acti=[]
    start=[]
    end=[0,0]
    Actp=[]
    imp=False
    for j in range(0,N):
        Actp.append('C')
    for j in range(0,N):
        t=input().split()
        t[0]=int(t[0])
        t[1]=int(t[1])
        t.append(j)
        start.append(int(t[0]))
        acti.append(t)
    acti.sort()
    for j in range(0,len(acti)):
        if(end[0]<=acti[j][0]):
            Actp[acti[j][2]]='C'
            end[0]=acti[j][1]
        else:
            if(end[1]<=acti[j][0]):
                Actp[acti[j][2]]='J'
                end[1]=acti[j][1]
            else:
                imp=True
    if(imp):
        output.append("IMPOSSIBLE")
    else:
        asti=""
        for j in Actp:
            asti+=str(j)
        output.append(asti)
for i in range(T):
	print("Case #%d: %s" %(i+1,output[i]))
def DISTRIBUTE(arr):
	dl=[]
	str1=""
	C=[]
	J=[]
	C.append(arr[0])
	dl.append("C")
	for i in range(1,len(arr)):
		for j in range(len(C)):
			if((arr[i][0]>C[j][0] and arr[i][0]<C[j][1]) or (arr[i][1]>C[j][0] and arr[i][1]<C[j][1])):
				for k in range(len(J)):
					if((arr[i][0]>J[k][0] and arr[i][0]<J[k][1]) or (arr[i][1]>J[k][0] and arr[i][1]<J[k][1])):
						return "IMPOSSIBLE"
					else:
						J.append(arr[i])
						dl.append("J")
				if(len(J)==0):
					J.append(arr[i])
					dl.append("J")
			else:
				C.append(arr[i])
				dl.append("C")
				break;
	return (str1.join(dl))


T=int(input())
output=[]
for i in range(T):
	N=int(input())
	arr = [[0]*2]*N
	for i in range(N):
		arr[i] = list(map(int, input().split(' ')))
	output.append(DISTRIBUTE(arr))
for i in range(T):
	print("Case #%d: %s" %(i+1,output[i]))




"""
dl=['C']
	str1=""
	Cstat=1
	Jstat=0
	for i in range(1,len(arr)):
		if(arr[i][0]<arr[i-1][1]):
			if(Cstat==0):
				dl.append("C")
			elif(Jstat==0):
				dl.append("J")
			else:
				return "IMPOSSIBLE"
		else:
			if(Cstat==0):
				dl.append("C")
			elif(Jstat==0):
				dl.append("J")
			else:
				return "IMPOSSIBLE"
	return (str1.join(dl))"""
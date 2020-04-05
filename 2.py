def createStr(str):
	pc=0
	ns=[]
	sd=list(str)
	for i in sd:
		if(i=="0"):
			while(pc!=0):
				ns.append(")")
				pc-=1
			ns.append("0")
		else:
			a=int(i)
			while(pc!=a):
				if(pc<a):
					ns.append("(")
					pc+=1
				else:
					ns.append(")")
					pc-=1
			ns.append(i)
	if(pc!=0):
		while(pc!=0):
			ns.append(")")
			pc-=1
	str1=""
	return (str1.join(ns))


T=int(input())
output=[]
for i in range(T):
	S = input()
	output.append(createStr(S))
for i in range(T):
	print("Case #%d: %s" %(i+1,output[i]))

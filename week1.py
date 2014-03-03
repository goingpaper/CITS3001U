def naive(T,P):
	result = []
	n = len(T)
	m = len(P)
	for i in range(n-m):
		match = True
		for j in range(m-1):
			if T[i+j]!=P[j]:
				match = False
		if match:
			result.append(i) 
	return result


def RBK(T,P):
	T = list(T)
	P = list(P)
	p = 0
	n = len(T)
	m = len(P)

	for j in range(m):
		p = p * 10 + int(P[j])
		print p
	z = 0
	for j in range(m-1):
		z = z * 10 + int(T[j])
		#print z 

	result = []

	for s in range(n-m+1):
		print z % 10**(m-1)*10 + int(T[s+m-1])
		z = z % 10**(m-1) * 10 + int(T[s+m-1])
		print str(p)+"\n __ \n"
		if z == p:
			result.append(s)
	return result

def RBKG(T,P):
	T = list(T)
	P = list(P)
	p = 0
	q = 13
	n = len(T)
	m = len(P)

	for j in range(m):
		p = p * 10 + int(P[j])

	pdelta = p % q

	z = 0
	for j in range(m-1):
		z = z * 10 + int(T[j])
		#print z 

	result = []

	for s in range(n-m+1):
		print z % 10**(m-1)*10 + int(T[s+m-1])
		z = z % 10**(m-1) * 10 + int(T[s+m-1])
		zd = z % q
		print str(p)+"\n __ \n"
		match = True
		if zd == pdelta:
			Plist = list(str(p))
			Zlist = list(str(z))
			for i in range(len(Plist)):
				if Plist[i]!=Zlist[i]:
					match = False
			if match:
				result.append(s)

	return result

def KMP(T,P):
	pass

def recurt(word):
	wordl = [word]
	words = []
	while len(wordl)>0:
		current = wordl.pop()
		if current not in words:
			words.append(current)
		if len(current)==1:
			continue
		first = current[1:]
		sec = current[:-1]
		print first
		print "\n"+sec+"\n __"
		wordl.append(first)
		wordl.append(sec)

	return words

	

def prefix(P):
	kvals = []
	for i in range(0,len(P)):
		current = P[:i]
		prefixes = []
		jj = i-1
		while(jj>0):
			prefixes.append(P[:jj])
			jj-=1

		scheck = P[1:i+1]
		kval = 0
		print scheck+":"
		for k in prefixes:
			print ":"+k
			res = naive(scheck,k)
			#print res
			if len(res)>0 and len(k)>kval:
				kval = len(k)
		kvals.append(kval)

	return kvals

print prefix("abbabaa")
print naive("bbabaa","abb")

#print RBKG("12323142412345523123","123")

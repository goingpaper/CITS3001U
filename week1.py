def naive(T,P):
	result = []
	n = len(T)
	m = len(P)
	for i in range(n-m+1):
		match = True
		for j in range(m):
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
	pie = prefix(P)
	q = 0
	result = []
	n = len(P)
	m = len(T)
	for i in range(m):
		print q
		if q == n-1:
			result.append(i-n+1)
			q = pie[q]
		while q>-1 and P[q] != T[i]:
			print q
			q = pie[q]
			if q == pie[q]:
				break
		if P[q] == T[i]:
			q =q+1

	return result

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
		jj = i
		while(jj>0):
			prefixes.append(P[:jj])
			jj-=1

		scheck = P[1:i+1]
		kval = 0
		#print scheck+":"
		len_shc = len(scheck)
		for k in prefixes:
			#print ":"+k
			len_k = len(k)
			res = naive(scheck,k)
			#print res
			if len(res)>0 and kval==0 or len(res)>0 and len_k<kval:

				last = res[-1]
				calc = len_shc - len_k
				#print last
				#print calc
				if last == len_shc - len_k:
					kval = len(k)

		kvals.append(kval)

	return kvals

def boyer(T,P):
	result = []
	n = len(T)
	m = len(P)
	for i in range(n-m+1):
		match = True
		for j in range(m-1,-1,-1):
			if T[i+j]!=P[j]:
				match = False
				break
		if match:
			result.append(i) 
	return result

def LCSn(X,Y):
	i = len(X)
	j = len(Y)
	#print X
	#print Y
	if i*j==0:
		return ""
	if X[i-1]==Y[j-1]:
		return LCSn(X[:i-1],Y[:j-1])+X[i-1]
	if X[i-1]!=Y[j-1]:
	
		return max(LCSn(X[:i-1],Y),LCSn(X,Y[:j-1]))


#print prefix("aba")
#print naive("bba","a")
#print naive("boo","bob")
#print boyer("ababab","ab")
#print RBKG("12323142412345523123","123")
#print LCSn("agasddaswdfqbcd","abdfwaqfawefr")
#print max("affafaf","gwffasd")
#print "asddf"[:-1]

def LCS(X,Y):
	table = [[object for i in range(len(Y))] for j in range(len(X))]
	# 0 nothing 1 left 2 above 3 diagonal
	for i in range(len(table)):
		for j in range(len(table[i])):
			if i ==0 or j==0:
				table[i][j] = (0,0)
				continue
			if X[i]==Y[j]:
				table[i][j] = (table[i-1][j-1][0]+1,3)
			if X[i]!=Y[j] and table[i-1][j][0] >= table[i][j-1][0]:
				table[i][j] = (table[i-1][j][0],2)
			if X[i]!=Y[j] and table[i][j-1][0] >= table[i-1][j][0]:
				table[i][j] = (table[i][j-1][0],1)

	start = table[-1][-1]
	m = len(X)-1
	n = len(Y)-1
	string = ""
	while(m>0 and n>0):

		if table[m][n][-1] == 3:
			string+=X[m]
			m-=1
			n-=1
		if table[m][n][-1] == 2:
			m-=1
		if table[m][n][-1] == 1:
			n-=1

	return string

print LCS("dsdasd","asfgw")
print LCSn("dsdasd","asfgw")

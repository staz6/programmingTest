import sys
def func(n):
		# init case
		if n < 10:
			return n

		# convert number to list of integerer
		l = []
		for _,c in enumerate(str(n)):
			l.append(int(c))
		n = len(l)

		# right to left traversal,
		for i in range(n-1,0,-1):
			if l[i] < l[i-1]:
				l[i-1] -= 1
				for i in range(i,n):
					l[i] = 9
		
		return int("".join([str(x) for x in l]))

n = len(sys.argv)
if(n == 1):
	print("Argument is required, format python task2.py 322 ")
else:
	print(func(int(sys.argv[1])))
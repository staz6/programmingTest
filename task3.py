import matplotlib.pyplot as plt
import sys
def evaluate(string):
    string = string.replace(" ", "")

    def splitby(string, separators):

        lis = []
        current = ""
        for ch in string:
            if ch in separators:
                lis.append(current)
                lis.append(ch)
                current = ""
            else:
                current += ch
        lis.append(current)
        return lis

    lis = splitby(string, "+-")
    def evaluate_mul_div(string):
        lis = splitby(string, "*/")
        if len(lis) == 1:
            return lis[0]
        
        output = float(lis[0])
        lis = lis[1:]

        while len(lis) > 0:
            operator = lis[0]
            number = float(lis[1])
            lis = lis[2:]

            if operator == "*":
                output *= number

            elif operator == "/":
                output /= number

        return output

    
    for i in range(len(lis)):
        lis[i] = evaluate_mul_div(lis[i])

    output = float(lis[0])
    lis = lis[1:]

    while len(lis) > 0:
        operator = lis[0]
        number = float(lis[1])
        lis = lis[2:]

        if operator == "+":
            output += number
        elif operator == "-":
            output -= number

    return output

x='(5+8)*(3/8+3)'
def find_between(s, start, end):
	print('eval',s)
	eval=evaluate((s.split(start))[1].split(end)[0])
	output=str(int(eval)).join([s[:s.find(start)],s[s.find(end)+1:]])
	print('output',output)

	if output.find('(')==-1:
		print("not found")
	else:
		find_between(output,'(',')');
	result = evaluate(output)
	print(result)
	return result

# print(evaluate("1+2x3-4/5"))
input='(5+8)*3/8+x'
graphRange=10
lsy=[]
lsx=[]
n = len(sys.argv)
if(n == 1):
	print("Argument is required, format python task3.py '(5+8)*3/8+3' ")
else:	
	print("Range is set to 10")
	if(input.find('x')==-1):
			find_between(input,'(',')');
	else:
			
			for i in range(1,graphRange):
				lsy.append(i)
				lsx.append(find_between(input.replace('x',str(i)),'(',')'))
			print(lsy)
			print(lsx)
			plt.plot(lsx, lsy)

			plt.xlabel('x - axis')
			# naming the y axis
			plt.ylabel('y - axis')
			  
			# giving a title to my graph
			plt.title('task 3 graph')
			  
			# function to show the plot
			plt.show()
		



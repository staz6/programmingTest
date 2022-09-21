#!/usr/bin/python
import sys
# main evaluate function body
def evaluate(string):
    string = string.replace(" ", "")

    # use to split the equation according to the parameters give eg: splitby("3+2-3-2","+-") -> '3,+,2,-,3,-,2'
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
    # To evaluate whether + and divide
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

    # last +,i operation
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
# this will get the expression between (), pass it to evaluate and replace the output into the origin string
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

input='(5+8)*3/8+3'
n = len(sys.argv)
if(n == 1):
	print("Argument is required, format python task1-t.py '(5+8)*3/8+3' ")
else:
	try:
		input=str(sys.argv[1])
		if(input.find('(')==-1):
			print(evaluate(input))
		else:
			find_between(input,'(',')');
	except:
		print("")

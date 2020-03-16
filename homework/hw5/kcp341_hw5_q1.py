from ArrayStack import ArrayStack

def postfix():
    operators = "+-*/"
    stack = ArrayStack()
    while x!= 'done()':
        x = input("-->")
        if "=" in x:
            equalPosition = x.find('=')
            variable_name = ''
            for k in range(0, equalPosition-1):
                variable_name += x[k]
            for j in range(equalPosition+2,len(x)):
                if x[j] not in operators:
                    stack.push(int(x[j]))
                else:
                    operand_1 = stack.pop()
                    operand_2 = stack.pop()
                    if(j=='+'):
                        res = operand_2+operand_1
                    elif(j=='-'):
                        res = operand_2-operand_1
                    elif(j=='*'):
                        res = operand_2*operand_1
                    else:
                        res = operand_2/operand_1
                    stack.push(res)
        else:
            for i in x:
                if i not in operators:
                    stack.push(int(i))
                else:
                    operand_1 = stack.pop()
                    operand_2 = stack.pop()
                    if(i=='+'):
                        res = operand_2+operand_1
                    elif(i=='-'):
                        res = operand_2-operand_1
                    elif(i=='*'):
                        res = operand_2*operand_1
                    else:
                        res = operand_2/operand_1
                    stack.push(res)
            print(stack.pop())



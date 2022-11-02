
def calculator(input):
    operators = ["+","-","*","/","//","(",")"]
    math_Operators = set(operators)
    operators.clear() # save space
    # remove all white spaces, and make sure
    # input is converted to string to avoid input errors
    expression = str(input).replace(" ","")

    # check if input contains invalid math operator
    for s in expression:
        if s.isdecimal():
            continue
        if s not in math_Operators:
            print(f'Expression {expression} contains an invalid operation {s}')
            return
    math_Operators.clear() # save space
    parenthesis = [] 
    ans = []
    # parenthesis prioritized first
    stack = [] # helps with dealing with parenthesis
    if "(" in expression:
        for s,i in enumerate(expression):
            if s == "(":
                stack.append(s) #push into stack
            elif s == ")": #append the expression inside
                        # the parenthesis into a queue as a list
                        # and reset the stack
                parenthesis.append(stack[1::])
                stack.clear()
            elif "(" in stack: #push numbers and operations
                            # in between parenthesis
                stack.append(s)
        
        # evaluate expression in parenthesis
        
    print(parenthesis)
    op_func = {"**": expo, "*":mul, "/": div, "//": divInt,
            "+": add, "-":sub}
    #print(evaluate(parenthesis[0],op_func))

    return expression

def evaluate(input, op_func):
    queue = ["**","*","/","//","+","-"]
    q = []
    for op in queue:
        for i in range(len(input)):
            if op == input[i]:
                ans = op_func[op](int(input[i-1]),int(input[i+1]))
                input[i-1] = ans
                q.append(ans)
    return q

def expo(a, b):
    return a ** b
def mul(a ,b):
    return a * b
def div(a, b):
    return a / b
def divInt(a, b):
    return a // b
def add(a, b):
    return a + b
def sub(a, b):
    return a - b


    

print(calculator("(5+3*5**3)"))
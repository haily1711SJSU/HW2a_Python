
def calculator(input):
    operators = ["+","-","*","/","//","(",")"]
    math_operators = set(operators)
    operators.clear() # save space
    # remove all white spaces, and make sure
    # input is converted to string to avoid input errors
    expression = str(input).replace(" ","")

    # check if input contains invalid math operator
    for s in expression:
        if s.isdecimal():
            continue
        if s not in math_operators:
            print(f'Expression {expression} contains an invalid operation {s}')
            return
    input_list = []
    i = 0
    while i < len(expression):
        digit = ""
        while expression[i].isdigit() and i < len(expression)-1:
            digit += expression[i]
            i += 1
        input_list.append(digit)
        if expression[i] in math_operators:
            if expression[i]+expression[i+1] == "**":
                input_list.append(expression[i]+expression[i+1])
                i += 1
            elif expression[i]+expression[i+1] == "//":
                input_list.append(expression[i]+expression[i+1])
                i += 1
            else:
                input_list.append(expression[i])
        i += 1
        
    input_list[-1] += expression[-1]
    op_func = {"**": expo, "*":mul, "/": div, "//": divInt,
            "+": add, "-":sub}

    return evaluate(input_list, op_func)

def evaluate(input, op_func):
    queue = ["**","*","/","//","+","-"]
    q = []
    print(input)
    for op in queue:
        n = len(input)
        i = 0
        while i < n:
            if op == input[i]:
                left = int(input[i-1])
                right = int(input[i+1])
                ans = op_func[op](left,right)
                q.append(ans)
                for a in range(2):
                    input.pop(i)
                input.pop(i-1)
                input.insert(i-1, ans)
            n = len(input)
            i += 1
    return float(q[-1])

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


print(calculator("11/31"))

def calculator(input):
    # remove all white spaces, and make sure
    # input is converted to string to avoid input errors
    expression = str(input).replace(" ","")

    # check if input contains invalid math operator
    operators = ["+","-","*","/","//","(",")"]
    math_operators = set(operators)
    operators.clear() # save space
    for s in expression:
        if s.isdecimal():
            continue
        if s not in math_operators:
            print(f'Expression {expression} contains an invalid operation {s}')
            return

    # convert the string input into a list
    # for example "12+ 31 / 3" is converted into 
    # ['12', '+', '31', '/', '3']
    # each number is stored as one element
    # each math operation is stored as one element
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
    input_list[-1] += expression[-1] # edge case, append last element


    # create a dictionary that holds the keys that map to
    # all the math functions built in this program
    op_func = {"**": expo, "*":mul, "/": div, "//": divInt,
            "+": add, "-":sub}

    # calculate the list expression created above
    # and return a float as the answer
    return evaluate(input_list, op_func)

def evaluate(input, op_func):
    # Create a queue to mimic PEMDAS operations
    # For example, parenthesis is searched first, then exponents...
    # When a math operation is found, take the left and right 
    # elements and use the op_func to evaluate that 
    # expression. 
    # For example in ['12', '+', '31', '/', '3']
    # we search for '/' and take the left and right elements
    # 31 and 3 and evaluate 31 / 3
    # then pop all of those elements to get ['12', '+', '10.333334']
    # Append 10.333334 to a list [10.333334]
    # Finally do 12 + 10.333334 to get 22.0, list = [10.333334, 22]
    # return the last element of the list to get the answer
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


print(calculator("12+31 / 3 "))
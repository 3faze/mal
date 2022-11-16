def READ(string):
    return string

def EVAL(string):
    return string

def PRINT(string):
    return string

def rep(input):
    ast = READ(input)
    result = EVAL(ast)
    return PRINT(result) #Output

while True:
    inp = input("user> ")
    print(rep(inp))

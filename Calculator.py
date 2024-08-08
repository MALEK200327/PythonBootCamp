def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplaction(a,b):
    return a * b

def division(a,b):
    return a/b

operations = {
    "+":addition,
    "-":subtraction,
    "*":multiplaction,
    "/":division
}

print(operations["+"](4,5))
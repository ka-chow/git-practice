"def add(a, b):" 
"    return a + b" 
"def sub(a, b):" 
"    return a - b" 
def div(a, b): 
    if b == 0: 
        raise ValueError("Division by zero") 
    return a / b 
def pow(a, b): 
    return a ** b 
def mod(a, b): 
    return a % b 
def floor_div(a, b): 
    return a // b 

def factorial(x):
    if x == 0 or x == 1:
        return "1"
    
    result = 1
    expression = ""
    
    for i in range(x, 0, -1):
        result *= i
        expression += str(i)
        if i > 1:
            expression += "*"
    
    expression += "=" + str(result)
    
    return expression

x = int(input())

print(factorial(x))

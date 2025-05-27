def calc(op, i=0):
    result = i
    def operation(i):
        nonlocal result
        if op == "+":
            result += i
        elif op == "-":
            result -= i
        elif op == "*":
            result *= i
        elif op == "/":
            result /= i
        print(result)
        return result
    return operation

test=calc("*",i=1)

test(5)

test(2)
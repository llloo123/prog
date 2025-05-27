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


def povtor(kol):
    def decorator(step):
        def schet(*args, **kwargs):
            result = []
            for _ in range(kol):
                result.append(step(*args, **kwargs))
            return result
        return schet
    return decorator



while (True):
    kol=int(input("введите кол. повторений (0 для заверешения) "))
    if kol==0:
        break

    op=input("введите операцию ")

    i=int(input("введите начальное число "))

    forstep=int(input("введите переменную для шага "))
    test = calc(op, i)

    @povtor(kol)
    def step(forstep):
        return test(forstep)

    print(step(forstep)) 
def calc_x_iterative(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1/8
    else:
        x_values = [1, -1/8]
        for i in range(3, n + 1):
            next_x = ((i - 1) * x_values[-1]) / 3 + ((i - 2) * x_values[-2]) / 4
            x_values.append(next_x)
        return x_values[-1]
print(calc_x_iterative(3))
print(calc_x_iterative(7))
def calc_x(i):
    if i == 1:
        return 1
    elif i == 2:
        return -1/8
    else:
        return ((i - 1)*calc_x(i - 1)) / 3 + ((i - 2)*calc_x(i - 2)) / 4
print(calc_x(3))
print(calc_x(7))
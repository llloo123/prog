def count_iterative(data):
    count = 0
    stack = [data] 
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current)  
        else:
            count += 1
    return count
print(count_iterative(["x", "y", ["z"]])) 
print(count_iterative([1, 2, [3, 4, [5]]])) 

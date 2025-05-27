def count_recursive(data):
    count = 0
    if isinstance(data, list):
        for item in data:
            count += count_recursive(item) + 1 
        return count
    else:
        return 1  
print(count_recursive([]))      
print(count_recursive([1, 2, 3]))  
print(count_recursive(["x", "y", ["z"]]))
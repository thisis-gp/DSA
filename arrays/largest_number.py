def largest_ele(arr):
    max_element = float('-inf')
    for i in arr:
        if i>max_element:
            max_element = i
    return max_element

print(largest_ele([1,23,4,5,6]))
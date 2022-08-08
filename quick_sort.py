def quick_sort(data):
    left = []
    right = []

    if len(data) <= 1:
        return data

    pivot = data[0]
    pivot_count = 0

    for ele in data:
        if ele < pivot:
            left.append(ele)
        elif ele > pivot:
            right.append(ele)
        else:
            pivot_count += 1
        
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [pivot] * pivot_count + right

data = [9, 8, 4, 1, 5, 3, 2 ,6, 7]
print(quick_sort(data))

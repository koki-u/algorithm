def heap_sort(data):
    i = 0
    n = len(data)

    while i < n:
        upheap(data, i)
        i += 1

    while i > 1:
        i -= 1
        data[0], data[i] = data[i], data[0]

        downheap(data, i-1)

    return data

def upheap(data, n):
    while n:
        parent = int((n-1) / 2)
        if data[parent] < data[n]:
            data[n], data[parent] = data[parent], data[n]
            n = parent
        else:
            break

def downheap(data, n):
    if n==0:
        return data
    
    parent = 0
    while True:
        child = 2 * parent + 1
        if child > n:
            break
        if child < n and data[child] < data[child + 1]:
            child += 1
        
        if data[parent] < data[child]:
            data[child], data[parent] = data[parent], data[child]

            parent = child
        else:
            break

data = [9, 8, 4, 1, 5, 3, 2 ,6, 7]
print(heap_sort(data))
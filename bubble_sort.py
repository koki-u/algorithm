def bubble_sort(data):
    change = True

    for i in range(len(data)):
        for j in range(len(data) - i -1):
            if data[j] > data[j+1]:
                 data[j], data[j+1] = data[j+1], data[j]

    return data

a = [1, 2, 4, 9, 2]
print(bubble_sort(a))

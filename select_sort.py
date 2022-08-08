def select_sort(data):
    for i in range(len(data)):
        Min = i
        for j in range(i+1, len(data)):
            if data[j] < data[Min]:
                Min = j

        data[i], data[Min] = data[Min], data[i]

    return data

data = [9, 8, 4, 1, 5, 3, 2 ,6, 7]
print(select_sort(data))
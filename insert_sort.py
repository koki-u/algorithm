def insert_sort(data):
    for i in range(1, len(data)):
        j = i - 1
        sorted_list = data[i]
        while data[j] > sorted_list and j >= 0:
            data[j+1] = data[j]
            #整列済みの末尾のリストから比較
            j -= 1
        data[j+1] = sorted_list
    return data

data = [9, 8, 4, 1, 5, 3, 2 ,6, 7]
print(insert_sort(data))
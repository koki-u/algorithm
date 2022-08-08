from heapq import merge


def merge_sort(data):
    if len(data) <= 1:
        return data

    #分割
    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    #分割を再帰的におこなう
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged

data = [9, 8, 4, 1, 5, 3, 2 ,6, 7]
print(merge_sort(data))

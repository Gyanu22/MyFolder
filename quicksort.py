l = [x for x in range(1000,3,-1)]

def sort(arr):
    return arr if arr == [] else sort([x for x in arr[1:] if x < arr[0]]) + [arr[0]] + sort([x for x in arr[1:] if x >= arr[0]])

print(sort(l))
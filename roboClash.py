def roboClash(arr):
    n = len(arr)
    indices = list(range(n))
    indices.sort(key=lambda x: arr[x])
    print(indices)
    right, prefix = 0, 0
    for i in range(n):
        if prefix < arr[indices[i]]:
            right = i
        prefix += arr[indices[i]]
    res = [ind+1 for ind in indices[right:]]
    return res

arr = [ 1, 6, 2, 2, 7 ]
val = roboClash(arr)
print(val)

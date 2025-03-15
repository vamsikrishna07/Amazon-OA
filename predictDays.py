def predictDays(arr, k):
    n = len(arr)
    if n < 2 * k + 1:
        return []
    left = [1] * n
    for i in range(1, n):
        if arr[i - 1] >= arr[i]:
            left[i] = left[i - 1] + 1
    right = [1] * n
    for i in range(n - 2, -1, -1):
        if arr[i] <= arr[i + 1]:
            right[i] = right[i + 1] + 1
    result = []
    for i in range(k, n - k):
        if left[i] >= k + 1 and right[i] >= k + 1:
            result.append(i+1)
    return result

arr = [ 4, 3, 2, 2, 3, 4]
k = 2
val = predictDays(arr, k)
print(val)
def bucket_sort_std(arr):
    n = len(arr)
    if arr:
        max_val = max(arr)
    else:
        max_val = 1
    b = []
    for i in range(n):
        b.append([])

    for i in range(n):
        bi = arr[i] // max_val
        b[bi].append(arr[i])

    for i in range(n):
        b[i].sort()

    arr.clear()
    for i in range(n):
        for j in range(len(b[i])):
            arr.append(b[i][j])


def bucket_sort(arr):
    Neg = []
    Pos = []

    for i in range(len(arr)):
        if arr[i] < 0:
            Neg.append(-1 * arr[i])
        else:
            Pos.append(arr[i])

    bucket_sort_std(Neg)
    bucket_sort_std(Pos)

    for i in range(len(Neg)):
        arr[i] = -1 * Neg[len(Neg) - 1 - i]

    for i in range(len(Neg), len(arr)):
        arr[i] = Pos[i - len(Neg)]

    return arr

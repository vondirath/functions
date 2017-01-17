def checklca(r, n1, n2):
    if n1 < r > n2 and n2 > n1:
        return r
    if n2 < r > n1 and n1 > n2:
        return r


def question4(T, r, n1, n2):
    if r == None or r == n1 or r == n2:
        return r
    if n1 <= r and r <= n2 or n2 <= r and r <= n1:
        return r

    count = 0
    for index in T[r]:
        if index == 0:
            count += 1
        if index == 1:
            r = count
            return checklca(r, n1, n2)
        
    

matrix1 = [[0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 0, 0, 0, 1],
          [0, 0, 0, 0, 0]]

matrix2 = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0],
          [0, 0, 0, 1, 0]]

matrix3 = [[0, 0, 0, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 1, 1, 0, 0]]

print question4(matrix1, 3, 1, 4)
print question4(matrix1, 3, 4, 1)
print question4(matrix2, 4, 1, 2)
print question4(matrix3, 0, 1, 2)

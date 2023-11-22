import numpy

a = [[1,2,3],
    [4,5,6],
    [7,8,9]]
print("a =", a)
print("a[1] = ", a[1])
print("a[1][2]=", a[1][2])
print("a[0][-1]=", a[0][-1])

column = []
for row in a:
    column.append(row[2])

print("3rd column =", column)

x = [[1,1,1],[1,1,1],[1,1,1]]
y = [[1,2,3],[4,5,6],[7,8,9]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

print("x =", x)
print("y =", y)

print("x + y =")
for r in result:
    print(r)

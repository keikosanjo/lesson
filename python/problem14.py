list = []
def collatz(n):
    N = n
    while n > 1:
        if n%2 == 0:
            list.append(int(n/2))
            n = int(n/2)
        elif n%2 != 0:
            list.append((3*n)+1)
            n = ((3*n)+1)
    list.insert(0, N)

listLength = 0
listValue = 0
print(len(list))
for x in range(0, 1000000):
    collatz(x)
    if len(list) >= listLength:
        listLength = len(list)
        listValue = x
print('最長の数列を生成する値：{0}'.format(listValue))
print('数列の長さ：{0}'.format(listLength))

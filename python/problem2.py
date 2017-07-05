Sum = 0
Fib = [1 , 2]
max = 4000000

## フィボナッチ数列作成
i = 1
while (Fib[i] <= max):
    if i == 1:
        Fib[i] = 2
    elif i == 2:
        Fib.append(Fib[0] + Fib[1])
    elif i == 3:
        Fib.append(Fib[1] + Fib[2])
    else:
        Fib.append(Fib[i-1] + Fib[i-2])
print(Fib)

## 偶数値の項の総和
for i in range(0, len(Fib) - 1):
    if Fib[i] % 2 == 0:
        Sum += Fib[i]
print('偶数値の合計= %s' %Sum)

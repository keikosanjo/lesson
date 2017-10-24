def collatz(n):
    list = []
    list.append(n)
    while n == 1:
        if n%2 == 0:
            list.append(n%2)
            n = n%2
        elif n%2 != 0:
            list.append((3*n)+1)
            n = (3*n)+1
    print(list)
collatz(13)


Number = 600851475143
answer = 0

for num in range(1, Number):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        #print(num)
        if Number % num == 0:
            answer = num
print(answer)

count = 0
num = 0
while count < 20:
    num += 1
    count = 0
    for i in range(1,21):
        if num % i == 0:
            count += 1
print(num)

count = 1
divisor = 0
while divisor < 500:
    triangleNumber = 0
    for i in range(0, count + 1):
        triangleNumber += i
        divisor = 0
        for divideNumber in range(1, triangleNumber + 1):
            if triangleNumber % divideNumber == 0:
                divisor += 1
    count += 1
print(triangleNumber)

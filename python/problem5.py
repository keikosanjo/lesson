count = 0
for num in range(1,100000):
    for i in range(1,21):
        if((num/i) == 0):
            count += 1
            if(count == 20):
                print(num)


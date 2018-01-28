def calculate_reciprocal_number(d):
    array = []
    i = 0
    x = 1%d
    array.append(x)
    loop = True
    while(loop):
        x = (array[i]*10)%d
        if x == 0:
            array.clear()
            array.append(0)
            break
        elif x != 1:
            if x == array[i-1]:
                array.clear()
                array.append(0)
                break
            else:
                array.append(x)
        elif x == 1:
            break
        i += 1
    return(int(len(array)))

digit_number = []
for d in range(1,1000):
    digit_number.append(calculate_reciprocal_number(d))
number = max(digit_number)
d =  digit_number.index(number)
answer = d+1
print(answer)

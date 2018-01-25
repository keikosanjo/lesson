def calculate_reciprocal_number(d):
    array = []
    x = 0
    i = 0
    while x != 1:
        x = (array[i]*10)%d
        array.append(x)
        i += 1
    return(int(len(array)-1))

digit_number = []
for d in range(1,8):
    a = calculate_reciprocal_number(d)
    digit_number.append(a)
number = max(digit_number)
d =  digit_number.index(number)
print('d:{0}, number of digits:{1}',format(d,number))


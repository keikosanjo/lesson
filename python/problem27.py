def calcurate_divisor(number):
    count = 0
    for i in range(1,number+1):
        if number%i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

max_array = [ 0 ]
def calcurate_divisor_numbers(a,b):
    flag = 0
    i = 0
    while flag == 0:
        calcurate_result = (i*i) + (a*i) + b
        if calcurate_divisor(calcurate_result) == False:
            if max_array[0] < i-1:
                max_array.clear()
                max_array.append(i-1)
                max_array.append(a)
                max_array.append(b)
                flag = 1
        else:
            i += 1
for a in range(-999,1000):
    for b in range(-1000,1001):
        calcurate_divisor_numbers(a,b)
print(max_array)

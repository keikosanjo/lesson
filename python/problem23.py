def sum_of_true_divisor(number):
    total = 0
    for i in range(1,number):
        if number%i == 0:
            total += i
    return(total)

#print(sum_of_true_divisor(28))
for i in range(1,28123):
    if sum_of_true_divisor(i) > i:

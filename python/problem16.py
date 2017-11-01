from math import pow
def sum_of_number(x):
    number = int(pow(2,x))
    sum_of_number = list(str(number))
    int_list = map(int, sum_of_number)
    return(sum(int_list))

print(sum_of_number(1000))

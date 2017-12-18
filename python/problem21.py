def sum_divisor_list(num):
    list = []
    for i in range(1,num+1):
        if num % i == 0:
            list.append(i)
    list.remove(num)
    return sum(list)

result_list = []
def amicable_numbers(result):
    list = []
    a = sum_divisor_list(result)
    if sum_divisor_list(a) == result:
        result_list.append(result)

for i in range(2,10000):
    amicable_numbers(i)
print(sum(result_list))

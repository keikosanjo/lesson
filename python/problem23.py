def sum_of_true_divisor(number):
    total = 0
    for i in range(1,number):
        if number%i == 0:
            total += i
    return(total)

list = []
def judge_sum_of_divisor(N):
    for i in list:
        if i > N/2:
            break
        if N-i in list:
            return True
    return False

for i in range(1,28123):
    if sum_of_true_divisor(i) > i:
        print(i)
        list.append(i)

total = 0
for i in range(1,28123):
    if judge_sum_of_divisor(i) == False:
        total += i
print(total)

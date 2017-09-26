def sum_of_prime_number(limit):
    sum = 0
    for num in range(1,limit+1):
        count = 0
        for i in range(1,num+1):
            if num% i == 0:
                count += 1
        if count == 2:
            sum += num
    print(sum)
sum_of_prime_number(2000000)

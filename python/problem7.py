def prime_number(num):
    count = 0
    number = 1
    division_count = 0
    while count < num:
        number += 1
        division_count = 0
        for i in range(1,number+1):
            if number%i == 0:
                division_count += 1
        if division_count == 2:
            count += 1
    print(number)

prime_number(10001)

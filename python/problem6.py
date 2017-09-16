number_of_squaring_of_sum = 0
number_of_sum_of_squares = 0
for i in range(1,101):
    number_of_sum_of_squares += i*i
    number_of_squaring_of_sum += i
number_of_squaring_of_sum = number_of_squaring_of_sum * number_of_squaring_of_sum

print(number_of_squaring_of_sum - number_of_sum_of_squares)

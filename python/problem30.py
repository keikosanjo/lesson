def calculate_sum_of_fifth_powers_of_digits(number):
    digit_number_list = list(str(number))
    number = [ pow(int(digit_number_list[i]),5)  for i in range(0,len(digit_number_list))]
    sum_result = sum(number)
    return sum_result

match_list = [ i  for i in range(2,1000000) if i == calculate_sum_of_fifth_powers_of_digits(i)]
print(match_list)
print("Result:%d" %sum(match_list))

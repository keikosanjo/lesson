def factorial(number):
    result = 1
    for i in range(number, 0, -1):
        result = result*i
    return(result)

def sum_of_the_figures_of_each_rank(factorial_result):
    str_number = str(factorial_result)
    sum_list = list(str_number)
    int_list = map(int , sum_list)
    result = (sum(int_list))
    print(result)

sum_of_the_figures_of_each_rank(factorial(100))

number_list = [pow(a,b) for b in range(2,101) for a in range(2,101)]
number_list_uniq = list(set(number_list))
print(len(number_list_uniq))

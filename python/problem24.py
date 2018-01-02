import itertools

element_list = ('0','1','2','3','4','5','6','7','8','9')

list(itertools.permutations(element_list))
print(list(itertools.permutations(element_list))[1000000])


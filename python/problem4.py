list = []
for num1 in range(100, 1000):
    for num2 in range(100, 1000):
       count = 0
       value = num1 * num2
       str_value = str(value)
       for i in range(0, int(len(str_value)/2)):
           #print(value)
           if(str_value[i] == str_value[len(str_value)-1-i]):
               count += 1
               if(count==3):
                   list.append(value)
list.sort()
print(list[len(list)-1])

for num1 in range(100, 999):
    for num2 in range(100, 999):
       value = num1 * num2
       str_value = str(value)
       for i in range(0,len(str_value)):
           print( str_value[0] )

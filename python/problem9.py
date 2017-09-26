def calculate_number_pythagoras(number):
    for m in range(1000):
        for n in range(1000):
            a = (m*m)-(n*n)
            b = 2*m*n
            c = (m*m)+(n*n)
            if (a*a) + (b*b) == c*c:
                if a + b + c == number and a >= 0 and b >= 0 and c >= 0:
                    print(a*b*c)

calculate_number_pythagoras(1000)

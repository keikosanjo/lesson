def calculate_diagonal_numbers(N):
    answer = 1
    for i in range(3, N+1, 2):
        for j in range(4):
            answer += ( i * i ) - ( i - 1 ) * j
    return(answer)

print(calculate_diagonal_numbers(1001))


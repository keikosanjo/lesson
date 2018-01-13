F = [1,1]

x = 1
def cal_fibonacci(N):
    F_N = F[N-2] + F[N-3]
    F.append(F_N)

data_size = True
i = 2
while data_size:
    i += 1
    cal_fibonacci(i)
    if len(str(F[i-1])) == 1000:
        data_size = False
print('answer:{0}'.format(i))

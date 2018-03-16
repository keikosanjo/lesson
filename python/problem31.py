import itertools

coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]

coin_list = [ c for c in itertools.combinations_with_replacement(coins, 200) if sum(c)== 200 ]
print(len(coin_list))

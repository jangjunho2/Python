cash_input = int(input())

coins = [500, 100, 50, 10]
coin_count = 0
for coin in coins:
    coin_count += cash_input//coin
    cash_input %= coin

print(coin_count)

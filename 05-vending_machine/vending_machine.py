usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

def get_change(amount, coins=eur_coins):
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)

    return change
def payment_check():
    pass

all_sets_prices = []


amount_of_sets = int(input())

for set in range(amount_of_sets):

    price_and_amount = {}
    amount_of_items = int(input())
    prices = [int(i) for i in input().split(' ')]

    for item in prices:
        if item not in price_and_amount:
            all_sets_prices.append(item*(prices.count(item)//3*2 + prices.count(item)%3))
            price_and_amount[item] = prices.count(item)

    #all_sets_prices.append(price_and_amount)

for set in all_sets_prices:
    print(set)
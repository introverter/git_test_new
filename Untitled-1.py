def can_be_splitted(text: str):
    if text[0].isdigit() or len(text) < 4 or not text[-2:].isalpha():
        return '-'
    return '+'


def main():
    results = []
    amount_of_line = int(input())

    for _ in range(amount_of_line):
        new_line = input()
        results.append(can_be_splitted(new_line))

    for item in results:
        print(item)


if __name__ == '__main__':
    main()

amount_of_sets = int(input())
all_sets_prices = [0 for i in range(amount_of_sets)]

for set in range(amount_of_sets):

    price_and_amount = {}
    amount_of_items = int(input())
    prices = [int(i) for i in input().split(' ')]

    for item in prices:
        if item not in price_and_amount.keys():
            all_sets_prices[set] += item*(prices.count(item)//3*2 + prices.count(item)%3)
            price_and_amount[item] = prices.count(item)


for set in all_sets_prices:
    print(set)
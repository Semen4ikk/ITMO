with open('input.txt') as file:
    value_of_ads = int(file.readline())
    cost_of_ad = list(map(int, file.readline().split()))
    value_of_clicks = list(map(int, file.readline().split()))

    cost_of_ad.sort()
    value_of_clicks.sort()

def find_max_profit(value_of_ads, cost_of_ad, value_of_clicks):
    profit = 0

    for i in range(value_of_ads):
        profit += cost_of_ad[i] * value_of_clicks[i]

    return profit

profit = find_max_profit(value_of_ads, cost_of_ad, value_of_clicks)
f = open('output.txt', 'w')
f.write(str(profit))
def get_price(percent, price):
    return round(price * ( 1 + percent / 100), 2)

prices_now = []
for _ in range(5):
    price = float(input('Цена на товар: '))
    prices_now.append(price)

first_percent = int(input('Повышение на первый год:'))
second_percent = int(input('Повышение на второй год:'))

price_first = [get_price(first_percent, i_price) for i_price in prices_now]
price_second = [get_price(second_percent, i_price) for i_price in price_first]

print('Сумма цен за каждый год:', round(sum(prices_now), 2), round(sum(price_first), 2), round(sum(price_second), 2))
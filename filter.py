item_prices = [120, 99, 45, 67, 102, 80, 111, 30 ]

def filter_high_prices(prices, threshold):
    expensive_items = []

    for price in prices:
        if price >= threshold:
           expensive_items.append(prices)
        
    return expensive_items

result = filter_high_prices(item_prices,100)
print(result)            
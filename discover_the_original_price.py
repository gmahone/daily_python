def discover_original_price(discounted_price, sale_percentage):
    sale_decimal = sale_percentage/100
    print(sale_decimal)
    price_decimal = 1 - sale_decimal
    print(price_decimal)
    result = discounted_price/price_decimal
    print(result)
    rounded_result = round(result, 2)
    return rounded_result

def discover_original_price(discounted_price, sale_percentage):
    sale_decimal = sale_percentage/100
    price_decimal = 1 - sale_decimal
    result = discounted_price/price_decimal
    rounded_result = round(result, 2)
    return rounded_result


# short solution
def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / ((100 - sale_percentage) * 0.01), 2)

# alternative short solution
def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price/(1-sale_percentage/100),2)

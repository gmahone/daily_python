def html_special_chars(data):
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    data = data.replace('"', '&quot;')
    return data

# using dict
def html_special_chars(data): 
    symbols = {'<': '&lt;', '>': '&gt;', '"': '&quot;', '&': '&amp;'}
    return "".join(symbols.get(x, x) for x in data)

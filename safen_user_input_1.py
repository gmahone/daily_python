def html_special_chars(data):
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    data = data.replace('"', '&quot;')
    data = data.replace("&", "&amp;")
    return data

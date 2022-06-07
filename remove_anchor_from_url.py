def remove_url_anchor(url):
    return url.split("#")[0]

# other solutions

# using partition
def remove_url_anchor(url):
  return url.partition('#')[0]

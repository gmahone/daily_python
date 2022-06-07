def remove_url_anchor(url):
    return url.split("#")[0]

# other solutions

# using partition
def remove_url_anchor(url):
  return url.partition('#')[0]

# regex solution
def remove_url_anchor(url):
  import re
  return re.sub('#.*$','',url)

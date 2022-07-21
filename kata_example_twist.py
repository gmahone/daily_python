websites = ["codewars"]*1000

# add solution using range
websites = ['codewars' for _ in range(1000)]

# add solution using loop
websites = []
for index in range(0,1000):
    websites.append("codewars")

# add solution using split    
websites = "codewars " * 1000
websites = websites.split()
print(websites)

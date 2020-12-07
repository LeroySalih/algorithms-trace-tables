h = 0
index = 0
items= [3, 5, 1, 2]

while index < len(items):
    if items[index] > h:
        h = items[index]
    index = index + 1

print ("h is ", h)

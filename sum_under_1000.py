i = 1
added = 0

while i < 1000:

    if i % 2 == 0 or i % 3 == 0:
        added += i

    i += 1


print(added)

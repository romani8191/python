with open("resume", 'r') as fp:
    count = 0
    for line in fp:
        if line != "\n":
            count += 1
print('Total Lines', count)
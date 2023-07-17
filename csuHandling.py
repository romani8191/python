with open ('records','r') as rec:
    display=rec.readlines()
for line in display:
    indi=line.split()
print(max(indi[3]))



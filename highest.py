a={
    'toothpaste':121,
    'burger':97,
    'bread':150,
    'dryer':780,
    'iron':500,
    'hair mask':1000
}

highest=max(a,key=a.get)
value=max(a.values())
print(f'Item of highest value is {highest}')
print(f'The value of the item is {value}')



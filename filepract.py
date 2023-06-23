with open('file1.txt','r') as f:
	data=f.read()
	char=data.split()
total=0
vovel=['a','e','i','o','u']


for char in data:
	if char in vovel:
		total+=1
f.close()

print(f'total no. of vovels are: {total}')






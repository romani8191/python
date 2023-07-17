import requests
import json

response = requests.get('https://fakestoreapi.com/products')
print (response.text)

sum=0
max=0
index=""
data = json.loads(response.text)
for host in data:
    title = host.get("title")
    price = host.get("price")
    print("Title",title,"Price",price)
    sum=sum+price
    if(max<price):
      max=price
      index=host
print("Total price=",sum)

print("Highest priced product=",index.get("title"),index.get("price"))



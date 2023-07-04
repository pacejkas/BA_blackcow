import json

filename = "Order History.json"
fid = open(filename, "r", encoding='utf-8')
data = json.load(fid)

n = len(data) # total number of data set
game = "블루 아카이브" # name of item purchase I am looking for
amount = [] # 

for i in range(0,n-1):
    if game in data[i]["orderHistory"]["lineItem"][0]["doc"]["title"]:
        #price = float(data[i]["orderHistory"]["totalPrice"][3:])*100 # express in cents
        price = float(data[i]["orderHistory"]["totalPrice"][3:])
        amount.append(price)

#totalAmount = sum(amount)/100 # divide by 100 to convert cents to dollars
totalAmount = sum(amount)

print("블루 아카이브에 총 ${:.2f} 씀".format(totalAmount))

fid.close()

#Assignment 7 #1
sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  
profit = (sales["sell_value"] - sales["cost_value"])*sales["inventory"]
print(round(profit))


#Assignment 7 #2
money = float(input("How much?"))
print("${:0.2f}".format(money)) #:0.2f kısmını internetten bulup yazdığım kodda kullandım.
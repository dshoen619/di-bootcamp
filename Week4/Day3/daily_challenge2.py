options=[]

items_purchase = {
  "Water": "$10",
  "Bread": "$300",
  "TV": "$1000",
  "Fertilizer": "$20"
}

wallet = "$1"

wallet_amount= int(wallet.lstrip("$"))

for i in items_purchase:
    dollar_amt=int(items_purchase[i].lstrip('$'))
    if dollar_amt<=wallet_amount:
        options.append(i)

if len(options)>0:
    print(options)
else:
    print("Nothing")

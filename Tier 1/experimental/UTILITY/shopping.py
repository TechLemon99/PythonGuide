sale_items = ["apple", "eggs", "milk", "bread", "muesli bar"]
user_shopping_list = ["eggs", "chicken nuggets", "monster energy zero ultra", "muesli bar"]

for i in user_shopping_list:
    if i in sale_items:
        print(f"{i} is on sale!")
    else:
        print(f"{i} is not on sale.")
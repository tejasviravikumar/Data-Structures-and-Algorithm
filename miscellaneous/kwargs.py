def groceries(**kwargs):
    # kwargs = {'apples': 2, 'mango': 5, 'kiwi': 10}
    Total_price = 0
    for price in kwargs.values():
        Total_price += price

    return Total_price
print(groceries(apples = 2 , mango = 5 , kiwi = 10))


# when we declare **kwargs at function definition it will pack the values
# if we declare **kwargs during function call it will unpack
# **kwargs is just a  common naming convention but we can use any variable to declare keywordarguments(kwargs)


def show_details(item_name , cp , sp):
    print(f"Item name:{item_name} |Cost Price:{cp} |Selling Price:{sp}")

info = {"item_name": "Banana", "cp":20 , "sp":16}
show_details(**info)
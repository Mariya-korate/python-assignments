my_cart = ["apples", "bananas", "milk"]
print(my_cart)
my_cart.append("bread")
print(my_cart)
my_cart.insert(0,"ketchup")
print(my_cart)
my_cart.remove("bananas")
print(my_cart)
removed_item=my_cart.pop(-1)
print(removed_item)
my_cart.extend(["rice", "butter"])
print(my_cart)
my_cart.sort()
print(my_cart)
my_cart.reverse()
print(my_cart)
my_cart_One = ["juice", "jam"]
new_cart=my_cart+my_cart_One
print(new_cart)
print(new_cart * 2)
str="tomato cucumber spinach"
str_one=str.split()
print(list(str_one))

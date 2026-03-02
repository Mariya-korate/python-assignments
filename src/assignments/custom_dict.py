customer_dict= {
    'name' : "John Doe",
    'age' : 32,
    'city' : "New York"
}
print(customer_dict)
customer_dict.update({'email': "johndoe@gmail.com"})
customer_dict.update({'phone': 856789})
print(customer_dict)
print(customer_dict.get('name'), customer_dict.get('city'))
del customer_dict['age']
print(customer_dict)
print(customer_dict.keys())
print(customer_dict.values())
print(customer_dict.items())
customer_dict.popitem()
print(customer_dict)
print(customer_dict.get("membership")) #Output: None
customer_dict["address"]="221B Baker Street"
print(customer_dict)

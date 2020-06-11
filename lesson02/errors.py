user = {"name": "Jphn"}

try:
    print(user["age"])
except KeyError:
    print("Invalid key!")

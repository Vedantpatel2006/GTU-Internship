dict_1 = {
    "key": 1,
    20: "value",
    "key1": [1, 2, 3],
    "key2": [5, 6, 7]
}

print(type(dict_1))
print(dict_1)

dict_1.update({"AQI": [101, 200, 300]})
print("After Update:", dict_1)

print("Items:", dict_1.items())
print("Keys:", dict_1.keys())
print("Values:", dict_1.values())

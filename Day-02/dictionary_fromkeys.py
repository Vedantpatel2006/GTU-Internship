keys_list = ["names", "rollno", "stream"]

print(type(keys_list))

names_list = ["GJ", "MH", "RJ"]
roll_list = [1, 11, 111]

dictb = dict.fromkeys(keys_list)

print(dictb)

dictb["names"] = names_list
dictb["rollno"] = roll_list
dictb["stream"] = ["DS", "CS", "EC"]
dictb["city"] = [1, 2, 3]

dictb.update({"AQI": [101, 200, 300]})

print(dictb)

print(dictb.items())
print(dictb.keys())
print(dictb.values())

oxford = {
    "Sad": "Misery",
    "Happiness": "Elation",
    "Anger": "Wrath"
}

print(type(oxford))
print(oxford)

oxford.update({"Fear": "Dread"})

print(oxford)

print(oxford.items())
print(oxford.keys())
print(oxford.values())

mylist = [
    "hasan",
    "khalid",
    "Farida",
    "mohamed",
    "jawad",
    "Lamiae",
    "Sanae",
    "Jihad",
    "no3man"
]
girls = []
boys = []
for name in mylist:
    if name.istitle():
        girls.append(name)
    else:
        boys.append(name)

print(girls)
print(boys)

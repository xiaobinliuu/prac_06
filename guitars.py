from guitar import Guitar

guitars = []
print("My guitars !")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = input("Cost: ")
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}),  worth ${cost}")
    name = input("Name: ")
print("These are my guitars: ")

for i, guitar in enumerate(guitars):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    print(f"Guitar {i + 1}: {guitar.name:15} ({guitar.year}) $ {guitar.cost:6} {vintage_string}")

from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added")
    name = input("Name: ")
print("\n... snip ...\n\nThese are my guitars: ")
for i, guitar in enumerate(guitars):
    print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{Guitar.is_vintage(guitar)}")

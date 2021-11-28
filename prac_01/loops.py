# 1)
for i in range(1,21,2):
    print(i, end=" ")
print()

# a)
for i in range(0, 101, 10):
    print(i, end=" ")
print()

# b)
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c)
# number_of_stars = int(input("How many stars? "))
# for i in range(1, number_of_stars + 1, 1):
#     print("*", end='')

# d)
stars_number = int(input("How many stars? "))
for i in range(1, stars_number + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
    
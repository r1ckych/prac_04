OUTPUT_FILE = "name.txt"

out_file = open(OUTPUT_FILE, "w")

name = input("What is your name? ")
out_file.write(name)
out_file.close()
out_file_read = open(OUTPUT_FILE, "r")
print_file = out_file_read.read()
print(f"Your name is {print_file}")

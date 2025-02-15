print("Open the file in read mode")
# Open the file in read mode
file = open("Profile.txt", "r")
# Read the entire content of the file
content = file.read()
# Print the content
print(content)
# Close the file
file.close()

# Open the file in read mode
file = open("Profile.txt", "r")
# Read each line one by one
for line in file:
    print(line.strip())  # .strip() to remove newline characters
# Close the file
file.close()

# Open the file in read mode
file = open("Profile.txt", "r")
# Read the first line
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()  # Read the next line
# Close the file
file.close

# Open the binary file in read binary mode
file = open("Profile.txt", "rb")
# Read the entire content of the file
content = file.read()
# Print the content (this will be in bytes)
print(content)
# Close the file
file.close()

# Open the file in read mode
file = open("Profile.txt", "r")
# Read the first 10 bytes
content = file.read(10)
print(content)
# Close the file
file.close()

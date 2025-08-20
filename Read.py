#File Read & Write Challenge
file = open("schedule_2025.pdf", "r") # Open the file in read mode

# Read the content of the file
content = file.read()
print(content)  # Print the content to verify
file.close()  # Close the file after reading



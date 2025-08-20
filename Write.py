# Open the file in write mode
file = open("schedule_2025.pdf", "w")  # Open the file in write mode

# Write new content to the file
file.write("Year 2025 Schedule\n")
file.write("January: New Year Celebration\n")
file.write("February: Valentine's Day\n")
file.write("March: Spring Festival\n")
file.write("April: Earth Day\n")
file.write("May: Labor Day\n")
file.write("June: Summer Solstice\n")
file.write("July: Independence Day\n")
file.write("August: Back to School\n")
file.write("September: Autumn Equinox\n")
file.write("October: Halloween\n")
file.write("November: Thanksgiving\n")
file.write("December: Winter Holidays\n")
file.close()  # Close the file after writing
# Open the file in read mode to verify the new content
file = open("schedule_2025.pdf", "r")  # Open the file in read mode

# Read the content of the file
content = file.read()  # Read the content of the file
print(content)  # Print the content to verify
file.close()  # Close the file after writing
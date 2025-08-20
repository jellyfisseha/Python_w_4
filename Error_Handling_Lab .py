file = None
try:
    file = open("sample", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    if file:
        file.close()
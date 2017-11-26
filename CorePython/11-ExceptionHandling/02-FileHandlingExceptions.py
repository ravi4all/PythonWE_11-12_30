try:
    file = open("file_1.txt")
    data = file.read()
    print(data)
    file.seek(0,1,2)

except FileNotFoundError as err:
    print("Error...",err)

finally:
    print("File closed...")
    file.close()

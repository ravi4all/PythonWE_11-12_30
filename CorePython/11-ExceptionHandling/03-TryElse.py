try:
    file = open("file_1.txt")
    data = file.read()
    print(data)
    file.seek(0,1,2)

except BaseException as err:
    print("Error...",err)

else:
    print("Inside Else")

finally:
    print("File closed...")
    file.close()

try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    c = a/b
    print(c)
    print("Output is",c)

except BaseException as err:
    print("Error...",err)

# except ZeroDivisionError as err:
#     print("Error...",err)

print("Hello world")

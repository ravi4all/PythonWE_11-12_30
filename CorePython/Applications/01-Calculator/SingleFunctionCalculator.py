def calc(ch,x,y):

    if ch == "1":
        print(x+y)
    elif ch == "2":
        print(x-y)
    elif ch == "3":
        print(x/y)
    elif ch == "4":
        print(x*y)
    else:
        print("Wrong Choice")

while True:

    print("""
    1. Add
    2. Sub
    3. Div
    4. Mul
    """)

    userChoice = input("Enter your choice : ")

    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))

    todo = {
        "1" : calc,
        "2" : calc,
        "3" : calc,
        "4" : calc,
        "q" : quit
    }

    todo.get(userChoice)(userChoice,num_1, num_2)

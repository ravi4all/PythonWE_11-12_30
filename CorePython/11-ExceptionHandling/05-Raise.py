def atm():
    try:
        x = int(input("Enter a number : "))
        y = int(input("Enter a number : "))
        if y > x:
            raise ValueError("Y should be smaller")
        else:
            z = x-y
            print("Result is",z)

    except (AssertionError, ValueError) as err:
        print(err)

atm()

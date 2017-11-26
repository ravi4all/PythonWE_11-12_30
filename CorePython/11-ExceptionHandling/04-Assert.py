def atm():
    try:
        x = int(input("Enter a number : "))
        y = int(input("Enter a number : "))
        z = x-y
        # Assert - Debugging
        assert(x > y), "Value cannot be negative"
        print("Result is",z)

    except (AssertionError, ValueError) as err:
        print(err)

atm()

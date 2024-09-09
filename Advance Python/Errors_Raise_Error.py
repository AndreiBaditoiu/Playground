while True:
    try:
        age3 = int(input("What is your age? "))  # wrap the input in int to make sure it will receive and int
        10 / age3
        raise Exception('Hey, cut it out!')

    except ZeroDivisionError:
        print("Please enter age higher than zero")
        break
    else:
        print("Thank you!")
        break
    finally:
        print("Ok, I'm finally done!")
    print("Can you hear me?")
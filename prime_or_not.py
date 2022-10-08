# Defining the function
def prime_checker(n):
    # checking if given number is greater than 1
    if n > 1:
        # iterating over the numbers
        for i in range(2, (n // 2) + 1):
            # if given number is divisible is not a prime number
            if n % i == 0:
                print("{} is a Not a Prime Number".format(n))
                break  # breaking the loop
        # Else it is a prime number
        else:
            print("{} is a Prime Number".format(n))

    # Else it is a not a prime number
    else:
        print("{} is not a Prime Number".format(n))


# Taking an input number from the user
a = int(input("Enter an input number:"))
# Printing result
prime_checker(a)

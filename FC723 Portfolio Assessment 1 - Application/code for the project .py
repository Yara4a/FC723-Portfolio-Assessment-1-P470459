def gcd(a, b):
    
    # calculate the GCD of two positive integers using the Euclidean Algorithm.
    
    while b != 0:
        a, b = b, a % b  
        # update a with b, and b with the remainder of a divided by b
    return a




def lcm(a, b):
    
    # calculate the LCM of two positive integers using the GCD.
    
    return abs(a * b) // gcd(a, b)  
    # use GCD to calculate LCM

    
def get_positive_integer(prompt):
    """
    Prompt the user for a positive integer and validate the input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if __name__ == "__main__":
    # Calls the main function if this file is run directly
        main()




# the main ain program
if __name__ == "__main__":
    print("Euclidean Algorithm: ")
    
    # Get inputs
    num1 = get_positive_integer("Enter the first positive integer: ")
    num2 = get_positive_integer("Enter the second positive integer: ")
    
    
    # Calculate and display results
    print(f"Greatest Common Divisor of {num1} and {num2}: {gcd(num1, num2)}")
    print(f"Least Common Multiple of {num1} and {num2}: {lcm(num1, num2)}")
    
   
    
   
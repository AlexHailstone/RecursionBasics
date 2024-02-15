# A program that asks the user for a natural number and 
# then calls a recursive function with that number as its argument. 
# The recursive function would take an input value n as its parameter and print 1, 
# then sum of first 2, the sum of first 3, …. ,the sum of first n natural numbers on separate lines. 
# The following would be two sample runs of the program.

# Examples:
## Enter a natural number: 3
## 1
## 3
## 6
 
## Enter a natural number: 5
## 1
## 3
## 6
## 10
## 15

class Recursion:
    def print_sums(self, n, current=1, total=0):
        # Recursive function to print the sum of first 'n' natural numbers.
        # n: The target natural number up to which sums are to be printed.
        # current: The current number being added to the sum.
        # total: The total sum accumulated up to the current number.

        # Base case: when the current number exceeds 'n', stop recursion
        if current > n:
            return

        # Calculate the new total with the current number added
        total += current

        # Print the current total
        print(total)

        # Recursive call to continue with the next number
        self.print_sums(n, current + 1, total)

# Loop until a valid input is received
while True:
    try:
        n = int(input("Enter a natural number: "))
        if n <= 0:
            print("Please enter a natural number greater than 0.")
        else:
            # If the input is a natural number, break from the loop
            break
    except ValueError:
        # Handle the case where the input is not an integer
        print("That's not an integer. Please enter a natural number greater than 0.")

# Instantiate the class
recursion_instance = Recursion()
# Call the instance method with the validated user input
recursion_instance.print_sums(n)


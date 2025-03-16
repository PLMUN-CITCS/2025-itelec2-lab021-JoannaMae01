"""
Factorial Calculator

This program prompts the user to enter a non-negative integer, validates the input, 
calculates its factorial, and displays the result.

Features:
- Function decomposition for modularity
- Input validation to ensure a valid non-negative integer is entered
- Iterative calculation of factorial using a loop
"""

def get_non_negative_integer() -> int:
    """
    Prompts the user to enter a non-negative integer and ensures valid input.

    Returns:
        int: A valid non-negative integer entered by the user.
    """
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))
            if number >= 0:
                return number
            print("Error: Please enter a non-negative integer.")
        except ValueError:
            print("Error: Please enter a valid integer.")


def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    Args:
        n (int): The non-negative integer for which the factorial is computed.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1  # Base case: 0! = 1

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    """
    Main function to get the user's non-negative integer input,
    compute its factorial, and display the result.
    """
    number = get_non_negative_integer()
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")


if __name__ == "__main__":
    main()

import re

def calculate(expression):
    # Replace all occurrences of the ^ operator with ** (exponentiation)
    expression = expression.replace("^", "**")
    # Replace all occurrences of the % operator with / 100
    expression = expression.replace("%", "/100")
    # Check for invalid characters
    if not re.match("^[\d+\-*/().%\s]+$", expression):
        return "Invalid expression!"
    try:
        # Evaluate expression using eval function
        result = eval(expression)
        # Check for division by zero
        if isinstance(result, (int, float)) and result in [float('inf'), float('-inf')]:
            return "Infinity"
        # Round result to 2 decimal places if it's a float
        result = round(result, 2) if isinstance(result, float) else result
        # Convert result to string and return it
        return str(result)
    except ZeroDivisionError:
        return "Infinity"
    except:
        return "Invalid expression!"


def get_user_input():
    # Get user input
    expression = input("Enter an expression: ")
    # Calculate result
    result = calculate(expression)
    # Print result
    print("Result:", result)

if __name__ == '__main__':
    get_user_input()

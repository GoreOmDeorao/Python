def string_to_int(num_str):
    """Convert a string to an integer."""
    result = 0
    for char in num_str:
        digit = ord(char) - ord('0')
        result = result * 10 + digit
    return result

def subtract_decimals(num1_str, num2_str):
    """Subtract two numbers represented as strings and handle negative results."""
    # Determine if the result will be negative
    num1_int = string_to_int(num1_str)
    num2_int = string_to_int(num2_str)
    
    if num1_int < num2_int:
        # Swap numbers and add a negative sign
        num1_str, num2_str = num2_str, num1_str
        is_negative = True
    else:
        is_negative = False

    # Ensure the numbers have the same length by padding with zeros
    max_len = max(len(num1_str), len(num2_str))
    num1_str = num1_str.zfill(max_len)
    num2_str = num2_str.zfill(max_len)
    
    result = []
    borrow = 0
    
    for i in range(max_len - 1, -1, -1):
        digit1 = int(num1_str[i])
        digit2 = int(num2_str[i]) + borrow

        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
        
        result.append(str(digit1 - digit2))
    
    # Remove leading zeros and reverse the result
    final_result = ''.join(result[::-1]).lstrip('0')
    
    # Handle the case where the result is empty (i.e., the result is 0)
    if final_result == '':
        final_result = '0'
    
    # Add negative sign if needed
    if is_negative:
        final_result = '-' + final_result
    
    return final_result

def get_input_and_subtract():
    """Take inputs from the user and subtract the numbers."""
    num1_str = input("Enter the first number: ")
    num2_str = input("Enter the second number: ")

    result = subtract_decimals(num1_str, num2_str)
    print(f"Result: {result}")

# Example usage
get_input_and_subtract()


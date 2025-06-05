import re

def validate_input(input_data):
    if not isinstance(input_data, str) or not input_data.strip():
        raise ValueError("Input must be a non-empty string.")
    return True

def format_text(text):
    return text.strip().capitalize()

def log_message(message):
    with open("app.log", "a") as log_file:
        log_file.write(f"{message}\n")

def process_input(user_input):
    try:
        num = int(user_input)
        if num > 7:
            return "Hello"
        else:
            return "(Number entered, but not greater than 7)"
    except ValueError:
        pass

    if user_input.lower() == "john":
        return "Hello, John"
    elif user_input.isalpha():
        return "There is no such name"

    nums = re.split(r'[ ,]+', user_input)
    try:
        nums = [int(x) for x in nums if x]
        multiples = [str(x) for x in nums if x % 3 == 0]
        if multiples:
            return f"Multiples of 3: {', '.join(multiples)}"
        else:
            return "No multiples of 3 found."
    except ValueError:
        pass

    return "Invalid input. Please enter a number, a name, or a list of numbers."
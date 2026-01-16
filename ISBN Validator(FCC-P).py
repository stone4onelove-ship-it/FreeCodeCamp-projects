def validate_isbn(isbn, length):
    short_length = length - 1
    main_digits = isbn[0:short_length]
    given_check_digit = isbn[short_length]
    main_digits_list = [int(digit) for digit in main_digits]
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')
    if not ',' in user_input:
        print('Enter comma-separated values.')
        return False
    if not values[1].isdigit():
        print('Length must be a number.')
        return False
    isbn = values[0]
    length = int(values[1])
    if not length in [10,13]:
        print('Length should be 10 or 13.')
        return False
    if length == 10 and len(isbn) == 10:
            for letter in isbn[:9]:
                if letter not in '0123456789':
                    print('Invalid character was found.')
                    return False
            if isbn[9] not in '0123456789X':
                print('Invalid character was found.')
                return False
    if length == 13:
        for letter in isbn:
            if letter not in '0123456789':
                print('Invalid character was found.')
                return False
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return False
    validate_isbn(isbn, length)

main()
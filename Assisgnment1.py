import re

def parse_phone_number(number):
    pattern_1 = r'(\d{10})'  # "2124567890"
    if re.search(pattern_1, number):
        print(f" Input Phone Number : {number} pattern is Valid")
        return

    pattern_2 = r'(\d{3}(-)\d{3}(-)\d{4})'  # "212-456-7890"
    if re.search(pattern_2, number):
        print(f" Input Phone Number : {number} pattern is Valid")
        return

    pattern_5 = r'(\d{3}.\d{3}.\d{4})'  # "212.456.7890"
    if re.search(pattern_5, number):
        print(f" Input Phone Number : {number} pattern is Valid")
        return

    pattern_6 = r'(\d{3} \d{3} \d{4})'  # "212 456 7890"
    if re.search(pattern_6, number):
        print(f" Input Phone Number : {number} pattern is Valid")
        return

    pattern_7 = r'((0|9|\+1)?\d{10})'  # "+12124567890"
    if re.search(pattern_7, number):
            print(f" Input Phone Number : {number} pattern is Valid")
            return

    pattern_8 = r'((0|9|\+1)? \d{3}.\d{3}.\d{4})'  # "+1 212.456.7890"
    if re.search(pattern_8, number):
        print(f" Input Phone Number : {number} pattern is Valid")
        return

    pattern_9 = r'((0|9|\+\d{3})?-\d{3}-\d{4})'  # "+212-456-7890"
    if re.search(pattern_9, number):
        print(f" Input Phone Number : {number} pattern is Valid")
        return

    pattern_10 = r'(\d{1}-\d{3}-\d{3}-\d{4})'  # "1-212-456-7890"
    if re.search(pattern_10, number):
        print(f" Input Phone Number : {number} pattern is Valid")
        return
    else:
        print("Invalid")

phonelist = ["2124567890",
            "212-456-7890",
            "212.456.7890",
             "212 456 7890",
             "+12124567890",
             "+1 212.456.7890",
             "+212-456-7890",
             "1-212-456-7890"]

for number in phonelist:
    # print('checking for date: ', date)
    parse_phone_number(number)




def analyze_string(input_string):
    word_count = len(input_string.split())
    blank_count = input_string.count(' ')
    upper_count = sum(1 for char  in input_string if char.isupper())
    lower_count = sum(1 for char  in input_string if char.islower())

    print(f"Total Words : {word_count}")
    print(f"Total Blanks : {blank_count}")
    print(f"Total UpperCase : {upper_count}")
    print(f"Total LowerCase: {lower_count}")

user_input = input("Enter any String :  ")
analyze_string(user_input)
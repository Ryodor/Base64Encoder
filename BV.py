
# This method returns a string with 'ABCD' in value


def return_char_string():
    char_string = 'ABCD'
    print(char_string)


return_char_string()


# This method transforms a string into a list filled with every character of the string

def transform_to_list(char_str):
    chars = []
    for character in char_str:
        for c in character:
            chars.append(c)

    print(chars)


transform_to_list('ABCD')

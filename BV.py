


# This method returns a string with 'ABCD' in value


def return_char_string():
    char_string = 'ABCD'
    print(char_string)
    return(char_string)


char_string = return_char_string()


# This method transforms a string into a list filled with every character of the string

def transform_to_list(char_str):
    chars = []
    for character in char_str:
            chars.append(character)

    print(chars)
    return(chars)


char_list = transform_to_list(char_string)


# This method transforms each element in its ASCII code

def transform_to_ascii(list):
    ascii_list = []
    for character in list:
            ord(character)
            ascii_list.append(ord(character))

    print(ascii_list)
    return(ascii_list)

transform_to_ascii(char_list)

def return_char_string():
    """This method returns a string with 'ABCD' in value

    Returns:
        char_string (string): always equal to 'ABCD'
    """
    char_string = 'ABCD'
    return (char_string)


def transform_to_list(char_str):
    """This method transforms a string into a list filled with every character of the string

    Args:
        char_str (string) : The only parameter.

    Returns:
        chars ([]) : A list
    """
    chars = []
    for character in char_str:
        chars.append(character)
    return chars


def transform_to_ascii(char_list):
    """This method transforms each element in its ASCII code

    Args:
        char_list ([]): A list of strings
    Returns:
        ascii_list ([]): A list of ints
    """
    ascii_list = []
    for character in char_list:
        ord(character)
        ascii_list.append(ord(character))
    return ascii_list


def transform_to_binary(ascii_list):
    """This method transforms each element in its binary value

    Args:
        ascii_list ([]): A list
    Returns:
        binary_list ([]): A list
    """
    binary_list = []
    for element in ascii_list:
        i = bin(element).replace('b', '')
        binary_list.append(i)
    return binary_list


def merge_elements(binary_list):
    """This method concatenate every elements in a list into a string

    Args:
        binary_list (string): A list
    Returns:
        merged_elements: A string
    """
    merged_elements = ''
    for element in binary_list:
        merged_elements += str(element)
    return merged_elements


def slice_list(merged_elements):
    """This method slice a string in a list of string. Each string is equal to 6 characters.
    The last element of the list can be inferior or equal to 6 characters

    Args:
        merged_elements (string): The string you want to split
    Returns:
        sliced_list ([]): A list
    """
    sliced_list = [merged_elements[element:element + 6] for element in range(0, len(merged_elements), 6)]
    return sliced_list


def fill_blank(sliced_list):
    """This method fills the last element with 0 until it has a length equal to 6

    Args:
        sliced_list ([]): A list
    Returns:
        filled_list ([]): The list with the last element length equal to 6
    """
    if len(sliced_list[-1]) < 6:
        sliced_list[-1] = sliced_list[-1] + "0"
        fill_blank(sliced_list)

    filled_list = sliced_list
    return filled_list


def main():
    char_string = return_char_string()
    char_list = transform_to_list(char_string)
    ascii_list = transform_to_ascii(char_list)
    binary_list = transform_to_binary(ascii_list)
    merged_elements = merge_elements(binary_list)
    sliced_list = slice_list(merged_elements)
    filled_list = fill_blank(sliced_list)


if __name__ == '__main__':
    main()

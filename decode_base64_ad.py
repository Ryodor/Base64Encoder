#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Story 17: Transformer chaque élément de la liste
# dans sa représentation binaire (cadrée à droite sur 6 positions)
# Exemple : [16, 20, 9, 3, 17, 0]


def b64_decimal_to_b64_binary(transform_element):
    """ Transform decimal base64 to binary base64

        Args:
            transform_element(List): element decimal

        Returns:
            List : binary number

    """
    for index, value in enumerate(transform_element):
        binary_value = format(value, 'b')
        if len(binary_value) < 6:
            while len(binary_value) < 6:
                binary_value = "0"+binary_value

            transform_element[index] = binary_value

    return transform_element


b64_decimal_to_b64_binary([16, 20, 9, 3, 17, 0])

# Result : ["010000","010100","001001","000011","010001","000000"]

# Story 18: Transformer la liste en une chaine de caractères
# Exemple : ["010000","010100","001001","000011","010001","000000"]


def binary_to_string(tranfrom_value):
    """ Tranform binary value list to string binary value

    Args:
        tranfrom_value(List):  List binary value

    Returns: string binary value

    """

    return ''.join(tranfrom_value)


binary_to_string(["010000","010100","001001","000011","010001","000000"])

# Result : "010000010100001001000011010001000000"

# Story 19: Raccourcir la chaine (par la droite) pour que sa longueur,
# soit multiple de huit.
# Exemple : "010000010100001001000011010001000000"


def transfrom_binary_multipl8(transform_binary):
    """ Trasnfrom the string binary so that size of the string,
        be equal to a multpiple of 8

    Args:
        transform_binary(String): String of binary value

    Returns: string binary value equal to o a multpiple of 8

    """

    if (len(transform_binary) % 8) > 0:
        rest = len(transform_binary) % 8
        transform_binary = transform_binary[:-rest]

    return transform_binary

transfrom_binary_multipl8("010000010100001001000011010001000000")

# Result : "01000001010000100100001101000100"


# Story 20: Transformer la chaine en liste
# (chaque élément a une longueur de huit)
# Exemple : "01000001010000100100001101000100"


def transform_binary_string_to_list(transform_string):
    """ Transformation of the binary value character string into an 8 character
        block list

    Args:
        transform_string(String): String character binary value

    Returns: List of string character binary value

    """
    transform_string_to_list = list()
    for i in range(0,len(transform_string), 8):
        transform_string_to_list.append(transform_string[i:i + 8])

    return transform_string_to_list


transform_binary_string_to_list("01000001010000100100001101000100")

# Result : ['01000001','01000010','01000011','01000100']

# Story 21: Transformer chaque élément de la liste dans sa valeur décimale
# Exemple : ['01000001','01000010','01000011','01000100']


def transform_list_binary_to_decimal(transfrom_value):
    """ Transform List string binary value in decimal value

    Args:
        transfrom_value(List): string of binary value

    Returns: list decimal value int

    """

    for index, value in enumerate(transfrom_value):
        transfrom_value[index] = int(value, 2)

    return transfrom_value


transform_list_binary_to_decimal(['01000001','01000010','01000011','01000100'])

# Result : [65, 66, 67, 68]


# Story 22: Transformer chaque élément dans le caractère ASCII correspondant
# Exemple : [65, 66, 67, 68]


def decimal_list_to_ascii(transfrom_value):
    """ Transforms the decimal value into an ascii character

    Args:
        transfrom_value(List): decimal value in list

    Returns: List of character value

    """

    for index, value in enumerate(transfrom_value):
        transfrom_value[index] = chr(value)

    return transfrom_value

decimal_list_to_ascii([65, 66, 67, 68])

# Result : ['A', 'B', 'C', 'D']


# Story 23: Transformer la liste en chaine de caractères
# Exemple : ['A', 'B', 'C', 'D']


def list_decimal_to_string(transform_string):
    """ Transfrom list to string

    Args:
        transform_string(List): list of character

    Returns: string

    """

    return ''.join(transform_string)


list_decimal_to_string(['A', 'B', 'C', 'D'])

# Result : "ABCD"


def main():
    """ This is main function and test all function

    Returns: none

    """

    operation1 = b64_decimal_to_b64_binary([16, 20, 9, 3, 17, 0])
    print("test b64_decimal_to_b64_binary : ", operation1)
    operation2 = binary_to_string(operation1)
    print("test binary_to_string : ", operation2)
    operation3 = transfrom_binary_multipl8(operation2)
    print("test transfrom_binary_multipl8 : ", operation3)
    operation4 = transform_binary_string_to_list(operation3)
    print("test transform_binary_string_to_list : ", operation4)
    operation5 = transform_list_binary_to_decimal(operation4)
    print("test transform_list_binary_to_decimal : ", operation5)
    operation6 = decimal_list_to_ascii(operation5)
    print("test decimal_list_to_ascii : ", operation6)
    operation7 = list_decimal_to_string(operation6)
    print("test list_decimal_to_string : ", operation7)


if __name__ == "__main__":
    # execute only if run as a script
    main()


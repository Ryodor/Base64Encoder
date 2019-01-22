#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Parti 8 : Transformer chaque element de la liste dans ca valeur decimal
# Exemple : ["010000","010100","001001","000011","010001","000000"]


def binary_to_decimal(transform_list):
    """ Transform binary value to decimal value

        Args:
            transform_list(list): list of the value binary.

        Returns:
            List: decimal.

    """

    for index, number in enumerate(transform_list):
        transform_list[index] = int(number, 2)

    print(transform_list)
    return transform_list


binary_to_decimal(["010000","010100","001001","000011","010001","000000"])

# Result = [16, 20, 9, 3, 17, 0]


# Parti 9 : Transformer chaque element de la liste dans ca valeur decimal
# Exemple : [16, 20, 9, 3, 17, 0]

base64_caractere = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")


def decimal_to_base64(transform_list):
    """ Transform decimal value to base64 caractere

        Args:
            transform_list(List): list of the value decimal.

        Returns:
            List: String value.

    """
    for index, number in enumerate(transform_list):
        transform_list[index] = base64_caractere[transform_list[index]]

    print(transform_list)
    return transform_list


decimal_to_base64([16, 20, 9, 3, 17, 0])

# Result = ["Q", "U", "J", "D", "R", "A"]


# Parti 10 : Transformer la liste en une chaine de caractères
# Example : ["Q", "U", "J", "D", "R", "A"]

def base64_list_tostring(transform_list):
    """ Transform decimal value to base64 caractere

        Args:
            transform_list(List): list of the value caractere base64.

        Returns:
            String : string value of the list

    """

    print(''.join(transform_list))
    return ''.join(transform_list)


base64_list_tostring(["Q", "U", "J", "D", "R", "A"])

# Result : "QUJDRA"

# Parti 10 : Cadrer la chaine dans un champ d'une longueur multiple de quatre (cadrée à gauche comblée par des "="
# Example : "QUJDRA=="


def string_base64_commpleting(complete_string):
    """ Add caractere compliment if complete_string is not multipl of 4

        Args:
            complete_string(List): element enceded in base64

        Returns:
            String : retourn final element encoded in base64

    """

    result_modulo = len(complete_string) % 4
    complet_element = ""
    print(result_modulo)
    if result_modulo > 0 :
        i = 0
        while i < result_modulo:
            complet_element += "="
            i += 1

    complete_string += complet_element
    print(complete_string)
    return complete_string


string_base64_commpleting("QUJDRA")

# Result : "QUJDRA=="
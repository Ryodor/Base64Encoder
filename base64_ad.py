#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Parti 8 : Transformer chaque element de la liste dans ca valeur decimal
# Exemple : ["010000","010100","001001","000011","010001","000000"]


def binaire_to_decimal(binaire):
    """ Transform binary value to decimal value

        Args:
            binaire(list): list of the value binaire.

        Returns:
            List: decimal.

    """

    for index, number in enumerate(binaire):
        binaire[index] = int(number, 2)

    print(binaire)
    return binaire


binaire_to_decimal(["010000","010100","001001","000011","010001","000000"])

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

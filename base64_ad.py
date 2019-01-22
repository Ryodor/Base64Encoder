#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Parti 8 : Transformer chaque element de la liste dans ca valeur decimal
# Exemple : ["010000","010100","001001","000011","010001","000000"]


def binaire_to_decimal(binaire):
    """ Transform binaire value to decimal value

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

# resultat = [16, 20, 9, 3, 17, 0]


# Parti 9 : Transformer chaque element de la liste dans ca valeur decimal
# Exemple : [16, 20, 9, 3, 17, 0]

base64_caractere = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

def decimal_to_base64(transformList):
    """ Transform ecimal value to base64 caractere

        Args:
            transformList(List): list of the value decimal.

        Returns:
            List: String value.

    """
    for index, number in enumerate(transformList):
        transformList[index] = base64_caractere[transformList[index]]

    print(transformList)
    return transformList

decimal_to_base64([16, 20, 9, 3, 17, 0])

# resultat = ["Q", "U", "J", "D", "R", "A"]
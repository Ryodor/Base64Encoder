#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Parti 8 : Transformer chaque element de la liste dans ca valeur decimal
# Exemple : ["010000","010100","001001","000011","010001","000000"]


def binaire_to_decimal(binaire):
    """ Transform binaire value to decimal value

        Args:
          binaire: value binaire.
        Returns:
          List decimal.
    """

    for index, number in enumerate(binaire):
        binaire[index] = int(number, 2)

    print(binaire)
    return binaire


binaire_to_decimal(["010000","010100","001001","000011","010001","000000"])

# resultat = [16, 20, 9, 3, 17, 0]

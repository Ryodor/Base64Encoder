#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Story 17: Transformer chaque élément de la liste dans sa représentation binaire (cadrée à droite sur 6 positions)
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

        print(transform_element)

    return transform_element


b64_decimal_to_b64_binary([16, 20, 9, 3, 17, 0])

# Result : ["010000","010100","001001","000011","010001","000000"]

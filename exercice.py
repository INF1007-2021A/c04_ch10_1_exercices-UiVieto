#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.linspace(-1.3, 2.5, 64)


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:

    coordonnees_polaires = []
    for elem in cartesian_coordinates:
        coordonnees_polaires.append([np.sqrt(elem[0]**2 + elem[1]**2), np.degrees(np.arctan(elem[1]/elem[0]))])

    return np.array(coordonnees_polaires)


def find_closest_index(values: np.ndarray, number: float) -> int:
    return 0


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass

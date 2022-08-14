"""
Array in python is most commonly referred to as `lists`. Here we implement
the same structure as you would when using common working methods in lists.
"""


class Array:
    def __init__(self, *args) -> None:
        self._array = list(args)

    # def __repr__(self) -> list:
    #     return

    def __add__(self, list_to_add: list) -> list:
        """
        Add two lists together.

        Parameters
        ----------
        list_to_add: list
            Arbitrary list to add.

        Returns
        -------
        list
            1D array of two lists added.
        """
        return [*self._array, *list_to_add]

    def __mul__(self, integer: int) -> list:
        return [j for j in self._array for _ in range(integer)]

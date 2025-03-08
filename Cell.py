class Cell:
    """Represents a cell in a grid.

       Attributes:
           value (int): The value of the cell (0 represents an empty cell).
           fixed (bool): Indicates if the value is fixed and cannot be changed.
           possible_values (set): A set of possible values for the cell.
       """

    def __init__(self, value:int = 0, fixed:bool = False):
        """  initialize all attributes for a cell
            :param value: Initial value (default = 0)
            :type value: int
            :param fixed: Fixed value (default = False)
            :type fixed: bool
            """

        self.value = value
        self.fixed = fixed
        self.possible_values = set(range(1, 10))

    def set_value(self, value:int):
        """ Sets the value of the cell.
        If the cell is not fixed and the value is possible the value gets set
        :param value: value to set
        :return: an ValueError when setting is not possible
        """
        if not self.fixed and value in self.possible_values:
            self.value = value
            self.possible_values.remove(value) # remove from possible value
        else:
            raise ValueError("Value is fixed and cannot be set.")

    def reset(self):
        """ Resets the cell to its initial value
        :return: ValueError when resetting is not possible
        """
        if not self.fixed:
            self.value = 0
            self.possible_values = set(range(1, 10))
        else:
            raise ValueError("Value is fixed and cannot be reset.")

    def eliminate_possible_values(self, value):
        """ removes value from possible_values for this cell

        :param value: value to eliminate
        """
        if value in self.possible_values:
            self.possible_values.remove(value)

    def __str__(self):
        """ prints value if one is set else .
        :return: string representation of the cell
        """
        return str(self.value) if self.value != 0 else "."

    def __repr__(self):
        """ prints value if one is set else ."""
        return f"Cell(value={self.value}, fixed={self.fixed}, possible_values={self.possible_values})"

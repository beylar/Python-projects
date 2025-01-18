class NSideDieFixed:
    """A class for a N-sided die with deterministic outcomes

    Attributes
    ----------
    sides : int
        the number of sides in the die
    value : int
        the current value of the die

    Methods
    -------
    roll(None)
        generate the outcome of rolling a die
        The next outcome is the increment of the current value.

    getValue(None)
        get the current value of a die

    setValue(int)
        set the current value of a die

    Raises
    ------
    ValueError
        if the number of sides is less than 1
        if value to be set in setValue() is out of range
    """

    def __init__(self, no_sides):
        """Initialize a die

        Parameters
        ----------
        no_sides : int
            The number of sides in the die

        Returns
        -------
        None
        """
        if no_sides < 1:
            print("ValueError: The number of sides must be at least 1.")
            return
        self.__sides = no_sides
        self.__value = 1

    def roll(self):
        """Roll this die

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.__sides-1 < self.__value:
            self.__value = 1
            return
        self.__value += 1


    def getValue(self):
        """Get the velue of this die

        Parameters
        ----------
        None

        Returns
        -------
        int
            the current value of the dice
        """
        return self.__value


    def setValue(self, value):
        """Set the value of this die to a given value

        Parameters
        ----------
        value : int
            the value to be set

        Returns
        -------
        None
        """
        if 1 <= value <= self.__sides:
            self.__value = value
            return
        print("ValueError: The value must be between 1 and 6, inclusive.\n")
            
        
print("For die 0:")
die0 = NSideDieFixed(0)
print()

dieA = NSideDieFixed(6)
print("For die A:")
for times in range(15):
    dieA.roll()
    print(f"The {times+1:2}th time: {dieA._NSideDieFixed__value}")
print()

dieB = NSideDieFixed(10)
print("For die B:")
for times in range(20):
    dieB.roll()
    print(f"The {times+1:2}th time: {dieB._NSideDieFixed__value}")
print()

dieC = NSideDieFixed(6)
dieC.setValue(7)
dieC.setValue(3)
print(f"Die C's value: {dieC._NSideDieFixed__value}")
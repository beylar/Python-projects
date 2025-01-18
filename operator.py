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

    __add__(NSideDieFixed)
        add the value of this die and the other's

    __le__(NSideDieFixed)
        determine whether the value of this die is less or
        equal than the other's

    __len__(NSideDieFixed)
        return the number of sides of this die

    __str__(None)
        return a string about the number of sides and the current value of a die

    __repr__(None)
        return a string about which class this die comes from

    Raises
    ------
    ValueError
        if value in __init__() is les than 1
        if value to be set in setValue() is out of range
    """

    sides = 6
    def __init__(self, value):
        """Initialize a die

        Parameters
        ----------
        value : int
            The initial value of a die

        Returns
        -------
        None
        """
        if value < 1 or value > NSideDieFixed.sides:
            raise ValueError(f"The value must be between 1 and {NSideDieFixed.sides}.")
        self.__value = value


    def roll(self):
        """Roll this die

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if self.sides-1 < self.__value:
            self.__value = 1
        else:
            self.__value += 1


    def getValue(self):
        """Get the value of this die

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
        """Set the value of this die to the given value

        Parameters
        ----------
        value : int
            the value to be set

        Returns
        -------
        None
        """
        if 1 <= value <= NSideDieFixed.sides:
            self.__value = value
        else:
            print("ValueError: The value must be between 1 and {NSideDieFixed.sides}, inclusive.")


    def __add__(self, other):
        """Add the value of this die and the other's

        Parameters
        ----------
        other : NSideDieFixed
            the other die

        Returns
        -------
        int
            the sum of the two dice's values
        """
        return self.__value + other.__value


    def __le__(self, other):
        """Check whether the vlaue of this die is less than or equal to the others'

        Parameters
        ----------
        other : NSideDieFixed
            the other die

        Returns
        -------
        True
            if the value of this die is less than or equal
            to the other die's
        False
            otherwise
        """
        return self.__value <= other.__value


    def __len__(self):
        """Find the number of sides of this die

        Parameters
        ----------
        None

        Returns
        -------
        int
            the number of sides in the die
        """
        return NSideDieFixed.sides


    def __str__(self): # returns a string using f-strings will have both instant and class variable
        """Compose a string for describing this object when print() is called.

        Parameters
        ----------
        None

        Returns
        -------
        str
            returns a string which includes the number sides and the current value of a die
        """
        return f"This die has {NSideDieFixed.sides} sides with a value of {self.__value}."


    def __repr__(self): # self.__class__ which is used to print the string with the given value
        """Compose a string for describing this object when typing its name in a shell.

        Parameters
        ----------
        None

        Returns
        -------
        str
            returns a string about which class this die comes from
        """
        return f"This is an object from {self.__class__}."
    

dieA = NSideDieFixed(1)
print("For die A:")
print(dieA)

dieB = NSideDieFixed(2)
print("\nFor die B:")
print(dieB)

print("\nAfter changing the class variable sides:")
NSideDieFixed.sides = 12
print(dieA)
print(repr(dieB)) 
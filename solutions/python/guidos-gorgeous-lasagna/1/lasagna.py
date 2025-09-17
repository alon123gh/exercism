"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int) -> int:
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return max(EXPECTED_BAKE_TIME-elapsed_bake_time,0)


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the total preparation time for a lasagna.

    Each layer of the lasagna takes a fixed amount of time (defined by the
    PREPARATION_TIME constant) to prepare. This function multiplies the
    number of layers by that constant.

    Args:
        number_of_layers (int): The number of layers in the lasagna.

    Returns:
        int: Total preparation time in minutes.
    """
    return number_of_layers*PREPARATION_TIME


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
     """ Calculate the total elapsed cooking time for the lasagna.

    This includes both:
    - The preparation time, based on the number of layers.
    - The baking time that has already elapsed.

    Args:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): The time already spent baking, in minutes.

    Returns:
        int: Total elapsed time (preparation + elapsed bake time), in minutes.
    """
     return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)

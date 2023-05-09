# This file calculate the blood alcohol level of a person based on the number of drinks he had.

# Importing the necessary modules
import sys
import math

# Defining the constants
ALCOHOL_DENSITY = 0.789
ALCOHOL_ELIMINATION = 0.15

# Defining the functions
def get_drink_info():
    """
    This function asks the user for the number of drinks he had and the time he had them.
    It returns a list of the number of drinks and the time he had them.
    """
    drinks = int(input("Nombre de Paix dieu consommées (pinte): "))
    masse = int(input("Masse (kg): "))
    lapse_temps = int(input("durée de la beuverie (min): "))
    return drinks, masse, lapse_temps

def get_alcohol_level(drinks, masse, lapse_temps):
    """
    This function calculates the alcohol level of a person based on the number of drinks he had and the time he had them.
    It returns the alcohol level of the person.
    """
    alcohol_level = ((drinks*500) * 0.1 * ALCOHOL_DENSITY) / (0.7 * masse)
    print(alcohol_level)
    alcohol_level = alcohol_level - (ALCOHOL_ELIMINATION * (lapse_temps/60))
    return alcohol_level

def get_time_to_zero(alcohol_level):
    """
    This function calculates the time it takes for a person to have an alcohol level of 0.
    It returns the time it takes for a person to have an alcohol level of 0.
    """
    time_to_zero = alcohol_level / ALCOHOL_ELIMINATION
    return time_to_zero

def main():
    """
    This function calculates the alcohol level of a person based on the number of drinks he had and the time he had them.
    It returns the alcohol level of the person and the time it takes for a person to have an alcohol level of 0.
    """
    drinks, masse, lapse_temps = get_drink_info()
    alcohol_level = get_alcohol_level(drinks, masse, lapse_temps)
    time_to_zero = get_time_to_zero(alcohol_level)
    print("Alcoolémie: {:.2f}".format(alcohol_level))
    print("Temps avant retour à zéro: {:.2f}".format(time_to_zero))

# Main program
if __name__ == "__main__":
    main()

# End of program

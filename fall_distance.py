# Author: Jovane Cano
# Github Username: jovanecano
# Date: 04/20/2024
# Description: The following is a function that returns the distance in meters that an object has fallen in time.

# formula used to determine the distance that the object falls due to gravity in a specific time period: d = (1/2)gt^2
def fall_distance(seconds):
    """This function assigns values to the g and t variables from the formula listed above and
    returns the value"""
    g = 9.8 # assigning g the values of 9.8
    t = seconds # t will vary based on the argument entered by the user
    d = ((1 / 2) * g * t ** 2)
    return d


# dist = fall_distance(3.2)
# print(dist)

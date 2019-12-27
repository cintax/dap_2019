"""This module does blah blah."""

from math import sqrt

__version__ = "v1.0" 
__author__  = "C1ntax"

def hypothenuse(side_one, side_two):
    """ returns the length of the hypothenuse when given the lengths of two other sides of a right-angled triangle """
    return sqrt((side_one ** 2) + (side_two **2))

def area(side_one, side_two):
    """ returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters """
    return 0.5 * side_one * side_two
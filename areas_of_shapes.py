#!/usr/bin/env python3

import math

def circle():
    radius = int(input("Give radius of the circle: ")) 
    print(f"The area is {math.pi*(radius**2):6f}")

def rectangle():
    width = int(input("Give width of the rectangle: "))
    height = int(input("Give height of the rectangle: "))
    print(f"The area is {height*width:6f}")

def triangle():
    base = int(input("Give base of the triangle: "))
    height = int(input("Give height of the triangle: "))
    print(f"The area is {0.5*base*height:6f}")

def main():
    # enter you solution here
    while True:
        choice = input("Choose a shape (triangle, rectangle, circle): ")
        if choice == "triangle":
            triangle()
        elif choice == "circle":
            circle()
        elif choice == "rectangle":
            rectangle()
        elif choice == "":
            break
        else:
            print("Unknown shape!")

if __name__ == "__main__":
    main()

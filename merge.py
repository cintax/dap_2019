#!/usr/bin/env python3

def merge(L1, L2):
    L = L1 + L2
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(L) - 1):
            if L[i] > L[i + 1]:
                # Swap the elements
                L[i], L[i + 1] = L[i + 1], L[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return L

def main():
    list_one = [-97, -69, -65, -64, -37, -13, -9, -7, 2, 6, 19, 40, 60, 63, 64, 74, 76, 93, 95, 96]
    list_two = [-99, -70, -65, -40, -35, -1, 14, 19, 20, 87]
    list_three = merge(list_one, list_two)
    print(list_three)

if __name__ == "__main__":
    main()

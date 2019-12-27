#!/usr/bin/env python3

import sys,math

def summary(filename):
    with open(filename, 'r') as f:
        x = 0
        numbers = []
        for lines in f:
            try:
                num = float(lines.strip("\n"))
            except ValueError:
                print("Invalid Character")
                continue
            numbers.append(num)
            
        print(numbers)
            
        addition = sum(numbers)
        average = addition / len(numbers)
        
        for number in numbers:
            x += (float(number) - average)**2
        
        sd = abs(math.sqrt(x / float(len(numbers) - 1)))
        
        return(addition,average,sd)
            
def main():
    for filename in sys.argv[1:]:
        triple = summary(filename)
        print(f"File: {filename} Sum: {'%.6f'%triple[0]} Average: {'%.6f'%triple[1]} Stddev: {'%.6f'%triple[2]}")
        
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename,'r') as f:
        lines = f.readlines()
        lines.pop(0)
        
        pattern = r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)"
        
        for line in lines:
            temp = re.findall(pattern, line)
            string = "\t".join(list(temp[0]))
            result.append(string)
            
    return result
        
def main():
    print(red_green_blue())

if __name__ == "__main__":
    main()

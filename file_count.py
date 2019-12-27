#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, 'r') as f:
        line_count = 0
        word_count = 0
        char_count = 0
        for lines in f:
            line_count += 1
            for word in lines.split():
                word_count += 1
            for char in lines:
                char_count += 1
                    
    return (line_count, word_count, char_count)
                
def main():
    for filename in sys.argv[1:]:
        triple = file_count(filename)
        print(f"{triple[0]}\t{triple[1]}\t{triple[2]}\t{filename}")

if __name__ == "__main__":
    main()

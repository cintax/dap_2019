#!/usr/bin/env python3

import sys,re

def file_extensions(filename):
    list1 = []
    dict1 = {}
    set1 = []
    with open(filename, 'r') as f:
        list1_pattern = r'^\w+$'
        dict_pattern = r'\.(\w+$)'
        lines = f.readlines()
        for line in lines:
            temp = re.findall(list1_pattern, line)
            if temp:
                list1.append(temp[0])

        for line in lines:       
            temp = re.findall(dict_pattern, line)
            if temp:
                set1.append(temp[0])
        
        set1 = list(set(set1))
        
        for s in set1:
            dict1[s] = []
            for line in lines:
                temp = re.findall(r'\.(\w+$)',line)
                
                if temp:
                    if temp[0] == s:
                        q = re.findall('.*',line)
                        dict1[s].append(q[0])
            
    return (list1, dict1)

def main():
    lister = file_extensions(r"src\filenames.txt")
    print(f"{len(lister[0])} files with no extension")
    for x in lister[1]:
        print(f"{x}")
    
if __name__ == "__main__":
    main()

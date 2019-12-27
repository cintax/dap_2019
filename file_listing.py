#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    info = []
    result = []
    with open(filename,"r") as f:
        for line in f:
            sdhm_regex = re.findall(r'\d{1,}',line)
            month_regex = re.findall(r'[A-Z]..',line)
            file_regex = re.findall(r'[.A-Za-z]\w*.\w*.\w*.\w*',line)
            info.append(int(sdhm_regex[1]))
            info.append(month_regex[0])
            info.append(int(sdhm_regex[2]))
            info.append(int(sdhm_regex[3]))
            info.append(int(sdhm_regex[4]))
            info.append(file_regex[-1])
            result.append(tuple(info))
            info = []
    
    print(result)
    return result

def main():
    file_listing()

if __name__ == "__main__":
    main()

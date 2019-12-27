#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    reg_list = re.findall(r'\[\s*([-+]?\d+)\s*\]',s)
    for i in range(len(reg_list)):
        reg_list[i] = int(reg_list[i])
    return reg_list
        
def main():
    print(integers_in_brackets(" afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xxx"))

if __name__ == "__main__":
    main()

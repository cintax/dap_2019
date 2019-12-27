#!/usr/bin/env python3

def find_matching(L, pattern):
    obj = list(enumerate(L))
    result = []
    for x in obj:
        if pattern in x[1]:
            result.append(x[0])
            
    return result        

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))
    
if __name__ == "__main__":
    main()

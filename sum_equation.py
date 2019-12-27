#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    
    add = sum(L)
    
    s = " + ".join(str(x) for x in L)
    
    s += " = " +str(add)
    
    return s
        
        
def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()

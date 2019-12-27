#!/usr/bin/env python3

def triple(value):
    return value*3
        
def square(value):
    return value**2

def main():
    for i in range(1,11):
        a = triple(i)
        b = square(i)
        if b > a:
            break
        print(f"triple({i})=={a} square({i})=={b}")

if __name__ == "__main__":
    main()

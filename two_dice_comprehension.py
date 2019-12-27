#!/usr/bin/env python3

def main():
    s = { m : n for m in range(1,6)
                for n in range(1,6) if m + n == 5}
    for key, value in s.items():
        print(f"({key}, {value})")
    
if __name__ == "__main__":
    main()

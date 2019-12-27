#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, param1):
        self.start = param1
    
    def write(self, string):
        print(self.start+string)
    
def main():
    p = Prepend("+++ ")
    x = p.write("Hello")
    
if __name__ == "__main__":
    main()

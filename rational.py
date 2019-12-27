#!/usr/bin/env python3

import math
from fractions import Fraction

class Rational(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        list1 = str(self).split("/")
        list2 = str(other).split("/")
        result = float(eval(str(self)+"+"+str(other)))
        a = int(list1[1])*int(list2[1])
        b = int(result*a)
        return Rational(b,a)        
    
    def __sub__(self,other):
        list1 = str(self).split("/")
        list2 = str(other).split("/")
        result = float(eval(str(self)+"-"+str(other)))
        a = int(list1[1])*int(list2[1])
        b = int(result*a)
        return Rational(b,a)     
    
    def __mul__(self,other):
        list1 = str(self).split("/")
        list2 = str(other).split("/")
        a = int(list1[0])*int(list2[0])
        b = int(list1[1])*int(list2[1])
        return Rational(a,b)
    
    def __truediv__(self,other):
        list1 = str(self).split("/")
        list2 = str(other).split("/")     
        a = int(list1[0])*int(list2[1])
        b = int(list1[1])*int(list2[0])
        return Rational(a,b)
    
    def __eq__(self,other):
        return float(eval(str(self))) == float(eval(str(other)))
        
    def __gt__(self,other):
        return float(eval(str(self))) > float(eval(str(other)))
        
    def __lt__(self,other):
        return float(eval(str(self))) < float(eval(str(other)))
    
    def __str__(self):
        return f"{self.x}/{self.y}"
    
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()

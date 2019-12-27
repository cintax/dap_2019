#!/usr/bin/env python3

def transform(s1, s2):
    list1 = list(map(int, s1.split()))
    list2 = list(map(int, s2.split()))
    list3 = zip(list1,list2)
    result = list(map(lambda x: x[0]*x[1], list3))
    return result

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def reverse_dictionary(d):
    reverse = dict()
    temp = []
    for key in d:
        value = d[key]
        if type(value) == list:
            for i in range(len(value)):
                reverse[value[i]] = []
        else:
            reverse[value] = []
    
    print(reverse)
    
    for key in d:
        value = d[key]
        if type(value) == list:
            for i in range(len(value)):
                temp.append(value[i])
        else:
            temp.append(value)
            
    temp = set(temp)
        
    for x in temp:
        print(x)
        for key in d:
            if x in d[key]:
                reverse[x].append(key)
                

            
    return reverse

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()

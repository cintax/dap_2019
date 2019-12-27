#!/usr/bin/env python3

def detect_ranges(T):
    L = sorted(T)
    result = []
    temp = 0
    parity = False
    for i in range(len(L)):
        if i == 0:
            continue
        
        if L[i] == L[i-1] + 1 and parity is True:
            temp = temp + 1
            print("true",temp)
            parity = True
            if i == len(L)-1:
                result.append((L[i-1]-temp, L[i-1]+1))
        elif L[i] != L[i-1] + 1 and parity is True:
            result.append((L[i-1]-temp, L[i-1]+1))
            parity = False
            temp = 0
            if i == len(L)-1:
                result.append(L[i])
                print(temp)
        elif L[i] != L[i-1] + 1 and parity is False:
            result.append(L[i-1])
            if i == len(L)-1:
                result.append(L[i])
                print(temp)            
        elif L[i] == L[i-1] + 1 and parity is False:
            temp = temp + 1
            print("false",temp)
            parity = True
            if i == len(L)-1:
                result.append((L[i-1], L[i]+1))
                
    return result
        
def main():
    T = [-86, -65, -60, -45, 32, 44, 48, 74, 82, 83]
    result = detect_ranges(T)
    print(T)
    print(result)

if __name__ == "__main__":
    main()

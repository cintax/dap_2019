#!/usr/bin/env python3

def word_frequencies(filename="src/alice.txt"):
    result = {}
    with open(filename,"r") as f:
        
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                x = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                result[x] = ""

        counter = 0        
        for key in result:
            for line in lines:
                words = line.split()
                for word in words:
                    x = word.strip("""!"#$%&'()*,-./:;?@[]_""")
                    if x == key:
                        counter += 1
                        
            result[key] = counter
            counter = 0
                
    return result
    
def main():
    print(word_frequencies())

if __name__ == "__main__":
    main()

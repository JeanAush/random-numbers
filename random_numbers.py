"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the                                                                
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""
#Jean Esther.py
import random
def main():
    MIN_RANDOM=0  #the minimum number that should be printed.
    MAX_RANDOM=100  #the maximum number thst should be printed.
    #the number of times the numbers should be printed.
    for i in range(10):
        print(random.randint(MIN_RANDOM,MAX_RANDOM))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

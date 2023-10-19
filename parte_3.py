import os
import sys
import readchar

def clear_and_print(n):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(n)

def main():
    n = 0

    while n <= 50:
        clear_and_print(n)
        
        key = readchar.readkey()

        if key == 'n':
            n += 1

if __name__ == "__main__":
    main()
             
    
#!/usr/bin/python3

import time

def user_input():
    print("Enter the check digit integer.")
    the_values = int(input(">> "))
    
    the_values = list(str(the_values))
        
    check_digit(the_values)



def check_digit(the_values):
    odd_values = 0
    even_values = 0
    final_digit = int(the_values[len(the_values) - 1])

    start = time.perf_counter()

    for i in range(len(the_values) - 1):
        if (i + 1) % 2 != 0:
            odd_values += int(the_values[i])
        else:
            even_values += int(the_values[i])

    the_modulo = ((even_values * 3) + odd_values) % 10
    the_check_digit_value = 10 - the_modulo
    
    end = time.perf_counter()

    if the_check_digit_value == final_digit:
        print("\nValid checksum value.\n")
    else:
        print("\nInvalid checksum value.\n")

    print(f"Time to execute the code: {end - start}")



def main():
    try:
        user_input()
    
    except ValueError:
        print("INAPPROPRIATE ARGUMENT VALUE (OF CORRECT TYPE).")
    
    except KeyboardInterrupt:
        print("\nKEYBOARD INTERRUPT!\nPROGRAM INTERRUPTED BY USER!")



if __name__ == "__main__":
    main()

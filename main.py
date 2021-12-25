# ------------- Packages ---------------


import string
import random


# --------- Global Variables -----------


s=[]

# --------- Functions -----------


def initial():
    # Set global variables
    global s
    # For abcdefghijklmnopqrstuvwxyz
    s1 = string.ascii_lowercase
    # For ABCDEFGHIJKLMNOPQRSTUVWXYZ
    s2 = string.ascii_uppercase
    # For 0123456789
    s3 = string.digits
    # For !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    s4 = string.punctuation
    # Adding everything to one List
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))  


def main():
    # Preparing the list
    initial()
    # Checking if the list is valid
    try:
        plen = int(input("Enter password length\n"))
        # Checking if the length is above 0 and below 70 
        if((plen<=0)or(plen>70)):
            print("Enter a value between 1 and 70")
        else:
            # Sending the randomly generated password 
            print("".join(random.sample(s,plen)))
    except ValueError:
        print("That was not an integer value.")


# ------------ Start Execution -------------


# Execute the Generator
main()
    
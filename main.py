from src.caseA import *
from src.caseB import *
from src.caseC import *


"""
access for the main program
"""
if __name__ == '__main__':
    print("This is a program for control system design simulation")
    choice = input("We have three different ways to do simulations, choose A, B, or C: ")
    if choice == 'A' or choice == 'a':
        approach = case_a()
        approach.case_a_run()
    elif choice == 'B' or choice == 'b':
        approach = case_b()
        approach.case_b_run()
    elif choice == 'C' or choice == 'c':
        approach = case_c()
        approach.case_c_run()
    else:
        print("Wrong input, please check the input and restart the program.")

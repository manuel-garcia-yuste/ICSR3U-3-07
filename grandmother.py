#!/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : October 2019
# This program uses Compound Boolean Expressions


def main():
    # this funcitions use the Compound Boolean Expressions

    # input
    age = int(input("Entrer your age:"))
    print("")

    # process & output
    if age >= 25 and age <= 45:
        print("You can date my grandchild!")
    else:
        print("You can´t date my grandchild")


if __name__ == "__main__":
    main()

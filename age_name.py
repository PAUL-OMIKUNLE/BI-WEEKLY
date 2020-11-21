#!/usr/bin/env python3
"""
Author : Me <paul.omikunle@gmail.com>
Date   : today
Purpose: To greet a user and Provide  detailed age Info
Note: The shebang line (usr/bin/env) tells the Operating system which
program to use to execute this program (python3).
"""

import argparse #  importing the argparse module to use it. 

""" 
We define a get_args function that holds the command-line
arguments we need for the program 
"""
def get_args():#defining the arguments, stating the variable age, to be used the main
    
    """
    The parser below will help figure out
    all the arguments. The
    description appears in
    the help message.
    """
    parser = argparse.ArgumentParser(
        description='can we get to know you',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    """
    Telling the parser to
    expect a required name argument that will be the
    object of our greeting.
    """
    parser.add_argument('name',
                        metavar='name',
                        help='Its a must you type in your name',
                        type=str,
                        nargs='+')

    """
    Telling the parser to
    expect a required age argument """
    parser.add_argument('age',
                        help='age is required',
                        metavar='age',
                        type=int)

    """
    We ask the parser to parse any
    arguments to the program. """
    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main program s"""

    args = get_args() # get_args() function to get the defined arguments above into the main


    date_of_birth = (2020 - args.age)  # this is used to get the user's date of birth
    age_group = str()  #this is used to create a variable that will hold the user's age group
    year = 'years'  # define a year string

    """
    if else conditions for age grouping
    """
    if args.age <= 1:
        age_group = 'Infant'
        year = year.replace('s', '') # if user age is less than one, say 'year' not 'years' old
    elif args.age <= 11:
        age_group = 'Child'
    elif args.age <= 17:
        age_group = 'Teen'
    elif (args.age >= 18) & (args.age <= 64):
        age_group = 'Adult'
    elif args.age >= 65:
        age_group = 'Elder'

    """a or an for the age classification"""
    article = f'an' if age_group[0].lower() in 'aeiou' else 'a' 


    """Get past, current and future age"""
    decade_ago = (2020 - 10) # Year decade ago
    age_decade_ago = (args.age - 10) # age decade ago
    current_year = 2020 # Current year


    """display user info using the above conditions"""
    print(f'Hello', f' '.join(args.name), f'you are {args.age} {year} old!') # greet the user, tell his age
    print(f'You were born in the year {date_of_birth}.') # Tell the user his/her date of birth 
    print(f'You are {article} {age_group}.') # Tell the user his age group for his current age
    print(f'In {decade_ago}, you were {age_decade_ago}') # Tell the user his age a decade ago


    """display user age for next 10,20,30, 40 and 50 years"""
    print(f'In {current_year + 10}, you will be {args.age + 10}') # shows user his age in ten years time
    print(f'In {current_year + 20}, you will be {args.age + 20}') # shows  the user his age in twenty years time
    print(f'In {current_year + 30}, you will be {args.age + 30}') # shows  the user his age in thirty years time
    print(f'In {current_year + 40}, you will be {args.age + 40}') # shows  the user his age in forty years time
    print(f'In {current_year + 50}, you will be {args.age + 50}') # shows  the user his age in fifty years time

"""
setting __name__ (module name) to “__main__”, to identify recognize the module, so it can be applied.

"""
if __name__ == '__main__':
    main()

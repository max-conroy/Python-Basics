# Simple Python functions for the Per Scholas Cloud DevOps program and uploaded from Git
# Written by Maximilian Conroy
# 11/24/2021

def convert_celsius(fahr):
    # Program to convert Fahrenheit to Celsius
    cel = (5 / 9) * (fahr - 32)
    print("It is {:.1f} degrees celsius.".format(cel))


def calc_tax(cost):
    # Program to find NY sales tax on a purchase
    tax = cost * 8.875
    tax = tax * .01
    print("Your NY sales tax is {:.2f}: ".format(tax))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_celsius(33)
    calc_tax(100)

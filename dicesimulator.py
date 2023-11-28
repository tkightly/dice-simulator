"""
dicesimulator.py
"""

import time
import sys
import argparse
import itertools
import matplotlib.pyplot as plt

def main(sides, quantity):

    """
    a simple function to calculate the probability of getting a particular dice sum when for
    xdy, where x is the quantity of dice to be rolled and y is the number of sides.
    """

    # Check paramters are present and convert into integers
    if sides:
        sides = int(sides)
    else:
        print("No parameter specified for sides. Quitting...")
        sys.exit()

    if quantity:
        quantity = int(quantity)
    else:
        print("No parameter specified for quantity. Quitting...")
        sys.exit()

    # We'll time how long it takes to execute, so start a timer
    start_time = time.time()

    print(f"Rolling {sides}d{quantity}")

    # Use the itertools module to get all possible combinations of the rolls
    combinations = list(itertools.product(range(sides), repeat=quantity))

    # This will be used to store the calculated total of each combination
    outcomes_list = []

    # These are used to store the values for the X and Y axix
    report_outcome = []
    report_probability = []

    # Loop through each possible combination, work out the sum and append to sum_outcome
    for outcome in combinations:
        sum_outcome = 0

        for value in outcome:
            sum_outcome = sum_outcome + value + 1

        outcomes_list.append(sum_outcome)

    # desired_outcome is each possible roll. Loop through each and count how many times that roll
    # occurs, work out the probability, then append it to the Y axis
    i = 0
    for desired_outcome in range(quantity, (sides * quantity + 1)):
        i += 1
        print(f"Working on outcome {i} of {sides * quantity + 1 - quantity}")
        incidents = 0
        report_outcome.append(desired_outcome)

        for outcome in outcomes_list:
            if desired_outcome == outcome:
                incidents += 1

        probability = incidents/(len(combinations))

        report_probability.append(probability)

    print("Execution took ", round(time.time() - start_time, 2), "seconds")

    # Output the bar chart
    plt.bar(report_outcome, report_probability)
    plt.title('Probablity')
    plt.xlabel('Outcome')
    plt.ylabel('Probability')
    plt.show()

if __name__ == '__main__':

    # parse parameters from command line
    parser=argparse.ArgumentParser()

    # configure command line parameters
    parser.add_argument("--sides", help="How many sides the die has")
    parser.add_argument("--quantity", help="How many dice you wish to roll")
    args=parser.parse_args()

    main(args.sides, args.quantity)

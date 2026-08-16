"""
dicesimulator.py
"""

import time
import sys
import argparse
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

    print(f"Rolling {quantity}d{sides}")

    # Build up the distribution of the running total one die at a time, instead of
    # enumerating every one of the sides**quantity possible dice combinations.
    #
    # counts[k] holds the number of ways to reach a running total of k using the dice
    # rolled so far. Rolling one more die convolves counts with the single-die
    # distribution (each existing total can be extended by any of the die's faces).
    # This keeps the work polynomial in sides * quantity rather than exponential in
    # quantity.

    # After 1 die, each face 1..sides has exactly one way to occur.
    counts = [0] + [1] * sides  # index 0 unused, indices 1..sides = 1 way each

    for die in range(2, quantity + 1):
        print(f"Adding die {die} of {quantity}")
        max_total = die * sides
        new_counts = [0] * (max_total + 1)

        for prev_total in range(die - 1, (die - 1) * sides + 1):
            ways = counts[prev_total]
            if ways == 0:
                continue
            for face in range(1, sides + 1):
                new_counts[prev_total + face] += ways

        counts = new_counts

    total_combinations = sides ** quantity

    # These are used to store the values for the X and Y axix
    report_outcome = list(range(quantity, sides * quantity + 1))
    report_probability = [counts[outcome] / total_combinations for outcome in report_outcome]

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

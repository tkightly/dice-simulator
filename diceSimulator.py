import math, time, sys, argparse
import matplotlib.pyplot as plt
import itertools

def main(sides, quantity):

    # Check paramters are present and convert into integers
    if (sides):
        sides = int(sides)
    else:
        print("No parameter specified for sides. Quitting...")
        sys.exit()

    if (quantity):
        quantity = int(quantity)
    else:
        print("No parameter specified for quantity. Quitting...")
        sys.exit()

    # We'll time how long it takes to execute, so start a timer
    startTime = time.time()

    print("Rolling %sd%s" % (quantity, sides))

    # Use the itertools module to get all possible combinations of the rolls 
    combinations = list(itertools.product(range(sides), repeat=quantity))
    
    # This will be used to store the calculated total of each combination
    outcomesList = []
    
    # These are used to store the values for the X and Y axix
    reportOutcome = []
    reportProbability = []

    # Loop through each possible combination, work out the sum and append to sumOutcome
    for outcome in combinations:
        sumOutcome = 0

        for value in outcome:
            sumOutcome = sumOutcome + value + 1

        outcomesList.append(sumOutcome)

    # desiredOutcome is each possible roll. Loop through each and count how many times that roll
    # occurs, work out the probability, then append it to the Y axis
    i = 0
    for desiredOutcome in range(quantity, (sides * quantity + 1)):
        i += 1
        print("Working on outcome %s of %s" % (i, sides * quantity + 1 - quantity))
        incidents = 0
        reportOutcome.append(desiredOutcome)

        for outcome in outcomesList:
            if desiredOutcome == outcome:
                incidents += 1

        probability = incidents/(len(combinations))

        reportProbability.append(probability)

    print("Execution took ", round(time.time() - startTime, 2), "seconds")

    # Output the bar chart
    plt.bar(reportOutcome, reportProbability)
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
    

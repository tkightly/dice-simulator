import math
import matplotlib.pyplot as plt
import itertools


def main():
    sides = 6
    quantity = 3

    print("Rolling %sd%s" % (quantity, sides))
    #print("Maximum possible roll is %s" % (sides * quantity))
    #print("Minimum possible roll is %s" % (quantity))

    combinations = list(itertools.product(range(sides), repeat=quantity))

    reportOutcome = []
    reportProbability = []

    for desiredOutcome in range(quantity, (sides * quantity + 1)):
        incidents = 0
        reportOutcome.append(desiredOutcome)

        for outcome in combinations:
            sumOutcome = 0

            for value in outcome:
                sumOutcome = sumOutcome + value + 1

            if sumOutcome == desiredOutcome:
                incidents += 1

        probability = incidents/(len(combinations))

        reportProbability.append(probability)

        # print('Probability to get a %s is %s: total is %s/%s' %
        #      (desiredOutcome, round(probability, 4), incidents, len(combinations)))

    plt.bar(reportOutcome, reportProbability)
    plt.title('Probablity')
    plt.xlabel('Outcome')
    plt.ylabel('Probability')
    plt.show()


if __name__ == '__main__':

    main()

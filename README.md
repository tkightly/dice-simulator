# dice-simulator
This is my first attempt at doing a semi-useful project with python, a simple function to calculate the probability of getting a particular dice sum when for xdy, where x is the quantity of dice to be rolled and y is the number of sides.

Also generates a pretty bar chart

## V2.0
Optimsed the code by only working out the sum of each combination once, instead of every for every possible outcome. Runs significantly faster, although it still took 548 seconds to calculate 10d6 on my i5-1038NG7 CPU @ 2.00GHz. Old version available for comparison.
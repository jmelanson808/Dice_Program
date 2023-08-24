import random
import math

# Simulates 4 six-sided die rolls, returns True if any resulted in a 6.
def roll_dice(num_dice):
    six_exists = False
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        # print(roll)
        if(roll == 6) :
            six_exists = True
    return six_exists

# Rolls a batch of roll_dice() sets, returns the number of sets that contained at least one 6.
def roll_set(num_sets) : 
    six_check = False
    win_count = 0
   
    for _ in range(num_sets) : 
        six_check = False
        six_check = roll_dice(4)
        if(six_check == True) :
            win_count += 1
    return win_count
    
# Runs a number of roll_set() batches, outputting the results.
def roll_batch(num_tests, num_sets) :
    counter = 0
    ratio = 0.0
    print('Displaying number of sets that contained at least one 6 :')
    for _ in range(num_tests) :
        result = roll_set(num_sets)
        print(result, end = " ")
        if(result > int(num_sets / 2)) :
            counter += 1
    ratio = math.ceil(counter / num_tests * 10000) / 100
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(ratio, '% of batches resulted in a win-rate over 50%')

# Enter the amount of batches you want to test, followed by the amount of sets in each batch.
# Each set simulates rolling four 6-sided dice.
roll_batch(45, 1000)

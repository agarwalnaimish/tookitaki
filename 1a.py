import random

def roll_at_max_k_times(dice_values, k):

    value = 0
    for _ in range(k):

        value = random.choice(dice_values)

        if random.random() <= (1.0 / k):
            break

    return value

def roll_experiment(n, k, dice_values):

    sum_win_amount = 0

    for _ in range(n):
        sum_win_amount += roll_at_max_k_times(dice_values, k)

    expected_win_amount = sum_win_amount / n

    return expected_win_amount

def main():

    # values which dice can take
    dice_values = [1, 2, 3, 4, 5, 6]

    # roll dice 3 times at max
    # and either stop at a value and take it as a dollar amount or 
    # roll once again
    # repeat the experiment a large number of times

    n = 100000
    k = 3
    expected_win = roll_experiment(n, k, dice_values)
    print("expected win amount =", expected_win)
    
if __name__ == "__main__":
    main()

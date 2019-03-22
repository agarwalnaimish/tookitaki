import random

def roll_at_max_M_times(numbers, M):

    value = 0
    for _ in range(M):

        value = random.choice(numbers)

        if random.random() <= (1.0 / M):
            break

    return value

def roll_experiment(n, M, numbers):

    sum_win_amount = 0

    for _ in range(n):
        sum_win_amount += roll_at_max_M_times(numbers, M)

    expected_win_amount = sum_win_amount / n

    return expected_win_amount

def expected_winnings(N, M):

    # list of numbers
    numbers = list(range(1, N + 1))

    # roll M times at max
    # and either stop at a value and take it as a dollar amount or 
    # roll once again
    # repeat the experiment a large number of times

    n = 100000
    expected_win = roll_experiment(n, M, numbers)
    
    return expected_win

if __name__ == "__main__":
    N = 100
    M = 5
    expected_win = expected_winnings(N, M)
    print("expected win amount =", expected_win)

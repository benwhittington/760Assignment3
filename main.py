import numpy as np


def dp(initial_inventory, print_output=False):
    no_weeks = 13
    max_inventory = 10  # a
    max_sales = 5  # u_n
    prices = [1, 2, 3, 1, 2, 2, 5, 4, 1, 1, 4, 4, 2]  # pi
    production = [2, 1, 2, 1, 2, 2, 2, 1, 2, 3, 2, 1, 0]  # w

    reward = [[-1 for _ in range(max_inventory + 1)] for _ in range(no_weeks + 1)]
    reward[0] = [-1 for _ in range(max_inventory + 1)]
    reward[0][initial_inventory] = 0  # zero starting reward

    phi = [[-1 for _ in range(max_inventory + 1)] for _ in range(no_weeks + 1)]  # predecessor

    for n in range(no_weeks):  # every stage
        for x in range(max_inventory + 1):  # every inventory level

            if reward[n][x] == -1:  # if state (n, x) is unreachable
                continue

            available_for_sale = x + production[n]

            for s in range(min((max_sales + 1, available_for_sale + 1))):  # every sale in A_n(x)
                x_next = available_for_sale - s  # x_next, inventory in next stage

                if x_next > max_inventory:  # must discard excess stock
                    x_next = max_inventory

                r = prices[n] * s

                # check if current choice of s is better than alternative path to next (stage, inventory)
                if r + reward[n][x] > reward[n+1][x_next]:
                    reward[n+1][x_next] = r + reward[n][x]
                    phi[n+1][x_next] = x  # store predecessor info

    # backtrack to compute best decisions, start with maximum reward
    best_i = np.argmax(reward[-1])
    decisions = []

    for p in reversed(phi):
        decisions.append(best_i)
        best_i = p[best_i]

    decisions.reverse()

    if print_output:
        print(np.matrix(phi))
        print("---------------")
        print(np.matrix(reward))

    return decisions


def main():
    initial_inventory = 9
    decisions = dp(initial_inventory, print_output=False)

    print(decisions)


if __name__ == "__main__":
    # [0, 0, 4, 7, 4, 2, 6, 9, 7, 5, 4, 7, 10, 9]

    main()

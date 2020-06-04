import numpy as np


def transition(x, max_sales, production, price, max_inventory):
    transitions = []
    rewards = []
    available_for_sale = x + production

    for s in range(min((max_sales + 1, available_for_sale + 1))):

        inventory = available_for_sale - s

        if inventory > max_inventory:
            inventory = max_inventory

        transitions.append(inventory)
        rewards.append(price * s)

    return transitions, rewards


def dp(initial_inventory):
    no_weeks = 13
    max_inventory = 10  # a
    max_sales = 5  # u_n
    prices = [1, 2, 3, 1, 2, 2, 5, 4, 1, 1, 4, 4, 2]
    production = [2, 1, 2, 1, 2, 2, 2, 1, 2, 3, 2, 1, 0]

    reward = [[-1 for _ in range(max_inventory + 1)] for _ in range(no_weeks + 1)]
    reward[0] = [-1 for _ in range(max_inventory + 1)]
    reward[0][initial_inventory] = 0  # zero cost at starting node inventory

    phi = [[-1 for _ in range(max_inventory + 1)] for _ in range(no_weeks + 1)]

    for n in range(no_weeks):
        for x in range(max_inventory + 1):
            if reward[n][x] == -1:  # if state (n, x) is unreachable
                continue

            next_inventory, rewards_n = transition(x, max_sales, production[n], prices[n], max_inventory)

            for i, r in zip(next_inventory, rewards_n):
                if r + reward[n][x] > reward[n+1][i]:
                    reward[n+1][i] = r + reward[n][x]
                    phi[n+1][i] = x

    decisions = []
    best_i = np.argmax(reward[-1])

    for p, r in zip(reversed(phi), reversed(reward)):
        decisions.append(best_i)
        best_i = p[best_i]

    print(decisions)
    print("---------------")
    print(np.matrix(phi))
    print("---------------")
    print(np.matrix(reward))


def main():
    initial_inventory = 9
    dp(initial_inventory)


if __name__ == "__main__":
    main()

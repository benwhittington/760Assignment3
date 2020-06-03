import numpy as np

def dp():
    no_weeks = 13
    inventory_space = 10  # a
    max_sales = 5  # u_n
    prices = [1, 2, 3, 1, 2, 2, 5, 4, 1, 1, 4, 4, 2]
    production = [2, 1, 2, 1, 2, 2, 2, 1, 2, 3, 2, 1, 0]

    cost = np.zeros((max_sales, no_weeks))

    for n in range(no_weeks):



def main():
    dp()


if __name__ == "__main__":
    main()

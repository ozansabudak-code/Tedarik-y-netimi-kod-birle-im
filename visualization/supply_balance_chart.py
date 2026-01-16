import matplotlib.pyplot as plt

def visualize_supply_balance(excess, shortages):
    categories = ['Excess', 'Shortages']
    values = [sum(excess.values()), sum(shortages.values())]

    plt.bar(categories, values)
    plt.title('Supply Balance')
    plt.ylabel('Quantity')
    plt.show()

def calculate_supply_balance(supplies):
    excess = {}  # Store excess supplies
    shortages = {}  # Store shortages
    for item, quantity in supplies.items():
        if quantity > optimal_supply:
            excess[item] = quantity - optimal_supply
        elif quantity < optimal_supply:
            shortages[item] = optimal_supply - quantity
    return excess, shortages

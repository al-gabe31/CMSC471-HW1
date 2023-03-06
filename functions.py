# Name: Gabe Aquino
# ID: LQ90575
# Email: lq90575@umbc.edu

# This is where all my functions will go that I wll use for question 4 on HW1

import random

# Returns a random decimal from [0, 1]
def rand_percent():
    value = random.randint(0, 100)
    value /= 100
    return value

# Returns a random price of chips in a given day
def price():
    base = 5
    variation = random.randint(-3, 3)

    return base + variation

# Returns a random number of chips eaten
def consumption():
    value = rand_percent()

    if value < 0.25:
        return random.choice([0, 1]) # Returns randomly 0 or 1
    elif value < 0.75:
        return random.choice([2, 3, 4]) # Returns randomly 2, 3, or 4
    else:
        return random.choice([5, 6]) # Returns randomly 5 or 6

# TYPE      VAR     DESCRIPTION
# int       s0      initial supply of bags of chips
# int       T       time horizon
# string    type    type of belief/average price per unit, viz. exact or approcimate
# int       k       length of the history that the agent can remember
# float     alpha   a constant to be multiplied with the current belief while comparing it with the current price
# int       u       upper limit of the supply of bags of chips, and
# int       l       lower limit of the supply of bags of chips
def buyChips(s0, T, type, k, alpha, u, l):
    s = [0 for i in range(T)] # supply of bags of chips over time
    p = [0 for i in range(T)] # price per unit of bags of chips over time
    c = [0 for i in range(T)] # consumption of bags of chips over time
    b = [0 for i in range(T)] # belief/average price per unit of bags of chips over time
    d = [0 for i in range(T)] # demand for bags of chips over time
    e = [0 for i in range(T)] # expenditure/money spent on buying bags of chips over time

    # Returns the average of prices using the exact method
    def exact_average(t):
        total = 0
        start = -1
        end = t

        if t < k:
            start = 0
        else:
            start = t - k + 1

        for i in range(start, end + 1):
            total += p[i]

        return round(total / (end - start + 1), 2) # Might as well round it to 2 decimals

    for t in range(T):
        # 1. Update Supply
        if t == 0:
            s[0] = s0
        else:
            # Current supply = past supply - consumption + demand
            s[t] = s[t - 1] - c[t - 1] + d[t - 1]
        
        # 2. Update Price
        p[t] = price() # Random price for p[t]
    
        # 3. Update Consumption
        c[t] = consumption() # Random consumption for c[t]

        # 4. Update Belief/Average price
        b[t] = exact_average(t)
        
        # 5. Update Demand
        if p[t] < alpha * b[t]:
            d[t] = max(u - s[t], 0)
        else:
            d[t] = max(l - s[t], 0)
        
        # 6. Update Expenditure
        e[t] = d[t] * p[t]
    
    return s, p, c, b, d, e # Final output lists
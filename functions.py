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
    s = [s0] # supply of bags of chips over time
    p = [0] # price per unit of bags of chips over time
    c = [0] # consumption of bags of chips over time
    b = [0] # belief/average price per unit of bags of chips over time
    d = [0] # demand for bags of chips over time
    e = [0] # expenditure/money spent on buying bags of chips over time

    t = 1  # Time variable

    # Returns the average price from the past k time states
    # Needs work
    def averagePrice():
        if type == "exact":
            total = 0

            # t <= k
            if t <= k:
                for i in range(1, t + 1):
                    total += p[i]
                
                total /= t
            
            # t > k
            else:
                for i in range(t - k + 1, t):
                    total += p[i]
                
                total /= k
            
            return total
        elif type == "approximate":

            # t == 1
            if t == 1:
                return b[0] # Returns the first belief state
            
            # t <= k
            elif t <= k:
                return b[t - 2] + ((p[t - 1] - b[t - 2]) / t)
            
            # t > k
            else:
                return b[t - 2] + ((p[t - 1] - p[t - k]) / k)
        else:
            print("ERROR - INVALID type VALUE")
            return -1
    
    return s, p, c, b, d, e # Final output lists
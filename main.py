import math

def calculate_target(curlvl, targetlvl, win_points, loss_points, win_perc):
    required_points = [50, 350, 750, 1250, 1850, 2750, 3750, 4850, 6050, 7350, 8750, 10450, 12250, 14150, 16150, 18250, 20450, 22950, 25550, 28250, 31050, 33950, 36950, 40050, 46850, 50850, 55050, 59450, 64050, 72050]

    if targetlvl > len(required_points):
        return "Target level out of range"
    if curlvl > targetlvl:
        return "Current level is higher than target level"
    curxp = required_points[curlvl -1]
    xprequired = required_points[targetlvl -1]
    
    # Total XP required to reach goal
    remaining_points = xprequired - curxp

    games = math.ceil(remaining_points / (win_points * win_perc + loss_points * (1 - win_perc)))

    return "Games: {}".format(games)

curlvl = int(input("Enter your current lvl: "))
targetlvl = int(input("Enter the target lvl: "))
win_perc = float(input("Your win% (0.0 to 1.0). 50% is 0.5, 30% 0.3 etc: "))

print(calculate_target(curlvl, targetlvl, 50, 25, win_perc))

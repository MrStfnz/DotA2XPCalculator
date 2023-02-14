import math
import PySimpleGUI as sg

# Set my PySimpleGUI Layout
sg.theme('Dark Black')
layout = [  [sg.Text('Current lvl:', size =(12, 1)), sg.InputText()],
            [sg.Text('Target lvl:', size =(12, 1)), sg.InputText()],
            [sg.Text('Win percentage:', size =(12, 1)), sg.InputText('between 0.0 - 1.0 where 10% = 0.1 and 20% = 0.2 etc')],
            [sg.Text(size =(30, 0), key ='-OUTPUT-')],
            [sg.T(), sg.Button('Calculate', focus = True, size=20), sg.Quit(size=20)]]

window = sg.Window('DotA2 XP Calculator', layout)


def calculate_target(curlvl, targetlvl, win_points, loss_points, win_perc):
    required_points = [50, 350, 750, 1250, 1850, 2750, 3750, 4850, 6050, 7350, 8750, 10450, 12250, 14150, 16150, 18250, 20450, 22950, 25550, 28250, 31050, 33950, 36950, 40050, 46850, 50850, 55050, 59450, 64050, 72050]

    if targetlvl > len(required_points):
        return "Target level out of range"
    if curlvl > targetlvl:
        return "Current level is higher than target level"
    elif curlvl < 1:
        return "Please enter a level between 1 - 30"
    if win_perc > 1:
        return "Please use a value between 0.0 - 1.0\n0% = 0.0\n25%=0.25\n50%=0.5\n69%=0.69 etc."

    curxp = required_points[curlvl -1]
    xprequired = required_points[targetlvl -1]

    # Total XP required to reach goal
    remaining_points = xprequired - curxp

    games = math.ceil(remaining_points / (win_points * win_perc + loss_points * (1 - win_perc)))

    return "Games required to goal: {}".format(games)

while True:
    event, values = window.read(timeout = 10)
    if event in (None, 'Quit'):
        break
    elif event == 'Calculate':
        try:
            window["-OUTPUT-"].update(calculate_target(int(values[0]), int(values[1]), 50, 25, float(values[2])))
        except ValueError as e:
            window["-OUTPUT-"].update("Please use a value between 0.0 - 1.0\n0%=0.0\n25%=0.25\n50%=0.5\n69%=0.69 etc.")
window.close()

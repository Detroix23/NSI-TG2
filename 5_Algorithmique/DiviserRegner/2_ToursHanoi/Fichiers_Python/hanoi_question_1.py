from hanoi_vision import Visualisation_hanoi

tour0 = [3,2,1]
tour1 = []
tour2 = []
hanoi = [tour0, tour1, tour2]

print(hanoi)

v = Visualisation_hanoi(hanoi)
v.fin()

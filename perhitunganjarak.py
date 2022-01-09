import numpy as np

def jarak(matrikJarak, rute):
    total = 0
    for i in range(len(rute)-1):
        total += matrikJarak[rute[i]][rute[i+1]]
    return total

matrikJarak = np.array([
[0, 330, 0, 0, 0, 690, 0, 0], # A
[330, 0, 250, 0, 280, 0, 0, 0], # B
[0, 250, 0, 86, 0, 0, 0, 0], # C
[0, 0, 86, 0, 80, 0, 0, 203], # D
[0, 280, 0, 80, 0, 0, 200, 0], # E
[600, 0, 0, 0, 0, 0, 140, 0], # F
[0, 0, 0, 0, 200, 140, 0, 95], # G
[0, 0, 0, 203, 0, 0, 95, 0] # H
               ])

rute = [0, 1, 4, 3, 7] # A->B->E->D->H
print("Rute ", rute)
print("Jarak ",jarak(matrikJarak, rute))


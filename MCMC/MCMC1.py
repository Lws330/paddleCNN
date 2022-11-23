import numpy as np
matrix = np.matrix([[0.9,0.075,0.025],[0.15,0.8,0.05],[0.25,0.25,0.5]], dtype=float)
for i in range(10):
    matrix = matrix*matrix
    print("Current round:", i+1)
    print(matrix)
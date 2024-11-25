import numpy as np
# vec=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# mat=vec.reshape((-1,1))
# print(mat)
M = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [0, 0, 0]])
print(M[2:4,1:3])

import numpy as np
def penjumlahan(M1,M2):
    M3 = np.empty(M1.shape)
    nbaris, nkolom = M1.shape
    for b in range(nbaris):
        for k in range(nkolom):
            M3[b,k] = M1[b,k] + M2[b,k]
    return M3
def pengurangan(M1,M2):
    M3 = np.empty(M1.shape)
    nbaris, nkolom = M1.shape
    for b in range(nbaris):
        for k in range(nkolom):
            M3[b,k] = M1[b,k] - M2[b,k]
    return M3

def perkalian(M1,M2):
    nbaris = M1.shape[0] # baris matrik 1
    nkolom = M2.shape[1] # kolom matrik 2
    M3 = np.zeros((nbaris, nkolom))
    for b in range(nbaris):
        for k in range(nkolom):
            for i in range(M1.shape[1]): # kolom matrik 1
                M3[b,k] = M3[b,k] + M1[b,i] *  M2[i,k]
    return M3
# sample 
A = np.array([[1, 2],
              [ 4, 5]])
B = np.array([[3, 2],
              [ 1, 2]])
print("A:\n",A)
print("B:\n",B)
print("A+B:\n",penjumlahan(A,B))
print("A-B:\n",pengurangan(A,B))
print("A*B:\n",perkalian(A,B))


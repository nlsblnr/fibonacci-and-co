import numpy as np

# vector representing the first two fibonacci numbers.
start_vector = np.array([[0], [1]])

# change-of-basis matrix from standard basis -> eigenvector basis
P_eigenvec_to_std = np.array(
    [[-1+np.sqrt(5), 1+np.sqrt(5)],
    [2, -2]]
)

# change-of-basis matrix from eigenvector basis -> standard basis
P_std_to_eigenvec = np.linalg.inv(P_eigenvec_to_std)

eigenvectors = [(1+np.sqrt(5))/2, (1-np.sqrt(5))/2]

def fib(n):
    diag_to_the_n_matrix = np.array(
        [[eigenvectors[0]**n, 0],
        [0, eigenvectors[1]**n]]
	)
    result = P_eigenvec_to_std @ diag_to_the_n_matrix @ P_std_to_eigenvec @ start_vector
    
    return result[0]

n = int(input("Calculate the following fibonacci number: "))
print(fib(n))
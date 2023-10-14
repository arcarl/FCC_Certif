import numpy as np


def calculate(l):
    if len(l) < 9:
        raise ValueError("List must contain nine numbers.")
    # Coverting the list into a numpy array 3x3
    m = np.resize(l, (3,3))

    # Creating the requesting dictionary
    d = {"mean": [np.mean(m, axis=0), np.mean(m, axis=1), np.mean(m)],
            "variance": [np.var(m, axis=0), np.var(m, axis=1), np.var(m)],
            "standard deviation": [np.std(m, axis=0), np.std(m, axis=1), np.std(m)],
            "max": [np.max(m, axis=0), np.max(m, axis=1), np.max(m)],
            "min": [np.min(m, axis=0), np.min(m, axis=1), np.min(m)],
            "sum": [np.sum(m, axis=0), np.sum(m, axis=1), np.sum(m)]}

    # Converting the numpy.array values into lists
    ld = {}
    for key, values in d.items():
        ld[key] = [value.tolist() for value in values]
    return ld

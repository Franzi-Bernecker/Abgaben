import numpy as np


def load_data(file_path):
    data_array = np.genfromtxt(file_path, delimiter=',', dtype=None, names=True)

    column_names = data_array.dtype.names
    column_arrays = {column: data_array[column] for column in column_names}

    return column_arrays

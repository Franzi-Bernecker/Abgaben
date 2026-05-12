def load_data(file_path):
    power_data = []

    file = open(file_path) 
    lines = file.readlines() 
    file.close() 

    return lines 

    
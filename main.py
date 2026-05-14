from power_curve import power_curve
from load_data import load_data
from sort import bubble_sort

if __name__ == "__main__":
    data = load_data('activity.csv')
    sorted_power = bubble_sort(data['PowerOriginal'])
    power_curve(sorted_power)
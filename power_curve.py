import matplotlib.pyplot as plt


def power_curve(sorted_power):
    plt.plot(range(len(sorted_power)), sorted_power[::-1])
    plt.xlabel('Duration [s]')
    plt.ylabel('Power [W]')
    plt.title('Power Curve')

    plt.savefig('figures/power_curve.png', dpi=300)
    plt.show()

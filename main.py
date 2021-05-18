import numpy as np
import matplotlib.pyplot as plt

from models.competition import Competition


def main():
    competitors = 20
    simulations = 10000
    results = list()

    for _ in range(simulations):
        competition = Competition(competitors)
        results.append(competition.run())
    
    bins = np.arange(0, competitors, 1)
    data = np.array(results)

    plt.xlim([0, competitors])
    plt.hist(data, bins=bins, alpha=0.5)
    plt.title('Distibution of Final Placement of the Average Joe')
    plt.xlabel('position')
    plt.ylabel('count')

    plt.show()


if __name__ == '__main__':
    main()
import numpy as np
from .base import ComplexSystem


class EpidemicModel(ComplexSystem):

    def __init__(self, population=100000, infected0=10, beta=0.3, gamma=0.1, steps=200):

        super().__init__(steps)

        self.population = population
        self.beta = beta
        self.gamma = gamma

        self.S = population - infected0
        self.I = infected0
        self.R = 0

    def step(self):

        new_infections = self.beta * self.S * self.I / self.population
        new_recoveries = self.gamma * self.I

        self.S -= new_infections
        self.I += new_infections - new_recoveries
        self.R += new_recoveries

    def simulate(self):

        infected = []

        for _ in range(self.n_steps):
            self.step()
            infected.append(self.I)

        return np.array(infected)

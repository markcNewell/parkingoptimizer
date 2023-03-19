from abc import ABC, abstractmethod
from models import Instance
import numpy as np

class GeneticOptimization(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def reproduce(mother: Instance, father: Instance) -> Instance:
        pass

    @abstractmethod
    def selection(population: list[Instance]) -> list[Instance]:
        pass

    @abstractmethod
    def mutate(instance: Instance) -> Instance:
        pass

    @abstractmethod
    def calculate_fitness(population: list[Instance]) -> list[float]:
        pass

    @abstractmethod
    def initialize_population() -> list[Instance]:
        pass

    @abstractmethod
    def log_population(population: list[Instance]) -> None:
        pass

    def main_loop(self, population: list[Instance]) -> list[Instance]:
        fitness = self.calculate_fitness(population)
        parents = self.selection(population, fitness)

        assert parents % 2 == 0
        random_shuffle = np.random.choice(parents, parents, replace=False)

        newPopulation = parents
        for mother, father in zip(random_shuffle[:parents//2], random_shuffle[parents//2:]):
            offspring = self.reproduce(mother, father)
            newPopulation.append(offspring)

        for i, instance in enumerate(newPopulation):
            newPopulation[i] = self.mutate(instance)

        return newPopulation


    def run(self) -> list[Instance]:
        population = self.initialize_population()

        for _ in range(self.iterations):
            newPopulation = self.main_loop(population)
            self.log_population(newPopulation)

            if self.early_stopping(population, newPopulation):
                break
            
            population = newPopulation

        return newPopulation
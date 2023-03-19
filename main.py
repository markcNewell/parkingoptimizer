from go import GeneticOptimization
from models import Instance
import numpy as np
import math

class ParkingOptimization(GeneticOptimization):
    def __init__(self, grid) -> None:
        super().__init__()
        self.grid = grid
        print(self.grid)
    
    def reproduce(mother: Instance, father: Instance) -> Instance:
        pass

    def selection(population: list[Instance]) -> list[Instance]:
        pass

    def mutate(instance: Instance) -> Instance:
        pass

    def calculate_fitness(population: list[Instance]) -> list[float]:
        pass

    def initialize_population(self, n: int) -> list[Instance]:
        return [self.create_instance() for _ in range(n)]

    def get_random_position(self):
        return np.random.randint(0, self.grid.shape[1]), np.random.randint(0, self.grid.shape[0])

    def create_instance(self) -> Instance:
        # 0 depicts a road
        # 1 depicts a space
        # -1 depicts obstacle
        space = [[1,1], [[1],[1]]]
        unavailable = [1,-1]

        for i in range(np.random.randint(0, 10)):

            # Loop until we get a valid random position
            x, y = self.get_random_position()
            while any([x == unavailable, y == unavailable]):
                x, y = self.get_random_position()

            


    def log_population(population: list[Instance]) -> None:
        pass


if __name__ == "__main__":
    grid = np.zeros((10,10))

    ParkingOptimization(grid)
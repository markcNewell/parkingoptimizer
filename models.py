from abc import ABC
import math
import numpy as np

class Instance(ABC):
    def __init__(self) -> None:
        pass

class InstanceParking(Instance):
    def __init__(self, parkingSpaces: list[str]) -> None:
        self.parkingSpaces = parkingSpaces

    def mutate(self, probability: float):
        """Mutation method is just going to be change the location of one of the spaces
        """
        if np.random.random() < probability:
            i = np.random.choice(range(len(self.parkingSpaces)))
            self.parkingSpaces.pop(i)
            self.parkingSpaces.append(create_new_parking_space(self.parkingSpaces))

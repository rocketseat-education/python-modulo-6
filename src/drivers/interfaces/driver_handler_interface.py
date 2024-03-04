from abc import ABC, abstractclassmethod
from typing import List


class DriverHandlerInterface(ABC):

    @abstractclassmethod
    def standard_derivation(self, number: List[float]) -> float:
        pass

    @abstractclassmethod
    def variance(self, number: List[float]) -> float:
        pass

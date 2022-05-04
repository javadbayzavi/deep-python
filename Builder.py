from __future__ import annotations
from abc import ABC, abstractmethod
from ast import JoinedStr

from numpy import product
class BuilderInterface(ABC):
    
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    def buildPart(self,partname) -> None:
        pass

class Builder(BuilderInterface):
    def reset(self) -> None:
        self._product = Product()
    
    def __init__(self) -> None:
        self.reset()
    
    def buildPart(self, partname) -> None:
        self._product.addPart(partname)

    @property
    def product(self) -> Product:
        product = self._product
        return product

class Product():
    def __init__(self) -> None:
        self.parts = []

    def addPart(self,partname):
        self.parts.append(partname)
    
    def getParts(self) -> str:
        return self.parts

class BuildPlanner():
    def __init__(self) -> None:
        self.builder = Builder()

    def BuildWithPlan(self,plan) -> Product:
        if plan == "A":
            self.builder.buildPart("Door")
            self.builder.buildPart("Brake")
            self.builder.buildPart("Wheels")
        else:
            self.builder.buildPart("Door")


if __name__ == "__main__":
    builder = BuildPlanner()
    print(builder.BuildWithPlan("A").getParts())
    print(builder.BuildWithPlan("B").getParts())
    
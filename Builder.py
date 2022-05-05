from __future__ import annotations
from abc import ABC, abstractmethod
from ast import JoinedStr

from numpy import product

#Generic Builder interface for general purpose builder
class BuilderInterface(ABC):
    
    @property
    @abstractmethod
    def product(self) -> ProductInterface:
        pass

    def buildPart(self,partname) -> None:
        pass

#Implementation of a Product builder
class Builder(BuilderInterface):
    def reset(self) -> None:
        self.product = Product()
    
    def __init__(self):
        self.reset()
    
    def buildPart(self, partname) -> None:
        self._product.addPart(partname)

    @property
    def product(self) -> ProductInterface:
        return self._product

    @product.setter
    def product(self,value) -> None:
        self._product = value

#Generic Interface for a configurable product
class ProductInterface:
    def addPart(self,partname) -> None:
        pass
    def getParts(self) -> str:
        pass

#Implementation of a Product that a builder can build
class Product(ProductInterface):
    def __init__(self) -> None:
        self.parts = []

    def addPart(self,partname) -> None:
        self.parts.append(partname)
    
    def getParts(self) -> str:
        return self.parts

#Builder planning engine act as a Abstract Factory to receive a blueprint and build products
class BuildPlanner():
    def __init__(self) -> None:
        self.builder = Builder()

    def BuildWithPlan(self,plan) -> Product:
        self.builder.reset()
        if plan == "A":
            self.builder.buildPart("Door")
            self.builder.buildPart("Brake")
            self.builder.buildPart("Wheels")
        else:
            self.builder.buildPart("Door")

        return self.builder.product
        


if __name__ == "__main__":
    builder = BuildPlanner()
    prod = builder.BuildWithPlan("A")
    print("Blueprint for Product A: " + str(prod.getParts()))
    prod = builder.BuildWithPlan("B")
    print("Blueprint for Product B: " + str(prod.getParts()))
    
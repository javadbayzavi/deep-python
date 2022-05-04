from __future__ import annotations
from abc import ABC, abstractmethod

#A general abstract interface for all type of factory
class AbstractFactoryInterface:
    @abstractmethod
    def create_conceret_entity(self,target) -> entity_interface:
        pass

#Concrete factory class to implement entities
class AbstractFactory(AbstractFactoryInterface):
    def create_conceret_entity(self,target) -> entity_interface:
        if target == "A":
            return conceret_entityA()
        else:
            return conceret_entityB()

#Abstract entity for all sort of classes
class entity_interface:
    def showMyInfo(self) -> str:
        pass

#Conceret class for entity A
class conceret_entityA(entity_interface):
    def showMyInfo(self) -> str:
        return "This message from conceret entity A"

#Conceret class for entity B
class conceret_entityB(entity_interface):
    def showMyInfo(self) -> str:
        return "This message from conceret entity B"

#Client side for testing the implementation
if __name__ == "__main__":
    factory = AbstractFactory()
    entity = factory.create_conceret_entity("A")
    print(entity.showMyInfo())
    entity = factory.create_conceret_entity("B")
    print(entity.showMyInfo())

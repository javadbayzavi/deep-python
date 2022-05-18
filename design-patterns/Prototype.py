from abc import ABC, abstractmethod
import copy

class PrototypeInterface(ABC):
    def print() -> None:
        pass

    @abstractmethod
    def clone()-> None:
        pass

class Prottype(PrototypeInterface):
    def __init__(self,classname,prop1,prop2) -> None:
        self._classname = classname
        self._property1 = prop1
        self._property2 = prop2

    def print(self) -> None:
        print("Class name:" + self._classname + " Property1:" + self._property1 + " Property2:" + self._property2)
    
    def clone(self) -> PrototypeInterface:
        tempproto = Prottype(self._classname + "_cloned", self._property1,self._property2)
        return tempproto

def testPrototype():
    prototyper = Prottype("Prototype","Value1","Value2")
    prototyper.print()
    prototyped = prototyper.clone()
    prototyped.print()

testPrototype()
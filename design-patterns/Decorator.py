from cProfile import run
from types import BuiltinFunctionType


class OperationalModel:
    def runTheContext(self):
        pass

class Operation(OperationalModel):
    def runTheContext(self):
        pass

class UIOperations(Operation):
    def runTheContext(self):
        print('Run the context in UI Operation decore')

class BusinessOperation(Operation):
    def runTheContext(self):
        print('Run the context in Business Operation decore')

class Decorator():
    wrappedContext : Operation
    def __init__(self, context : Operation) -> None:
        self.wrappedContext = context
    def runTheContext(self):
        self.wrappedContext.runTheContext()
    def changeDecore(self, context: Operation):
        self.wrappedContext = context

ui = UIOperations()
business = BusinessOperation()
dcor = Decorator(ui)
dcor.runTheContext()
dcor.changeDecore(business)
dcor.runTheContext()

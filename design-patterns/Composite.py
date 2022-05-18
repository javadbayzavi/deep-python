import sys
from matplotlib.pyplot import cla


class OperationModel:
    def operationType1(self):
        pass
    def operationType2(self):
        pass
    def operationType3(self):
        pass

class UIOperation(OperationModel):
    def operationType1(self):
        print('UI operation 1 has called')
    def operationType2(self):
        print('UI operation 2 has called')
    def operationType2(self):
        print('UI operation 3 has called')

class BusinessOperation(OperationModel):
    def operationType1(self):
        print('Business operation 1 has called')
    def operationType2(self):
        print('Business operation 2 has called')
    def operationType3(self):
        print('Business operation 3 has called')

class DataOperation(OperationModel):
    def operationType1(self):
        print('Data operation 1 has called')
    def operationType2(self):
        print('Data operation 2 has called')
    def operationType3(self):
        print('Data operation 3 has called')

class Composite(OperationModel):
    operands = []

    def operationType1(self):
        for oprand in self.operands:
            oprand.operationType1()

    def operationType2(self):
        for oprand in self.operands:
            oprand.operationType2()

    def operationType3(self):
        for oprand in self.operands:
            oprand.operationType3()

    def addOperator(self, opt:OperationModel):
        self.operands.append(opt)
    
    def remOperator(self, opt:OperationModel):
        self.operands.remove(opt)

ui = UIOperation()
business = BusinessOperation()
data = DataOperation()
system = Composite()
system.addOperator(ui)
system.addOperator(business)
system.addOperator(data)

system.operationType1()
system.operationType2()
system.operationType3()
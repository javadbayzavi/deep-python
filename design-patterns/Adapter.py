class OperationalClass:
    def getInfo(self):
        print('basic info')

    def getExtraInfo(self):
        print('basic extra info')

class specificOperation:
    def getInfo(self):pass
    def getExtraInfo(self):pass

class SpecificOperationModel1(specificOperation):
    def getInfo(self):
        return "This information comes from SpecificOperationModel1"
class SpecificOperationModel2(specificOperation):
    def getExtraInfo(self):
        return "This information comes from SpecificOperationModel2"

class adapter1(OperationalClass):
    specific1: SpecificOperationModel1
    specific2: SpecificOperationModel2
    def __init__(self,opt1:specificOperation, opt2:specificOperation) -> None:
        self.specific1 = opt1
        self.specific2 = opt2
        super().__init__()
    
    def getInfo(self):
        return self.specific1.getInfo()
    
    def getExtraInfo(self):
        return self.specific2.getExtraInfo()

spec1 = SpecificOperationModel1()
spec2 = SpecificOperationModel2()
adapter = adapter1(spec1,spec2)

print(adapter.getInfo())
print(adapter.getExtraInfo())
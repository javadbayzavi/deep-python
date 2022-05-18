

class feature:
    def sameValidOperation():
        pass
    
    def getInfo():
        pass


class systemFeautreUI(feature):
    def sameValidOperation(self):
        print('Shared operation from UI')

    def getInfo(self):
        print('UI function has called')

class systemFeatureBusiness(feature):
    def sameValidOperation(self):
        print('Shared operation from Business')

    def getInfo(self):
        print('Business function has called')

class bridge:
    _implementorsource: feature 
    def __init__(self,host:feature) -> None:
        self._implementorsource = host

    def conectFeatures(self,feature2 : feature):
        self._implementorsource.getInfo()
        feature2.getInfo()

    def connectReveseFeature(self,feature2 : feature):
        feature2.getInfo()
        self._implementorsource.getInfo()
    
ui = systemFeautreUI()
business = systemFeatureBusiness()
bridge = bridge(ui)
bridge.conectFeatures(business)
bridge.connectReveseFeature(business)
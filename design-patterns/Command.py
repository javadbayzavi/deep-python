from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def Run(self, params) -> None:
        pass

    @abstractmethod
    def processMe(self, params) -> None:
        pass

class Command(CommandInterface):
    def Run(self, params) -> None:
        return self.processMe(params)

class CommandChild1(Command):
    def __init__(self,classname) -> None:
        self._classname = classname
    
    def processMe(self, params) -> None:
        print(self.showInfo(params))

    def showInfo(self,param):
        self._classname = param
        return "This command has run from " + param


class CommandChild2(Command):
    
    def processMe(self, params) -> None:
        self._classname = params
        print(self.extraFunction())
    
    def extraFunction(self) -> str:
        return "CommandChild2 called extraFunction indirectly"

command = CommandChild1("CommandChild1")
command.Run("CommandChild1")

command = CommandChild2()
command.Run("")
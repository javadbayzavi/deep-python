from asyncio.windows_events import NULL
from multiprocessing import Lock
from threading import Thread

#Singletone mapper which handle racing access to share object of Singleton using lock mechanisms
class SingletoneMap(type):
    _instance = {}
    _lock : Lock = Lock()

    def __call__(self, *args, **nestedargs) -> None:
        with self._lock:
            if self not in self._instance:
                instance = super().__call__(*args, **nestedargs)
                self._instance[self] = instance
            
            return self._instance[self]

#Singletone class: do basic stuff
class Singletone(metaclass = SingletoneMap):
    _classname : str = None
    def __init__(self, clasname) -> None:
        self._classname = clasname
    
    def print(self):
        print(self._classname)
            
#Test function to be called using threads            
def testSingletone(classname):
    singletone = Singletone(classname)
    singletone.print()

#Testing using multi thread processes
process1 = Thread(target=testSingletone, args=("FirstClass",))
process2 = Thread(target=testSingletone, args=("SecondClass",))
process1.start()
process2.start()

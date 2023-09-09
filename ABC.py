from abc import ABC, abstractclassmethod

class Super_Class(ABC):

    @abstractclassmethod
    def union(self):
        pass

    @abstractclassmethod
    def interception(self):
        pass

    @abstractclassmethod
    def difference(self):
        pass
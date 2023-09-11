from abc import ABC, abstractclassmethod


class SuperClass(ABC):

    @abstractclassmethod
    def union(self):
        pass

    @abstractclassmethod
    def interception(self):
        pass

    @abstractclassmethod
    def difference(self):
        pass

    
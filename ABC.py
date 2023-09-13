from abc import ABC, abstractclassmethod


class SuperClass(ABC):

    @abstractclassmethod
    def union(self):
        pass

    @abstractclassmethod
    def show_union(self):
        pass

    @abstractclassmethod
    def intersection(self):
        pass

    @abstractclassmethod
    def show_intersection(self):
        pass

    @abstractclassmethod
    def difference_one(self):
        pass

    @abstractclassmethod
    def difference_two(self):
        pass

    @abstractclassmethod
    def show_difference(self):
        pass

    
from myclass import MyClass

class SubClass(MyClass):
    """ 
    This class is a subclass of the class.
    """

    def __init__(self, color = "Blue", age = 90, name = "Mul"):
        super(SubClass, self, age, name)
        self._color = color
    
    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color
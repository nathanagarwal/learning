class MyClass(object):

    def __init__(self, age = 45, name = "Jose"):
        self._age = age
        self._name = name

    def getName(self):
        return self._name

    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age

    def setName(self, name):
        self._name = name

    def printSelf(self):
        print("Age:", self._age)
        print("Name:", self._name)

        

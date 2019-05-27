class MyClass(object):
    """ 
    This class is a learning opportunity to practice writing classes.
    """

    def __init__(self, age=45, name = "JoseMuldoons"):
        super(MyClass, self).__init__(age, name)

    def setAge(self, _age):
        #Do I need to declare age outside of the constructor 
        # as well to establish as instance variable?
        self.age = _age

    def getAge(self):
        return self.age

    def setName(self, _name):
        self.name= _name
    
    def getName(self):
        return self.name


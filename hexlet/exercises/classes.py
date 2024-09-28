class Base:
    # BEGIN (write your solution here)
    # def __init__(self) -> None:
    #     self.name = 'Baseii'

    def is_instance_of(self):
        print(type(self).__name__)
        klasses = [k.__name__ for k in type(self).__mro__]
        print(klasses)
        # m = type(self).__mro__
        # print('mro:', m)
        # for item in m:
        #     print(item.__name__)

class Child(Base):
    pass

class ChildOfChild(Child):
    pass


if __name__ == '__main__':
    # b = Base()
    # b.is_instance_of()
    c = ChildOfChild()
    c.is_instance_of()
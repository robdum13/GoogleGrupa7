class Stack:

    def _init_(self):
        self.stacklist = []

    def pop(self):
        value = self.stacklist[-1]
        del self.stacklist[-1]
        return value

    def __str__(self):
        return  f"{self.__stackList}"

object_1 = Stack()
print(object_1.__stackList)
object_1.push(3)
object_1.push(2)
object_1.push(1)
print(object_1.pop())
print(object_1.pop())
print(object_1.pop())
print(len(object_1.stacklist))




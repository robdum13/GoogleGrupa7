class Calculator:
    

    def Adunare(self):
        return (self.first_op + self.second_op)

    def Scadere(self):
        return (self.first_op - self.second_op)

    def Inmultire(self):
        return (self.first_op * self.second_op)

    def Impartire(self):
        if(self.second_op !=0):
            return (self.first_op / self.second_op)
        else:
            return "Nu functioneaza"

    def __int__(self,first_op, second_op, op):
        self.first_op = first_op
        self.second_op = second_op
        self.op = op
        if(self.op == '-'):
            return self.Scadere()
        elif(self.op == '+'):
            return  self.Adunare()
        elif(self.op =='/'):
            return self.Impartire()
        else:
            return self.Inmultire

object1= Calculator(3,4,'+')
object2 = Calculator( 5,6,'-')
object3 = Calculator (8,7,'/')

print(object1)
print(object3)
print(object2)
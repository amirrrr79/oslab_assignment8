class mokhtalet:
     def __init__(self,a=0,b=0):
         self.a=a
         self.b=b
     
     
     def show(self):
         print(self.a,'+',self.b,'i')
         
     def sum(self,other):
         result=mokhtalet()
         result.a=self.a+other.a
         result.b=self.b+other.b
         return result
     
     def sub(self,other):
         result=mokhtalet()
         result.a=self.a-other.a
         result.b=self.b-other.b
         return result
     
     def mul(self,other):
         result=mokhtalet()
         result.a=(self.a*other.a)-(self.b*other.b)
         result.b=(self.a*other.b)+(self.b*other.a)
         return result
         
p1=mokhtalet(4,8)             
p1.show()
p2=mokhtalet(5,7)
p2.show()
p3=mokhtalet.sum(p1,p2)
p3.show()
p4=mokhtalet.sub(p1,p2)
p4.show()
p5=mokhtalet.mul(p1,p2)
p5.show()

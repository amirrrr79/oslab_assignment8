import math
class kasr:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    
    def show(self):
        print(self.a,'/',self.b)
        
    def sum(self,other):
        result=kasr()
        if(self.b==other.b):
            result.a=self.a+other.a
            result.b=self.b
        else:
            result.a=(self.a*other.b)+(self.b*other.a)
            result.b=self.b*other.b
            
        return result
    
    def sub(self,other):
        result=kasr()
        if(self.b==other.b):
           result.a=self.a-other.a
           result.b=self.b
        else:
            result.a=(self.a*other.b)-(self.b*other.a)
            result.b=self.b*other.b
            
        return result
    
    def mul(self,other):
        result=kasr()
        result.a=self.a*other.a
        result.b=self.b*other.b
        return result
    
    def divid(self,other):
        result=kasr()
        result.a=self.a*other.b
        result.b=self.b*other.a
        return result
    
    def simple(self):
        result=kasr()
        result_gcd=math.gcd(self.a,self.b)
        result.a=self.a//result_gcd
        result.b=self.b//result_gcd
        return result
        
t1=kasr(4,5)
t1.show()
t2=kasr(8,6)
t2.show()
t4=kasr.sum(t1,t2)
t4.show()    
t5=kasr.sub(t1,t2)
t5.show() 
t6=kasr.mul(t1,t2)
t6.show()
t7=kasr.divid(t1,t2)
t7.show()
t8=kasr.simple(t2)
t8.show()

                
            
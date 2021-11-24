class time:
    def __init__(self,h=0,m=0,s=0):
        self.hour=h
        self.minute=m
        self.second=s
    
    def show(self):
        print(self.hour,':',self.minute,':',self.second)
    
    def sum(self,other):
        result=time()
        result.hour=self.hour+other.hour
        result.minute=self.minute+other.minute
        result.second=self.second+other.second
        result.fix()
        return  result
    
    def fix(self):
        if self.second>=60:
            self.second-=60
            self.minute+=1
        if self.minute>=60:
            self.minute-=60
            self.hour+=1
    
    def tafrigh(self,other):
        result=time()
        result.hour=self.hour-other.hour
        result.minute=self.minute-other.minute
        result.second=self.second-other.second
        result.fixs()
        return  result
    
    def fixs(self):
      if self.second<0:
           self.second+=60
           self.minute-=1
      if self.minute<0:
           self.minute+=60
           self.hour-=1
                
    
    def f(self):
        s=self.hour*3600+self.minute*60+self.second
        print('second=',s)
    def h(self):
        self.hour=self.second//3600
        self.second=self.second%3600
        self.minute=self.second//60    
        self.second=self.second%60
        print(self.hour,':',self.minute,':',self.second)
        
t1 = time(7,30,20)
t1.show() 
t2=time(6,50,10)
t2.show()
t3=time.tafrigh(t1,t2)
t3.show()
t4=time(s=9010)
t4.h()

        
                
    
                       
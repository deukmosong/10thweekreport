class Counter:
  

    def __init__(self,number=None):
        if number==None:
            self.__number=0
        else:
            if number>100 or number<0 :
             number=0
            else :
                self.__number=number
    def  reset(self):
        self.__number=0
    
    def inc(self):
        self.__number=self.__number+1

    def dec(self):
        self.__number-=1

    def __str__(self):
        return 'C('+str(self.__number)+')'
    def __add__(self,other):

        if self.__number-other.__number>0:
            return Counter(0)
        else :
            return Counter(self.__number+other.__number)
    def __sub__(self,other):
        if self.__number-other.__number<0:
            return Counter(0)
        else :
            return Counter(self.__number-other.__number)

c1=Counter(10)
c1.inc()
print('c1=',c1)
print()
c2=Counter()
c2.inc()
c2.inc()
c2.dec()
print('c2=',c2)
c2.reset()
print('c2=',c2)
## add,sub 확인 
c1=Counter(10)
c2=Counter(20)
c3=c1+c2
c4=c1-c2
print('c3=',c3)
print('c4=',c4)

      

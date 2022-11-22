class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector2D(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector2D(self.x-other.x,self.y-other.y)
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    def __mul__(self,other):
        return Vector2D((self.x)*(other.x),(self.y)*(other.y))
    def __truediv__(self,other):
        return Vector2D(self.x/other.x,self.y/other.y)
    def __neg__(self):
        return Vector2D(-self.x,-self.y)
    def __lt__(self,other):
        return self.x< other.x and self.y<other.y
       
    def __le__(self,other):
        return self.x<= other.x and self.y<=other.y
      
    def __ge__(self,other):
       return self.x>= other.x and self.y>=other.y
        
    def __gt__(self,other):
        return self.x> other.x and self.y>other.y
          
    def __eq__(self,other):
       return self.x== other.x and self.y==other.y
        
    def __ne__(self,other):
        return self.x!= other.x and self.y!=other.y
         

v1=Vector2D(30,40)
v2=Vector2D(10,20)
print("v1>v2=",v1>v2)
print("v1>=v2=",v1>=v2)
print("v1<v2=",v1<v2)
print("v1<=v2=",v1<=v2)



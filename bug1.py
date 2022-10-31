# TODO: there's code missing in one or more lines below

class Base:
    def __init__(self, x, y, size):
        # TODO: will need to fill this in
        self.x = x # added x instance variable
        self.y = y # added y instance variable
        self.size = size # added size instance variable
    
    def draw(self):
        return ""

class Circle(Base): #Added Base parameter because Circle is a child of base
    def __init__(self, x, y, size): # added self to match parameters of Base
        super().__init__(x,y,size)

    def draw(self):
        return f"""
({self.x}, {self.y})
{self.size}
        , - ~ ~ ~ - ,
    , '               ' ,
  ,                      ,
 ,                        ,
,                          ,
,                          ,
,                          ,
 ,                        ,
  ,                      ,
    ,                 , '
      ' - , _ _ _ , '
        """

class Square(Base):
    def __init__(self,x,y,size): # added x to match parameters of Base
        super().__init__(x,y,size)

    def draw(self): #added self parameter
        return f"""
({self.x}, {self.y})
{self.size}
--------------------
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
--------------------
        """

def draw_any_shape(myShape):
    print(myShape.draw())

def main():
    s = Square(1,2,3)
    draw_any_shape(s)

    c = Circle(2,2,1)
    draw_any_shape(c)

main()
##  반지름이 3이고 x,y 좌표가 (2.4)인 원을 만들어 넓이와 둘레를 출력하세여

```python
class Circle:
    pi = 3.141592
    
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
       
    def area(self):
        return self.pi * self.r * self.r
    
    def circumference(self):
        return 2 * self.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
```

```python
s = Circle(0,0,3)
s.move(2,4)
print(f'넓이 : {s.area()}')
print(f'둘레 : {s.circumference()}')

```

```
넓이 : 28.259999999999998
둘레 : 18.84
```


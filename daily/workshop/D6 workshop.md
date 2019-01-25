## 양의 정수 x를 입력 받아 제곱근의 근사값의 결과를 반환하는 함수를 작성하세요.  sqrt() 사용 금지`

```python
def my_sqrt(n):
    x, y = 1, n
    answer = 0
    
    while True:
        answer = (x+y) / 2
        if answer**2 < n:
            x = answer
        else:
            y = answer
    
        if abs(answer**2 - n) < 1e-5:
            return answer
    
my_sqrt(2) 
```

```
1.414215087890625
```


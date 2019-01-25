

## 1  Python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하세요.

```python
import keyword
print(keyword.kwlist)
```

```
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



## 2  파이썬에서 float는 실수를 표현하는 과정에서 같은 값으로 일치되지 않습니다. (floating point rounding error) 따라서, 아래의 값을 비교하기 위해 작성해야하는 코드를 작성하세요.

```python
a = 0.1 * 3
b = 0.3

print(f'그냥 a==b를 했을 때 {a==b}')
print(f'abs(a-b)<1e-10 했을 때{abs(a-b)<1e-10}')
```

```
그냥 a==b를 했을 때 False
abs(a-b)<1e-10 했을 때True
```



## 3  “안녕, 철수야”를 String Interpolation을 사용하여 출력하세요.

```python
name = "철수"
print(f'안녕, {name}야')
```

```
안녕, 철수야
```



## 4  다음 중 형변환시 오류가 발생하는 것은?

1) str(1) 2) int(‘30’) 3) int(5) 4) bool(‘50’) 5) int(‘3.5’)

```python
print(int('3.5'))
```

```
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-16-2460c40ec1c6> in <module>
----> 1 print(int('3.5'))

ValueError: invalid literal for int() with base 10: '3.5'
```



## 5 mutable 과 immtable을 분류하기

```
String, List, Tuple, Range, Set, Dictionary
```

Mutable = List, Set, Dictionary

Immutable = Range, String, Tuple
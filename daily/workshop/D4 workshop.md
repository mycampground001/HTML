## 1  두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.

``` python
n = 5
m = 9
print(m*('*'*n +'\n'))
```

```
*****
*****
*****
*****
*****
*****
*****
*****
*****
```



## 2  다음 딕셔너리에서 평균 점수를 출력하시오.

```python
student = { 'python': 80, 'algorithm' : 99, 'django':89, 'flask':83 }
result = 0

for score in student.values():
    result += score

print(result/len(student.values()))
```

```
87.75
```



## 3  다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.

```python
blood_types = ['A','B','A','O','AB','AB','O','A','B','O','B','AB']
blood = ['A','B','AB','O']

for i in range(len(blood)):
    blood[i] = blood_types.count(blood[i])
    
print(blood)
```

```
[3, 3, 3, 3]
```










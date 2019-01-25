## Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다. v 따라서, 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요

``` python
def palindrome(s):
    i = 0
    j = len(s)-1
    while i<j:
        while not s[i].isalnum() and i<j: #알파벳이 아닌 것들은 무시
            i += 1
        while not s[j].isalnum() and i<j: #알파벳이 아닌 것들은 무시
            j += 1      
        if s[i].lower() != s[j].lower():
            return False    
        i += 1
        j -=1
    return True

print(palindrome('1122+!!@#$#@2211'))
print(palindrome('토마토 토마토'))
print(palindrome('gods'))
```

```
True
True
False
```




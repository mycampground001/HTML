# def solve(n):
#     t = n%10
#     n = int(n/10)
#     while n!=0:
#         if n%10>t:
#             return False
#         t = n%10
#         n = int(n/10)
#     return True
 
# tc = int(input())
# for z in range(1,tc+1):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     result = -1
#     for i in range(n):
#         for j in range(i+1,n):
#             if result<arr[i]*arr[j]:
#                 if solve(arr[i]*arr[j]):
#                     result = arr[j]*arr[i]
#     print('#'+str(z),result)
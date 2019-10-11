# 作者     ：gw
# 创建日期 ：2019-07-04  上午 11:08
# 文件名   ：搭积木.py
# import sys
# n = int(input())
# if n==1:
#     print(1)
#     exit()
# ret = []
# for i in range(n):
#     arr = list(map(int, input().strip().split()))
#     ret.append(arr)
#
# ret = sorted(ret, key=lambda x:(x[1],x[0]))
# print(ret)
# count = 0
# for i in range(n-1):
#     if ret[i][0] <= ret[i+1][0] and ret[i][1] <= ret[i+1][1]:
#         count += 1
# print(count+1)

import sys
n = int(input())
if n==1:
    print(1)
    exit()
ret = []
for i in range(n):
    arr = list(map(int, input().strip().split()))
    ret.append(arr)

ret = sorted(ret, key=lambda x:(x[0],x[1]))
dp = [ret[0][1]]
print(dp)
# print(ret)
ans = []
for i in range(1,n):
    if ret[i][1] >= dp[-1]:
        dp.append(ret[i][1])
        ans.append(ret[i])
    else:
        for j in range(len(dp)):
            if ret[i][1] > dp[j]:
                continue
            elif dp[j] != ret[i][1]:
                # dp.insert(j,ret[i][1])
                dp[j] = ret[i][1]
                ans.append(ret[i])
                break
            else:
                dp.insert(j,ret[i][1])
                ans.append(ret[i])
                break
# print(dp)
print(ans)
print(len(dp))

# import sys
# n = int(input())
# if n==1:
#     print(1)
#     exit()
# ret = []
# for i in range(n):
#     arr = list(map(int, input().strip().split()))
#     ret.append(arr)
#
# ret = sorted(ret, key=lambda x:x[0])
# dp = [ret[0][1]]
# ans = []
# for i in range(1,n):
#     flag = False
#     if ret[i][1] >= dp[-1]:
#         dp.append(ret[i][1])
#         ans.append(ret[i])
#     else:
#         low, high = 0,len(dp)-1
#         mid = 0
#         while low<=high:
#             mid = (low+high)//2
#             if dp[mid] < ret[i][1]:
#                 low += 1
#             elif dp[mid] > ret[i][1]:
#                 high -= 1
#             else:
#                 flag = True
#                 break
#         if flag:
#             flag = False
#             dp.insert(mid,ret[i][1])
#             ans.append(ret[i])
#         else:
#             dp[low] = ret[i][1]
#             ans.append(ret[i])
# print(ans)
# print(len(dp))
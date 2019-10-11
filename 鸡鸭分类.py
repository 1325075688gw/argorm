# 作者     ：gw
# 创建日期 ：2019-07-04  下午 16:25
# 文件名   ：鸡鸭分类.py
import sys

a = sys.stdin.readline().strip()

res = 0
l = 0
for i in range(len(a)):
    if a[i] == 'C':
        res = res + i - l
        l = l + 1
print(res)
# 作者     ：gw
# 创建日期 ：2019-07-20  下午 21:23
# 文件名   ：建物流中转站.py
def func():
    n = int(input())
    ret = []
    for i in range(n):
        res = list(map(int, input().split()))
        ret.append(res)
    X,Y =0,0
    count = 0
    for i in range(n):
        for j in range(n):
            if ret[i][j] == 1:
                X += j
                Y += i
                count += 1
    x = X//count
    y = Y//count
    return (ret,n,x,y)
def cal(ret,n,x,y):
    dis = 0
    for i in range(n):
        for j in range(n):
            if ret[i][j] == 1:
                dis += abs(x-j)+abs(y-i)
    return dis

ret,n,x,y = func()
print(min(cal(ret,n,x,y),cal(ret,n,x+1,y+1)))
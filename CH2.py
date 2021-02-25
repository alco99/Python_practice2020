#輸入直徑求面積、周長
d = int(input('')) #d 為直徑
d = d/2
a = round(d*d*3.14,3)  # 面積
p = round(2*d*3.14,3)  # 周長
print (a) 
print (p) 

#假設某月1號為星期一，輸入日期求星期幾
d = int(input('')) # d 為該月日期
w = d%7
if w==0:
    w=7
print (w) # w 為輸出之星期幾

#輸入攝氏溫度，求華氏溫度
c = int(input('')) # c 為攝氏
f = round(c*9/5+32,2)
print (f) # f 為輸出之華氏

#求兩個座標之間的距離
x1, y1 = eval(input('')) # x1, y1 是第一個座標
x2, y2 = eval(input('')) # x2, y2 是第二個座標
import math
d = math.sqrt((x1-x2)**2+(y1-y2)**2)
d = round(d,2)
print (d)

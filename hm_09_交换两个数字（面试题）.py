a = 6
b = 100
# 解法1：需要一个中间变量
# c = a
# a = b
# b = c
# 解法2: 不使用变量
# a = a + b
# b = a - b
# a = a - b
# 解法3：python 专有
# a ,b  = (b , a)
a , b = b , a
print(a)
print(b)


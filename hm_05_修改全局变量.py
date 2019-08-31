num = 30

def num1():
    global num
    num = 99
    print("num1 = %d" % num)
def num2():
    print("num2 = %d" % num)

num1()
num2()
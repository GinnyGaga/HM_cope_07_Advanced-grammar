
def measure():
    """测量温度和湿度"""
    print("测量开始。。")
    tem = 39
    wetness = 50
    print("测量结束 。。")
    return tem , wetness


result = measure()
print(result)
# print(result[0])
# print(result[1])
gl_temp,gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
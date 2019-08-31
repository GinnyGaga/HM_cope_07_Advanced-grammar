def demo(num,num_list):
    print("函数开始")
    # 1.不影响外部全局变量（赋值运算）
    # num = num + num

    # 2.不影响外部全局变量（赋值运算）
    num += num

    # 3.不影响外部全局变量（赋值运算）
    # num_list = num_list + num_list

    # 4.影响外部全局变量，调用方法
    # num_list.extend(num_list)

    # 5.影响外部全局变量，本质上做4的运算，调用列表extend 的方法，不会修改引用，
    # 不会修改引用就会影响外部的全局变量数据。
    num_list += num_list

    print(num)
    print(num_list)
    print("函数结束")

gl_num = 9
gl_list = [1,2,3]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)
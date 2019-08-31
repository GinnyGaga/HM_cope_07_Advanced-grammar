def demo(*args,**kwargs):
    print(args)
    print(kwargs)

gl_list = [1,2,3]
gl_dict = {"name":"ginny","year":18}
demo(*gl_list,**gl_dict)

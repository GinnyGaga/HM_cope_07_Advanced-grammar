def print_info(name,title = "",gender = True):
    """
    :param title: 职位
    :param name: 班上同学的名字
    :param gender:True 男生，Fault 女生
    """
    gender_text = "男生"
    if not gender :
        gender_text = "女生"
    print("[%s]%s 是 %s" % (title,name,gender_text))

print_info("小明")
print_info("老王")
print_info("小美",gender = False)
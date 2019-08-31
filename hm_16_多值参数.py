def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)

demo(1)
print("-"*10)
demo(1,2,3,4,5)
print("-"*10)
demo(1,2,6,3,name="ginny",old = 10,gender=True)
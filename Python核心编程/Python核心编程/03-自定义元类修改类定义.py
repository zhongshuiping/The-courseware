
class MyMetaClass(type):
    def __new__(cls, class_name, parents_class, old_attr):
        """该函数在Class1类对象创建的时候  自动调用 ----> 修改类的属性"""
        # 参数1是需要创建的类名  参数2是父类的元组 参数3是类属性构成的字典
        print("正在执行自定义代码创建类")
        print("需要创建的类名%s 父类%s 属性字典%s" % (class_name, parents_class, old_attr))
        new_attr = dict()
        for name,values in old_attr.items():
            # 如果是不以__开始的属性 那么就修改字符为大写
            if not name.startswith("__"):
                new_attr[name.upper()] = values
            else:
                new_attr[name] = values  # 否则就不修改
        return type(class_name, parents_class, new_attr)
        # return type.__new__(class_name, parents_class, new_attr)

# metaclass只需要对象时可调用对象  MyMetaClass() 等价于下面两步
# 1 mt = MyMetaClass.__new__()
# 2 mt.init()
class Class1(object, metaclass=MyMetaClass):
    foo = 100
    age = 101

print(hasattr(Class1, "foo"))
# print(Class1.age)
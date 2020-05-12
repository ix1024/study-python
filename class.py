class Test:
    '''
    测试Class
    '''
    def __init__(self, name, age):
        print('__init__')
        self.data = []
        self.name = name
        self.age = age

    def f(self):
        return self.name + ' ' + str(self.age)


# 实例化类
x = Test('kingwell', 30)
print(x.f())
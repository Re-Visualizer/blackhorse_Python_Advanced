"""
案例：演示在类外如何获取和设置对象的属性

类外，设置对象的属性：
     = 属性值
    特点：该属性读属于这个对象

    类外，获取对象的属性
    对象名.属性名
"""
class Car:
    def __init__(self, name = 'BYD'):
        self.name = name
        self.color = 'blue'
        self.wheel = 4
        self.price = 0


    def run(self):
        print(f'{self.name}已启动')

    def show(self):
        print(f'{self.name}的颜色是{self.color}')


xiaomi = Car('xiaomi')
xiaomi.run()
print(xiaomi.color)
xiaomi.color = 'orange'
xiaomi.show()

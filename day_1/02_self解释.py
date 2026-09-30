"""
案例：self关键字解释

self介绍：
    概述：
        他是Python内置的关键字，用于表示本类当前对象的引用
    作用：
        1. 在类中定义方法时，第一个参数必须是self，用于表示对象本身
        2. 在类中定义方法时，通过self关键字，可以访问对象的属性和其他方法
        3. 通过self关键字，可以实现对象的属性和方法的封装
"""
class Car:
    """
    定义一个汽车的通用模板
    """
    # 属性


    # 行为
    def run(self):
        print("汽车正在启动")
        print(f"self:{self}")

    def work(self):
        print(f"work函数的self:{self}")
        self.run()
        print("work函数执行完毕")
# 2.创建汽车类的对象
xiaomi = Car()
huawei = Car()
# 3.调用Car的run()函数
xiaomi.run()
huawei.run()
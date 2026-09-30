class Phone:
    # 属性

    # 行为
    # 1.1开机
    def open(self):
        print(f"{self}开机了")

    def close(self):
        print(f"{self}关机了")

    def take_photo(self):
        print(f"{self}拍照了")

# 2.创建手机类对象，访问其成员
iPhone = Phone()
print(f"iPhone对象：{iPhone}")

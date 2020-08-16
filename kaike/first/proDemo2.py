class Bike:
    # 初始化方法 no代表车辆编号、age代表车辆年限、
    # state代表车辆状态，0代表待租借，1代表租借中
    def __init__(self, NO, age, state=0):
        self.NO = NO
        self.age = age
        self.state = state

    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '车辆编号%d 已经运行%d年，车辆状态：%s' % (self.NO, self.age, status)


class Manage:
    # 定义一个列表，用来存储所有的车辆
    bike_list = []

    def __init__(self):
        bikeA = Bike(1001, 2)
        bikeB = Bike(1002, 2)
        bikeC = Bike(1003, 1)
        self.bike_list.append(bikeA)
        self.bike_list.append(bikeB)
        self.bike_list.append(bikeC)

    # 系统菜单
    def menu(self):
        print("欢迎使用共享单车租借系统\n")
        while True:
            print(' 1.查询所有车辆\n 2.共享车辆\n 3.租借车辆\n 4-5.归还车辆\n 5.退出系统\n')
            select = int(input('请输入所选功能对应得数字：'))
            if select == 1:
                # 单车信息
                self.info_bike()
            elif select == 2:
                # 共享单车
                self.add_bike()
            elif select == 3:
                # 租借车辆
                self.lease_bike()
            elif select == 4:
                # 归还车辆
                self.revert_bike()
            elif select == 5:
                # 退出系统
                print('期待您下次使用！祝您生活愉快！')
                break
        # 单车信息

    def info_bike(self):
        for bike in self.bike_list:
            print(bike)

    # 共享单车
    def add_bike(self):
        new_NO = int(input('请输入车辆编码'))
        new_age = int(input('请输入车辆使用年限'))

        new_bike = Bike(new_NO, new_age)
        self.bike_list.append(new_bike)
        print('车辆共享成功！')

    # 租借车辆
    def lease_bike(self):
        lease_NO = int(input("请输入租借的车辆编号"))
        for bike in self.bike_list:
            # 遍历自行车列表，与用户租借的编号进行匹配
            if bike.NO == lease_NO:
                # 如果单车在平台中存在
                if bike.state == 1:
                    # 车辆租借中
                    print("你来晚了，车被租走了")
                    break
                else:
                    # 车辆待租借
                    print("租借成功，欢迎您使用绿色出行")
                    bike.state = 1
                    break
            else:
                print('车辆编号输入错误')
                break

    # 归还车辆
    def revert_bike(self):
        pass


user = Manage()
print(user)
user.menu()
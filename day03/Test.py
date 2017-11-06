#coding=utf-8
from day07.file_test import FIleIoTest

class  Recursion:
    def __init__(self):
        self.list=[]
    def  recursion5(self,num):#num为参数  求num的阶乘  特点：定义方法 根据参数判断出节点  一个节点有固定值 其他的数字向节点推进
        if num==1:
            return 1
        else:
            return self.recursion5(num-1)*num
    def  rubbitnum(self,month):
        if month==1:
            return 1
        elif month==2:
            return 1
        else:
            return self.rubbitnum(month-1)+self.rubbitnum(month-2)

    def calcmolecule(self, month):
        if month == 1:
            return 2.0
        elif month == 2:
            return 3.0
        else:
            return float(self.calcmolecule(month - 1)) + float(self.calcmolecule(month - 2))
    def calcdenominator(self, month):
        if month == 1:
            return 1.0
        elif month == 2:
            return 2.0
        else:
            return float(self.calcdenominator(month - 1)) + float(self.calcdenominator(month - 2))
        #题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
    def calcAdd(self,num1,num2):
        if num2==1:
            return num1
        else:
            return self.calcAdd(num1,num2-1)*10+num1





    def listtest(self):

        name=raw_input('请输入姓名')

        self.list.append(name)
        y_n=raw_input('是否继续添加 输入y则继续，输入其他结束')
        if y_n=='y':
            self.listtest()
        else:
            print '**************************\n' \
                  '          客户姓名列表          \n'
            for i in self.list:#列表的遍历
                print i,
            # for i in range(len(self.list)):
            #     print self.list[i]
            print '\n***************************'



class Customer:
    def __init__(self):
        self.str='*********************************\n' \
                 '编号   菜品名称    价格    数量   小计\n'
        self.count=0
        self.name='admin'
        self.pw='123'
        self.map={1:['鱼香肉丝',16],2:['糖醋里脊',21],3:['酱牛肉',38],4:['老干妈炒饭',8]}
    def order(self):
        num=raw_input('如果是管理员的话请输入1，顾客的话输入其他')
        if num=='1':
            self.login()
        else:
            self.menu()

    def login(self):
        n=raw_input('请输入管理员姓名')
        if n==self.name:
            p=raw_input('请输入密码：')
            if p==self.pw:
                print 'welcome'
                #添加菜品 价格
                y_n = raw_input('是否添加菜品，输入y则添加，输入其他退出')
                if y_n == 'y':
                    self.addMenu()


                else:
                    print '退出'
                    return

            else:
                print '密码错误，请重新输入'
                self.login()
        else:
            print '姓名错误，请重新输入'
            self.login()
    def addMenu(self):
        print '当前编号为%s' % len(self.map)
        name = raw_input('请输入新菜品的名称')
        price = int(raw_input('请输入新菜品价格'))
        self.map.update({len(self.map) + 1: [name, price]})
        y_n = raw_input('是否继续添加 输入y则继续，输入其他结束')
        if y_n == 'y':
            self.addMenu()
        else:
            self.menu()


    def menu(self):
        print '菜品展示:\n' \
              '编号        菜品名称        价格\n' \
              '--------------------------------'
        for i in range(1,len(self.map)+1,1):
            print '%s         %s         %s'%(i,self.map[i][0],self.map[i][1])
        print '--------------------------------'
        id=int(raw_input('请根据菜单输入您所需菜品名称的编号'))
        num=int(raw_input('请输入数量'))
        price=self.map[id][1]
        sum=num*price#小计
        name=self.map[id][0]
        self.count+=sum
        self.str+='%s     %s      %s      %s     %s\n'%(id,name,price,num,sum)
        y_n=raw_input('是否继续点餐 是的话输入y，否则的话输入其他')
        if y_n=='y':
            self.menu()
        else:
            self.str+='***********************************\n'
            # print self.str
            self.str+= '总计：   %s'%self.count
            fileioTest=FIleIoTest()
            fileioTest.inputMenu(self.str)




















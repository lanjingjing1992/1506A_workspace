#coding=utf-8
class Shopping:#创建类
    def __init__(self,name='alice'):#重写 构造方法  初始化对象的时候被调用 #默认参数
        self.name=name
        self.map={'1':['体恤',245],'2':['网球鞋',300],'3':['网球拍',500]}
        self.count = 0
    def printName(self):
        print self.name
    def Shop(self):
        print 'Myshopping结算管理系统 > 结算：\n' \
              '*************************************\n' \
              '请选择商品编号：\n' \
              '*************************************\n' \
              '1 体恤    2 网球鞋   3 网球拍  '

        self.inputId()
    def inputId(self):
        id=raw_input('请输入商品编号：')
        name=self.map[id][0]
        price=self.map[id][1]




        print '商品名称：'+name+'    价格为:%s'%price
        num = int(raw_input('请输入商品数量'))
        sum = num * price
        self.count += sum
        print '小计    %s'%sum
        y_n=raw_input('是否继续购买，输入y则继续，输入其他则结束')
        if y_n=='y':
            self.inputId()#递归
        else:
            print '结束 总价:%s'%self.count
            return






# alice=Shopping()
# alice.printName()

# alice.Shop()
class Test:

    def calcMoney(self):
         money = int(raw_input('请输入本金'))
         for i in range(5):
             money*=1.003
             print '第%s年的本金跟利息%s'%(i+1,money)

    def exactDivision(self):#整除7
        sum=0
        for i in range(0,1001,7):
            # if i%7==0:
                sum+=i


        print sum
    def inputNum(self):
        num=float(raw_input('请输入一个整数'))
        i=0
        while True:
            num/=10
            i+=1
            if num<1:
                break


        print i
    def decrease(self):
        i=100
        while True:
            print i
            i-=5

            if i==5:
                continue
                print '结束'
            elif i<0:
                break
    def calc(self):
        sum=0
        for i in range(0,50,7):
            sum+=i

        print sum

    def InputNumSort(self):
        list=[]
        while True:
            num=int(raw_input('请输入数字，输入0结束'))
            if num==0:
                print 'max值%s'%(max(list))
                print 'min值%s' % (min(list))
                break
            else:
                list.append(num)
    def calclate5(self):
        for i in range(1,101,1):
            if i%5==0 and i%3!=0 and i%8!=0:
                print i
    def output7(self):
        for i in range(100,1000,1):
            #个位数
            num=i%10
            if num==7:
                print i
    def add(self):
        for i in range(100,1000,1):
            #百位
            n=i//100
            #十位
            m=i%100//10
            #个位
            k=i%10

            if n+m==k:
                print i
    def nextto(self):
        for i in range(10,100,1):
            #十位
            n=i//10
            #个位
            m=i%10
            if n-1==m or n+1==m:
                print i
    def print3(self):
        for i in range(100,1000,1):
            if i%100//10+i//100==3:
                print i














# c=Test()
# c.calcMoney()
# c.exactDivision()
# c.inputNum()
# c.decrease()
# c.calc()
# c.InputNumSort()
# c.calclate5()
# c.output7()
# c.add()
# c.nextto()
# c.print3()


class Customer:
    def __init__(self):
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
                pass
            else:
                print '密码错误，请重新输入'
                self.login()
        else:
            print '姓名错误，请重新输入'
            self.login()
    def menu(self):
        print '菜品展示:\n' \
              '编号        菜品名称        价格\n' \
              '--------------------------------'
        for i in range(1,len(self.map)+1,1):
            print '%s         %s         %s'%(i,self.map[i][0],self.map[i][1])
        print '--------------------------------'
        id=int(raw_input('请根据菜单输入您所需菜品名称的编号'))
        num=int(raw_input('请输入数量'))
        sum=num*self.map[id][1]#小计
        self.count+=sum
        y_n=raw_input('是否继续点餐 是的话输入y，否则的话输入其他')
        if y_n=='y':
            self.menu()
        else:
            print '总计：   %s'%self.count




c=Customer()#创建对象
# c.login()#登陆
c.order()

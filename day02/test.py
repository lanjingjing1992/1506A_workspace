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











c=Test()
# c.calcMoney()
# c.exactDivision()
# c.inputNum()
# c.decrease()
# c.calc()
# c.InputNumSort()
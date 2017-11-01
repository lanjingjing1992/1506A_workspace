#coding=utf-8

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
            print '***************************'









r=Recursion()
# print r.recursion5(5)
# print r.rubbitnum(8)
# sum=0.0
# for i in range(1,21,1):
#     sum+=float(r.calcmolecule(i)/r.calcdenominator(i))


# print sum
# num1=int(raw_input('请输入数字：'))
# num2=int(raw_input('请输入共有几个数字相加'))
# sum=0
# for i in range(1,num2+1,1):
#     sum+= r.calcAdd(num1,i)
#
#
#
# print sum
r.listtest()








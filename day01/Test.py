#coding=utf-8


# number=int(raw_input('请输入张浩的考试成绩'))
# if number>=98:
#     print 'mp4'
# elif number>60:
#
#         print '不罚写'
# else:
#         print '罚写代码'


# age=int(raw_input('请输入年龄'))
# sex=raw_input('请输入性别 boy为男孩，girl为女孩')
# if age>7 or (age>5 and sex=='boy'):
#     print 'ok'
# else:
#     print '不可以'

# num=int(raw_input('请输入坏鸡蛋的数量'))
# if num<5:
#     print '忍了吃了算了'
# else:
#     print '退货'

# num=int(raw_input('请输入一个数字'))
# if num%3==0 or num%5==0:
#     print 'yes'
# else:
#     print 'no'

# money=int(raw_input('请输入压岁钱的数目'))
# if money>1000:
#     print '捐了'
# elif money>500:
#     print '航模'
# else:
#     print '百科全书'
#
# vip=raw_input('请输入是否是vip，如果是的话输入y，不是的话输入其他')
# money=int(raw_input('请输入消费金额'))
# if vip=='y':
#     if money>200:
#         print money*0.75
#     else:
#         print money*0.8
# else:
#     if money>100:
#         print money*0.9
#     else:
#         print money

#请计算出100以内的偶数和
# sum=0
# for i in range(101):#o-100包括0但是不包括100
#     sum+=i
#
#
# print sum
class Shopping:
    def shop(self):#当前类对象的一个引用
        self.name='bob'#属性
        self.map={'1':['体恤','$570'],'2':['网球鞋','$245'],'3':['网球拍','$300']}

        print 'Myshopping结算管理系统 > 结算：\n' \
              '**********************************\n' \
              '请选择购买的商品编号：\n' \
              '1 体恤    2 网球鞋   3 网球拍\n' \
              '***********************************'
        self.select()

    def select(self):
        id=raw_input('请输入编号：')
        print self.map[id][0]
        print self.map[id][1]
        y_n=raw_input('是否继续输入，输入n结束，输入其他继续')
        if y_n=='n':
            print '结束'
            return
        else:
            self.select()





shopping=Shopping()
shopping.shop()







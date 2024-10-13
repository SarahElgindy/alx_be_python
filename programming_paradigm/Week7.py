# class Demo:
#     def add(self,*args):
#         total = 0
#         for i in args:
#             total += i
#         return total
# d=Demo()
# print(d.add(2,3))
# print(d.add(1,2,3))
# print (d.add(3,4,5,67,7,8)) 

class Father:
    def sleep(self):
        print("sleeps from 10:00 pm to 05:00 am")
def eat(self):
    print("eating")

class Son(Father):
    def sleep(self):
        print("sleeps from 02:00 am to 10:00 am")
        super().sleep()

Ram=Son()
Ram.sleep()
    
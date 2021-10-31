# 注：此处全局的变量名，写成name，只是为了演示而用
# 实际上，好的编程风格，应该写成gName之类的名字，以表示该变量是Global的变量
name = "whole global name";


class Person:
    def __init__(self, newPersionName):
        # self.name = newPersionName;

        # 1.如果此处不写成self.name
        # 那么此处的name，只是__init__函数中的局部临时变量name而已
        # 和全局中的name，没有半毛钱关系
        self.name = newPersionName;

        # 此处只是为了代码演示，而使用了局部变量name，
        # 不过需要注意的是，此处很明显，由于接下来的代码也没有利用到此处的局部变量name
        # 则就导致了，此处的name变量，实际上被浪费了，根本没有利用到

    def sayYourName(self):
        # 此处由于找不到实例中的name变量，所以会报错：
        # AttributeError: Person instance has no attribute 'name'
        print
        'My name is %s' % (self.name);


def selfAndInitDemo():
    persionInstance = Person("crifan");
    persionInstance.sayYourName();


###############################################################################
if __name__ == "__main__":
    selfAndInitDemo();
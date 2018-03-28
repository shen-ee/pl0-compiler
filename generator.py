# coding:utf-8
import globalvar


class Pcode:
    def __init__(self, operator, s1, s2):
        self.operator = operator
        self.s1 = s1
        self.s2 = s2


def gen(operator, s1, s2):
    code = globalvar.get_code()
    item = Pcode(operator, s1, s2)
    code.append(item)
    globalvar.set_code(code)
    return len(globalvar.get_code())-1


def show():
    print("****************")
    print("this is p-code:")
    code = globalvar.get_code()
    for i in code:
        print("No."+str(code.index(i))+"  "+str(i.operator)+"  "+str(i.s1)+"  "+str(i.s2))
    print("****************")


# show()
# gen("opr",0,1)
# gen("sto",0,1)
# show()

# coding:utf-8
import  globalvar



class Item:
    def __init__(self, name, typ, s1=0, s2=0):
        self.name = name
        self.typ = typ
        if typ == 'constant':
            self.num = s1
        else:
            self.lev = s1
            self.adr = s2
def show():
    print ("****************\nthis is the table:")
    table = globalvar.get_table()
    length = len(table)
    for i in table:
        if i.typ == "constant":
            print(str(table.index(i))+" "+i.name+" "+i.typ+" "+str(i.num))
        else:
            print(str(table.index(i))+" "+i.name+" "+i.typ+" "+str(i.lev)+" "+str(i.adr))
    print ("****************")
    return 0


def enter(name, typ, s1=0, s2=0):
    table = globalvar.get_table()
    item = Item(name, typ, s1, s2)
    table.append(item)


def position(name):
    level = globalvar.get_level()  # 获取当前的层数
    index = globalvar.get_index()
    table = globalvar.get_table()
    for i in range(len(table)-1, -1, -1):  # 查询顺序好像有问题
        # if not table[i].typ == 'constant':
            #if table[i].lev == level:  # 为了防止找之前同层过程的变量
                if table[i].name == name:
                    return table.index(table[i])  # 这边应该可以优化
            #elif table[i].lev == level - 1:
             #   level -= 1
             #   i += 1
        # else:  # 常量的时候直接跳过

    return -1  # 当没有找到的时候 返回-1

# table.append(Item("hhh","constant", 66666))
# table.append(Item("hhh","constant", 66666))
# table.append(Item("hhh","variable", 66666))
# enter("hhh","constant", 66666)
# show()

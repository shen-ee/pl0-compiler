# coding:utf-8
import globalvar
import token
import tab
import generator
import error_handling


# def statement():
#
#     if(globalvar.get_symbol() == token.IF):
#         print( "bingo")
#     return 0


def program():  # 分析主程序
    block()  # 调用<分程序>的分析子程序
    # print(globalvar.get_stri())
    # print (globalvar.get_pointer())
    if globalvar.get_symbol() == token.FINAL:  # 将"."设置成FINAL标识
        print("success this is program!!!!!!!!!!!!!!!!!!!")
    else:
        print("error in program()")


def block():  # <分程序>的分析子程序
    index = 3
    globalvar.set_index(3)
    tx0 = len(globalvar.get_table())-1
    cx0 = generator.gen("jmp", 0, 0)  # 保存当前p-code指令在code列表中的位置

    while globalvar.get_symbol() == token.CONST:  # 判断是否为 常量说明部分
        constant_declare()
    while globalvar.get_symbol() == token.VAR:  # 判断是否为 变量说明部分
        var_declare()
    index = globalvar.get_index()  # 在这保存一下应该分配的大小
    while globalvar.get_symbol() == token.PROCEDURE:  # 判断是否为 过程说明部分
        proc_declare()
    # 是应该在这建符号表吗？？
    code = globalvar.get_code()  # 获取一个p-code表的副本
    table = globalvar.get_table()  # 获取一个符号表的副本
    code[cx0].s2 = len(globalvar.get_code())
    if not globalvar.get_level() == 0:  # 判断一下是不是最外层的程序，如果是的话则不修改表
        table[tx0].adr = len(globalvar.get_code())  # 将符号表中过程的adr值改为在p-code中的初始位置
        globalvar.set_table(table)
    generator.gen("int", 0, index)
    statement()  # 调用<语句>的分析子程序
    generator.gen("opr", 0, 0)
    print("this is block")


def constant_declare():  # <常量说明部分> 的分析子程序
    if globalvar.get_symbol() == token.CONST:  # 虽然这句好像没什么用
        token.getsym()
        constant_def()   # 调用<常量定义>的分析子程序
        while globalvar.get_symbol() == token.COMMASY:  # 判断有没有"，"
            token.getsym()  # 有的话向前读一格
            constant_def()  # 接着判断是不是常量定义
        if globalvar.get_symbol() == token.SEMISY:  # 如果有"；"，该条<常量说明部分>结束
            token.getsym()
            print("this is constant_declare")
        else:  # 没有;的情况
            error_handling.error(5)
            # print("error in constant_declare() -->no semi symbol")
            return 0
    else:
        print("error in constant_declare()")
        return 0


def constant_def():  # <常量定义> 的分析子程序
    ret = identifier()  # 调用标识符的分析子程序
    if ret == 0:  # 当得出不是标识符时
        error_handling.error(4)  # const后面应该是标识符，弹出错误信息4
    if globalvar.get_symbol() == token.EQUSY:  # 判断是否为等于号
        token.getsym()  # 读入一个字符
        ret = unsigned_int()  # 判断是否为数字
        if ret:  # ret 为真的时候表示确实是数字
            if globalvar.get_num() > token.MAX_NUM:
                error_handling.error(30)  # 数字过大，弹出错误信息30
                exit()
            tab.enter(globalvar.get_id_name(), "constant", globalvar.get_num())
            print("this is constant_def")
        else:  # ret 为假的时候表示后面跟的不是数字
            error_handling.error(2)  # =后面跟的不是数，弹出错误信息2
    elif globalvar.get_symbol() == token.ASSIGNSY:
        error_handling.error(1)  # 应该是=而不是:=，弹出错误信息1
    else:
        error_handling.error(3)  # 标识符后面应该是=，弹出错误信息3
        print("error in constant_def()  -->no equal symbol")
        return 0


def unsigned_int():  # <无符号整数>的分析子程序
    if globalvar.get_symbol() == token.INTSY:
        token.getsym()
        print("this is unsigned_int")
        return True
    else:
        print("error in unsigned_int()  -->not int")
        return 0


def identifier():  # <标识符> 的分析子程序
    name = globalvar.get_id_name()
    if globalvar.get_symbol() == token.IDSY:  # 判断是不是标识符
        token.getsym()  # 是的话读下一个token
        print("this is identifier")
        print(globalvar.get_id_name())
        return globalvar.get_id_name()
    else:
        print("error in identifier()")
        return 0
    return name


def var_declare():  # <变量说明部分>的分析子程序
    level = globalvar.get_level()
    index = globalvar.get_index()
    if globalvar.get_symbol() == token.VAR:  # 虽然这句好像没什么用
        token.getsym()  # 读入一个字符
        ret = identifier()  # 判断是否为标识符
        if ret == 0:  # 不是标识符的情况
            error_handling.error(4)  # var后面应该是标识符，弹出错误信息4
        tab.enter(globalvar.get_id_name(), "variable",level,index)  # 把这个变量加入符号表
        index += 1  # 相对地址+1
        while globalvar.get_symbol() == token.COMMASY:  # 判断接下来是不是逗号，即是不是还有变量
            token.getsym()
            identifier()
            tab.enter(globalvar.get_id_name(), "variable", level, index)  # 把这个变量加入符号表
            index += 1
            # print("index="+str(index))
        if globalvar.get_symbol() == token.SEMISY:  # 判断是否为分号，即语句是否结束
            token.getsym()
            print("this is var_declare")
            print(index)
            globalvar.set_index(index)
            # print("ggggggindex=" + str(globalvar.get_index()))
            # globalvar.set_level(level) # 但是这边应该不会改level的数值
        else:
            error_handling.error(5)  # 结束的时候没有分号，弹出错误信息5
            # print("error in var_declare() -->no semi symbol")
            return 0
    else:
        print("error in var_declare()")


def proc_declare():  # <过程说明部分>的分析子程序
    proc_head()  # 调用<过程首部>分析子程序
    print("head success!!!!")
    globalvar.set_level(globalvar.get_level()+1)
    block()  # 调用<分程序>分析子程序
    globalvar.set_level(globalvar.get_level()-1)
    print(globalvar.get_stri()[globalvar.get_pointer() - 3:globalvar.get_pointer() + 3])
    print("block success!!!")
    if globalvar.get_symbol() == token.SEMISY:
        token.getsym()
        print("this is proc_declare")
    else:
        error_handling.error(5)  # 结束的时候没有分号，弹出错误信息5
        # print("error in proc_declare()-->no semi symbol")
        print(globalvar.get_stri()[globalvar.get_pointer()-3:globalvar.get_pointer()+3])
        return 0
    while globalvar.get_symbol() == token.PROCEDURE:  # 判断还有没有<过程首部>
        proc_declare()  # 递归进行<过程说明部分>子程序


def proc_head():  # <过程首部>的分析子程序
    level = globalvar.get_level()
    index = globalvar.get_index()
    if globalvar.get_symbol() == token.PROCEDURE:  # 判断当前字符是不是 procedure
        token.getsym()
        ret = identifier()  # 判断是否为标识符
        if ret == 0:
            error_handling.error(4)  # procedure 后面应该是标识符，弹出错误信息4
        tab.enter(globalvar.get_id_name(),"procedure",globalvar.get_level(),globalvar.get_index())  # 在这将过程添加进符号表
        globalvar.set_index(globalvar.get_index()+1)  # 更新数据的指针
        if globalvar.get_symbol() == token.SEMISY:  # 判断当前token是不是 ；
            token.getsym()
            print("this is proc_head")
        else:
            error_handling.error(5)  # 结束的时候没有分号，弹出错误信息5
    else:
        print("error in proc_head()")


def statement():  # <语句> 的分析子程序
    if globalvar.get_symbol() == token.IDSY:  # 判读是否为赋值语句--》当前token是不是<标识符>
        assign_statement()
    elif globalvar.get_symbol() == token.IF:  # 判断是否为条件语句--》当前token是不是if
        # print("success!!!!!!")
        if_statement()
    elif globalvar.get_symbol() == token.WHILE:  # 判断是否为当循环语句--》当前token是不是while
        while_statement()
    elif globalvar.get_symbol() == token.CALL:  # 判断是否为过程调用语句--》当前token是不是call
        # print("here*********")
        proc_call_statement()
    elif globalvar.get_symbol() == token.BEGIN:  # 判断是否为复合语句--》当前token是不是 begin
        # print("here*********")
        mixed_statement()
    elif globalvar.get_symbol() == token.REPEAT:  # 判断是否为重复语句--》当前token是不是 repeat
        repeat_statement()
    elif globalvar.get_symbol() == token.READ:  # 判断是否为读语句--》当前token是不是read
        read_statement()
    elif globalvar.get_symbol() == token.WRITE:  # 判断是否为写语句--》当前token是不是write
        write_statement()
    else:  # 其他情况，包括：空和其他不知名符号
        print("other conditions in statement()")
    print("this is statement")


def assign_statement():  # <赋值语句> 的分析子程序
    name = identifier()
    i = tab.position(name)
    table = globalvar.get_table()
    if i == -1:
        error_handling.error(11)  # 赋值语句中的标识符未声明，弹出出错信息11
        # print("error in assign_statement-->no such variable")
        return 0
    else:
        if not table[i].typ == "variable":
            error_handling.error(12)  # 不可向常量或着过程赋值，弹出错误信息12
            # print("error in assign_statement-->not a variable")
            return 0
    if globalvar.get_symbol() == token.ASSIGNSY:
        token.getsym()
        expression()
        generator.gen("sto", globalvar.get_level()-table[i].lev, table[i].adr)
    else:
        error_handling.error(13)  # 应为赋值运算符，弹出错误信息13
    print("this is assign_statement")


def expression():  # <表达式> 的分析子程序
    if globalvar.get_symbol() == token.PLUSSY:  # 表达式开头可能会出现正负号
        token.getsym()
    elif globalvar.get_symbol() == token.MINUSSY:  # 这是出现负号的情况
        generator.gen("opr", 0, 1)  # 生成取负的指令
        token.getsym()
    term()  # 调用项的分析子程序，这是必须存在的
    while globalvar.get_symbol() == token.MINUSSY or globalvar.get_symbol() == token.PLUSSY:
        addop = addtion_operator()  # 记录此时的符号
        term()
        if addop == token.PLUSSY:
            generator.gen("opr",0,2)  # 生成加法指令
        else:
            generator.gen("opr",0,3)  # 生成减法指令
    print("this is expression")


def term():  # <项>的分析子程序
    factor()  # 调用<因子>分析子程序
    while globalvar.get_symbol() == token.STARSY or globalvar.get_symbol() == token.DIVISY:
        mulop=multiply_operator()
        factor()
        if mulop == token.STARSY:
            generator.gen("opr", 0, 4)
        else:
            generator.gen("opr", 0, 5)
    print("this is term")


def factor():  # <因子>的分析子程序
    if globalvar.get_symbol() == token.IDSY:
        name = identifier()
        i = tab.position(name)
        table = globalvar.get_table()
        if i == -1:  # 返回值为-1代表没有在符号表里找到
            error_handling.error(11)  # 因子中的标识符未声明，弹出出错信息11
            # print ("error in factor()")
        else:
            if table[i].typ == "constant":
                generator.gen("lit", 0, table[i].num)  # 产生指令，将第二个参数取到栈顶
            elif table[i].typ == "variable":
                generator.gen("lod", globalvar.get_level()-table[i].lev, table[i].adr)  # 将变量的值取到栈顶，第一个参数为层差，第二个参数为偏移量
            else:  # 是过程标识符
                error_handling.error(21)
                # print("error in factor()")

    elif globalvar.get_symbol() == token.INTSY:
        unsigned_int()
        if globalvar.get_num() > token.MAX_NUM:
            error_handling.error(30)
            return 0
        generator.gen("lit", 0, globalvar.get_num())
    elif globalvar.get_symbol() == token.LPARSY:  # 如果是左括号
        token.getsym()
        expression()
        if globalvar.get_symbol() == token.RPARSY:
            token.getsym()
        else:  # 没有右括号
            error_handling.error(22)  # 没有右括号，弹出错误信息22
            # print ("error in factor-->no right par")
    else:
        print("error in factor()")
        print(globalvar.get_pointer())
        return 0
    print("this is factor")  # 成功运行


def addtion_operator(): # <加法运算符>的分析子程序
    addop = globalvar.get_symbol()
    if globalvar.get_symbol() == token.MINUSSY or globalvar.get_symbol() == token.PLUSSY:
        token.getsym()
        print("this is addtion_operator")
    else:
        print("error in addtion_operator")
    # print("%%%%%%%%%%%%%")
    return addop


def multiply_operator():  # <乘法运算符>的分析子程序
    mulop = globalvar.get_symbol()
    if globalvar.get_symbol() == token.STARSY or globalvar.get_symbol() == token.DIVISY:
        token.getsym()
        print("this is multiply_operator")
    else:
        print("error in multiply_operator")
    return mulop


def condition():  # <条件>的分析子程序
    if globalvar.get_symbol() == token.ODD:  # 判断是否有odd
        token.getsym()
        expression()
        generator.gen("opr", 0, 6)  # 生成odd指令
    else:  # 普通的条件
        expression()
        relop = relation_operator()  # 保存关系符号的值
        expression()
        # 以下指令都是针对次栈顶和栈顶的比较
        if relop == token.EQUSY:
            generator.gen("opr", 0, 8)  # 生成比较是否相等的指令
        elif relop == token.NOEQUSY:
            generator.gen("opr", 0, 9)  # 生成比较是否不等的指令
        elif relop == token.LESSTHANSY:
            generator.gen("opr", 0, 10)  # 生成比较是否小于的指令
        elif relop == token.NOLESSTHANSY:
            generator.gen("opr", 0, 11)  # 生成比较是否大于等于的指令
        elif relop == token.MORETHANSY:
            generator.gen("opr", 0, 12)  # 生成比较是否大于的指令
        elif relop == token.NOMORETHANSY:
            generator.gen("opr", 0, 13)  # 生成比较是否小于等于的指令

    print("this is condition")


def relation_operator():  # <关系运算符> 的分析子程序
    x = globalvar.get_symbol()
    # 判断是否为六种关系运算符的一种
    if x == token.LESSTHANSY or x == token.NOLESSTHANSY or x == token.MORETHANSY or x == token.NOMORETHANSY or x == token.NOEQUSY or x == token.EQUSY:
        token.getsym()
        print("this is relation_operator")
    else:  # 该符号不是关系运算符
        error_handling.error(20)  # 应为关系运算符，弹出错误信息20
    return x


def if_statement():  # <条件语句> 的分析子程序
    if globalvar.get_symbol() == token.IF:
        token.getsym()
        condition()
        if globalvar.get_symbol() == token.THEN:
            token.getsym()
            generator.gen("jpc", 0, 0)
            cx1 = len(globalvar.get_code())-1  # 记录当前p-code位置
            statement()
            code = globalvar.get_code()  # 创建一个code副本
            if code[cx1].operator == 'jpc':
                code[cx1].s2 = len(globalvar.get_code())
            else:
                print("error$$$$$$$$$$$")
            globalvar.set_code(code)  # 更新p-code列表
            print("this is if_statement")
            if globalvar.get_symbol() == token.ELSE:
                token.getsym()
                generator.gen("jpc",0,0)
                cx2 = len(globalvar.get_code())-1  # 记录当前p-code位置
                statement()
                code = globalvar.get_code()  # 创建一个code副本
                if code[cx2].operator == 'jpc':
                    code[cx2].s2 = len(globalvar.get_code())
                else:
                    print("error$$$$$$$$$$$")
                globalvar.set_code(code)
        else:
            error_handling.error(16)  # 应该为then，弹出错误信息16
            # print("error in if_statement() -->no then")
            return 0
    else:
        print("error in if_statement() -->no if")
        return 0


def while_statement():  # <当循环语句> 的分析子程序
    if globalvar.get_symbol() == token.WHILE:
        cx1 = len(globalvar.get_code())  # 判断条件的p-code位置
        print("watch me ,判断条件在"+str(cx1))
        token.getsym()
        condition()
        cx2 = len(globalvar.get_code())-1+1  # 意思为循环结束的下一个位置
        generator.gen("jpc", 0, 0)  # 这里尚且不知道要跳转到哪，所以先把第二个参数置为0
        if globalvar.get_symbol() == token.DO:
            token.getsym()
            statement()
            generator.gen("jmp", 0, cx1)
            code = globalvar.get_code()  # 构造一个p-code副本
            if code[cx2].operator == 'jpc':
                code[cx2].s2 = len(globalvar.get_code())  # 这里修改了之前未决定的位置
            else:
                print("error!!!!!!!!"
                      "&&&&&&&&&&&&&&&&&&&&&&"
                      "$$$$$$$$$$$$$$$$$$$$$4")
            globalvar.set_code(code)
            print("this is while_statement")
        else:  # 没有do的情况
            error_handling.error(18)  # 应为do，弹出错误信息18
            # print("error in while_statement() -->no do")
            return 0
    else:
        print("error in while_statement() -->no while")
        return 0

def repeat_statement():
    cx1 = len(globalvar.get_code())  # 判断条件的p-code位置
    token.getsym()
    statement()
    while globalvar.get_symbol() == token.SEMISY:
        token.getsym()
        statement()
    if globalvar.get_symbol() == token.UNTIL:
        token.getsym()
        generator.gen("jpc",0,cx1)
    else:
        error_handling.error(19)


def proc_call_statement():  # <过程调用语句> 的分析子程序
    if globalvar.get_symbol() == token.CALL:
        token.getsym()
        name = identifier()  # 获取当前标识符的名字
        if name == 0:
            error_handling.error(14)  # call后面应为标识符，弹出错误信息14
            return 0
        i = tab.position(name)
        table = globalvar.get_table()
        if i == -1:
            error_handling.error(11)  # 过程调用语句中的标识符未声明，弹出出错信息11
            # print("error in proc_call_statement()-->no such name")
            return 0
        else:
            if not table[i].typ == 'procedure':
                error_handling.error(15)
                return 0
                # print("error in proc_call_statement()-->not a procedure")
        generator.gen("cal",globalvar.get_level()-table[i].lev,table[i].adr)
        print("this is proc_call_statement")
    else:
        print("error in proc_call_statement()-->no call")


def mixed_statement():  # <复合语句> 的分析子程序
    if globalvar.get_symbol() == token.BEGIN:
        token.getsym()
        statement()
        ##print("here*********")
        while globalvar.get_symbol() == token.SEMISY:
            token.getsym()
            statement()
        if globalvar.get_symbol() == token.END:
            token.getsym()
            print("this is mixed_statement")
        else:  # 没有end标记
            error_handling.error(17)  # 应该为'end'，弹出错误信息17
            # print("error in mixed_statement()--no end")
            # print(globalvar.get_stri()[globalvar.get_pointer() - 3:globalvar.get_pointer() + 3])
            return 0
    else:
        print ("error in mixed_statement()--no begin")


def read_statement():  # <读语句> 的分析子程序
    if globalvar.get_symbol() == token.READ:
        token.getsym()
        if globalvar.get_symbol() == token.LPARSY:  # 判断是否为左括号
            token.getsym()
            name = identifier()
            i = tab.position(name)
            table = globalvar.get_table()
            if i == -1:  # 返回值为-1代表没有在符号表里找到
                error_handling.error(11)  # 读语句中的标识符未声明，弹出出错信息11
                # print ("error in read_statement()")
            else:
                if not table[i].typ == "variable":
                    error_handling.error(12)  # 不可向常量或着过程赋值，弹出错误信息12
                    # print("error in assign_statement-->not a variable")
                    return 0
                generator.gen("red", globalvar.get_level()-table[i].lev, table[i].adr)
            while globalvar.get_symbol() == token.COMMASY:
                token.getsym()
                name = identifier()
                i = tab.position(name)
                table = globalvar.get_table()
                if i == -1:  # 返回值为-1代表没有在符号表里找到
                    error_handling.error(11)  # 读语句中的标识符未声明，弹出出错信息11
                    #print ("error in read_statement()")
                else:
                    if not table[i].typ == "variable":
                        error_handling.error(12)  # 不可向常量或着过程赋值，弹出错误信息12
                        # print("error in assign_statement-->not a variable")
                        return 0
                    generator.gen("red", globalvar.get_level() - table[i].lev, table[i].adr)
            # print("here******")
            # print(globalvar.get_pointer())
            # print(globalvar.get_symbol())
            if globalvar.get_symbol() == token.RPARSY:  # 判断是不是右括号
                token.getsym()
                print("this is read_statement")
            else:
                error_handling.error(22)  # 缺少右括号，弹出错误信息22
                print (globalvar.get_symbol())
                # print("error in read_statement()--no )")
                return 0
        else:
            error_handling.error(40)  # 缺少左括号，弹出错误信息40
            # print ("error in read_statement()--no (")
            exit()
    else:
        print ("error in read_statement()--no read")
        return 0


def write_statement():  # <写语句>的分析子程序
    if globalvar.get_symbol() == token.WRITE:
        token.getsym()
        if globalvar.get_symbol() == token.LPARSY:  # 判断是否有左括号
            token.getsym()
            expression()
            generator.gen("wrt", 0, 0)  # 生成输出指令
            while globalvar.get_symbol() == token.COMMASY:
                token.getsym()
                expression()
                generator.gen("wrt", 0, 0)  # 生成输出指令
            if globalvar.get_symbol() == token.RPARSY:
                token.getsym()
                print("this is write_statement")
            else:  # 缺少右括号
                error_handling.error(22)  # 缺少右括号，弹出错误信息22
                # print("error in write_statement()--no )")
                return 0
        else:
            error_handling.error(40)  # 缺少左括号，弹出错误信息40
            # print ("error in write_statement()--no (")
            # return 0
            return 0
    else:
        print ("error in write_statement()--no write")
        return 0


# def alpha(): # <字母> 的分析子程序
#     print("this is alpha")
#
#
# def digit(): # <数字> 的分析子程序
#     print("this is digit")


# 下面是主程序

# token.getsym()
# program()
#tab.show()
#generator.show()
#tab.show()
#print(globalvar.get_pointer())


#stri="if"
#token.getsym()
#print(stri)
#print(symbol)
#statement()

# globalvar.show()
# globalvar.set_stri("if if#####")
# print("***************")
# globalvar.show()
# token.getsym()
# print("***************")
# statement()
# globalvar.show()
# token.getsym()
# statement()

#token.getsym()
#statement()
#print(globalvar.get_symbol())
# token.getsym()
# print(globalvar.get_symbol())
# coding:utf-8

# import grammar
import globalvar
reserve = ["const", "var", "procedure", "odd", "if",\
           "then", "while", "do", "call", "begin",\
           "end", "read", "write", "else", "repeat", "until"]

CONST = 1
VAR = 2
PROCEDURE = 3
ODD = 4
IF = 5
THEN = 6
WHILE = 7
DO = 8
CALL = 9
BEGIN = 10
END = 11
READ = 12
WRITE = 13

ELSE = 14
REPEAT = 15
UNTIL = 16

IDSY = 20  #
INTSY = 21  #
PLUSSY = 22  # +
MINUSSY = 23  # -
STARSY = 24  # *
DIVISY = 25  # ／
LPARSY = 26  # (
RPARSY = 27  # )
COMMASY = 28  # ,
SEMISY = 29  # ;
COLONSY = 30  # :
ASSIGNSY = 31  # :=
EQUSY = 32  # =
LESSTHANSY = 33  # <
MORETHANSY = 34  # >
NOLESSTHANSY = 35  # >=
NOMORETHANSY = 36  # <=
NOEQUSY = 37  # <>
FINAL = 233  # .
MAX_NUM = 2047

token = ""  # 表示当前的字符串
ch = ""  # 表示当前字符
# pointer = 0

# stri = grammar.stri# 输入的字符串
# symbol = grammar.symbol
# num = grammar.num
stri = globalvar.get_stri()
symbol = globalvar.get_symbol()
num = globalvar.get_num()
pointer = globalvar.get_pointer()
id_name = globalvar.get_id_name()


def getsym():
    global ch,reserve,IDSY,INTSY,token,pointer,symbol,stri,num,id_name
    global IDSY,INTSY,PLUSSY,MINUSSY

    stri = globalvar.get_stri()
    symbol = globalvar.get_symbol()
    num = globalvar.get_num()
    pointer=globalvar.get_pointer()

    clearToken() # 将之前的字符串置为为空
    getchar()
    while isSpace() or isNewline() or isTab():
        getchar()

    if isLetter():  # 判断当前ch是字母的时候
        while isLetter() or isDigit():
            catToken()
            getchar()
        retract()  # 当发现不是数字也不是字母的时候，停止扫描，指针回退一格
        resultValue = reserver()  # 返回了保留字在list中的位置序号
        if resultValue == 0:  # 等于0说明是标识符
            symbol = IDSY
            id_name = token
        else:  # 说明这是保留字
            symbol = resultValue  # symbol置为保留字list的序号

    elif isDigit(): # 判断当前ch是数字的时候
        while isDigit(): # 当是数字的时候就一直扫描下去
            catToken()
            getchar()
        retract() # 发现不是数字的时候停止扫描，指针回退一格
        num = transNum() # 将token由字符串转为数字存进num里
        symbol = INTSY

    elif isColon():
        getchar()
        if isEqu():
            symbol=ASSIGNSY
        else:
            retract()
            symbol=COLONSY

    elif isPlus():
        symbol = PLUSSY
    elif isMinus():
        symbol = MINUSSY
    elif isStar():
        symbol = STARSY
    elif isStar():
        symbol = STARSY
    elif isDivi():
        symbol = DIVISY
    elif isLpar():
        symbol = LPARSY
    elif isRpar():
        symbol = RPARSY
    elif isComma():
        symbol = COMMASY
    elif isSemi():
        symbol = SEMISY
    elif isEqu():
        symbol = EQUSY
    elif isLessthan():
        getchar()
        if isEqu():
            symbol = NOMORETHANSY
        elif isMorethan():
            symbol = NOEQUSY
        else:
            retract()
            symbol = LESSTHANSY
    elif isMorethan():
        getchar()
        if isEqu():
            symbol = NOLESSTHANSY
        else:
            retract()
            symbol = MORETHANSY
    elif ch == '.':
        symbol = FINAL
    else:
        print("error in getsym()")
        symbol = 999
    # print("getsym end")
    globalvar.set_num(num)
    globalvar.set_symbol(symbol)
    globalvar.set_pointer(pointer)
    globalvar.set_id_name(id_name)


def clearToken(): # 清除token中的内容
    global token
    token = ""


def reserver():#返回 token 在保留字中的位置
    global token,reserve
    # print("loading")
    if token in reserve: # 如果token在保留字中，返回它的序号
        return reserve.index(token)+1
    else: # 不在的话返回0
        return 0
    # print("this is resever")


def getchar(): # 获取当前指针所在字符，并将指针向前移动
    global ch,pointer,stri
    ch = stri[pointer] # 获取当前指针所在字符
    pointer = pointer + 1
    # print("this is getchar")


def catToken(): #将连续的字母或数字组成一个字符串
    global token,ch
    token = token + ch
    # print("this is catToken")


def retract(): # 使指针回退一格
    global pointer,ch,srti
    pointer = pointer-1
    # print("this is retract")


def transNum(): # 将数字由字符串转为整形
    return int(token)


def isLetter(): #判断当前ch是不是字母
    global ch
    if ch.isalpha():
        return True
    else:
        return False
    print("this is isLetter")


def isSpace(): # 判断当前ch是不是空格
    global ch
    if ch==" ":
        return True
    else:
        return False


def isTab(): # 判断当前ch是不是Tab
    global ch
    if ch=="\t":
        return True
    else:
        return False


def isNewline():  # 判断当前ch是不是换行符
    global ch
    if ch=="\n" or ch == '\r':  # 本来只判断了\n，后来发现换行还有一种是\r
        return True
    else:
        return False


def isDigit():
    global ch
    if ch.isdigit():
        return True
    else:
        return False
    print("this is isDigist")


def isColon():
    global ch
    if ch == ":":
        return True
    else:
        return False


def isPlus():
    global ch
    if ch == "+":
        return True
    else:
        return False


def isMinus():
    global ch
    if ch == "-":
        return True
    else:
        return False


def isEqu():
    global ch
    if ch == "=":
        return True
    else:
        return False


def isStar():
    global ch
    if ch == "*":
        return True
    else:
        return False


def isDivi():
    global ch
    if ch == "/":
        return True
    else:
        return False


def isLpar():
    global ch
    if ch == "(":
        return True
    else:
        return False


def isRpar():
    global ch
    if ch == ")":
        return True
    else:
        return False


def isComma():
    global ch
    if ch == ",":
        return True
    else:
        return False


def isSemi():
    global ch
    if ch == ";":
        return True
    else:
        return False


def isLessthan():
    global ch
    if ch == "<":
        return True
    else:
        return False


def isMorethan():
    global ch
    if ch == ">":
        return True
    else:
        return False


def show():
    global symbol,num,token
    if symbol == 20:
        print("this is identifier")
        print(token)
    elif symbol == 21:
        print("this is number")
        print(token)
        print(num)
    elif symbol == 22:
        print("this is plus")
        print(token)
    elif symbol == 23:
        print("this is minus")
        print(token)
    elif symbol == 24:
        print("this is star")
        print(token)
    elif symbol == 25:
        print("this is divi")
        print(token)
    elif symbol == 26:
        print("this is lpar")
        print(token)
    elif symbol == 27:
        print("this is rpar")
        print(token)
    elif symbol == 28:
        print("this is comma")
        print(token)
    elif symbol == 29:
        print("this is semi")
        print(token)
    elif symbol == 30:
        print("this is colon")
        print(token)
    elif symbol == 31:
        print("this is assign")
    elif symbol == 32:
        print("this is equal")
    elif symbol == 33:
        print("this is lessthan")
    elif symbol == 34:
        print("this is morethan")
    elif symbol == 35:
        print("this is nolessthan")
    elif symbol == 36:
        print("this is nomorethan")
    elif symbol == 37:
        print("this is noequal")
    elif symbol > 0 and symbol < 20 :
        print("this is reserver")
        print(token)
        print("number="+str(symbol))
    else:
        print("error in getsym()")

# 以下是测试

# stri="444444 444 hhhh \n\t const var + - := <> <>==#"
# while(ch != "#"):
#     getsym()
#     show()
#     print("")
#stri="if###"
#getsym()

# print(globalvar.get_num())
# print(globalvar.get_stri())
# print(globalvar.get_symbol())
# print(num)
# print(stri)
# print(symbol)
# getsym()
# print(symbol)
# print(globalvar.get_symbol())
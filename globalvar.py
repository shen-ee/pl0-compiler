# coding:utf-8
class GlobalVar:
    symbol = 0
    num = 0
    id_name = ""
    # stri = "const i=7,ii=7 ;var k,q;procedure swap;var k;k:=-8+8-8;."
    # stri = "procedure proc; ;."  # 检测有过程声明的最简情况
    # stri = "procedure kk;var k;;."
    # stri = "kk:=4*4+4."
    # stri = "if 1=1 then kk:=4."
    # stri = "while 1=1 do kk:=4."
    # stri = "call jjj."
    # stri = "begin kk:=44;gg:=77 end."  # 测试复合语句
    # stri = "read (hhh)."
    # stri = "write (4*4)."
    # stri = "kkk := -7."
    stri = "const a = 45,b=27;" \
           "var x,y,g,m;" \
           "procedure swap;" \
           "    var temp;" \
           "    begin" \
           "        temp :=x;" \
           "        x:=y;" \
           "        y:=temp" \
           "    end;" \
           "procedure mod;x:=x-x/y*y;" \
           "begin" \
           "    x:=a;" \
           "    y:=b;" \
           "    call mod;" \
           "    while x<>0 do" \
           "        begin" \
           "            call swap;" \
           "            call mod" \
           "        end;" \
           "    g:=y; "\
           "    m:=a*b/g;" \
           "    write(g,m)" \
           "end."

    pointer = 0
    table = []
    level = 0
    index = 0
    cx = 0  # code_index 表示生成代码的行数
    code = []  # 表示生成pcode的list
    error_happen = 0
    error = []


def reset():
    GlobalVar.symbol = 0
    GlobalVar.num = 0
    GlobalVar.id_name = ""
    GlobalVar.stri = ""
    GlobalVar.pointer = 0
    GlobalVar.table = []
    GlobalVar.level = 0
    GlobalVar.index = 0
    GlobalVar.cx = 0  # code_index 表示生成代码的行数
    GlobalVar.code = []  # 表示生成pcode的list
    GlobalVar.error_happen = 0
    GlobalVar.error = ""


def get_cx():
    return GlobalVar.cx

def set_cx(cx):
    GlobalVar.cx = cx


def get_code():
    return GlobalVar.code

def set_code(code):
    GlobalVar.code = code


def get_index():
    return GlobalVar.index


def set_index(index):
    GlobalVar.index = index


def get_level():
    return GlobalVar.level


def set_level(level):
    GlobalVar.level = level


def set_symbol(sy):
    GlobalVar.symbol=sy


def get_symbol():
    return GlobalVar.symbol


def set_num(number):
    GlobalVar.num = number


def get_num():
    return GlobalVar.num


def set_stri(strii):
    GlobalVar.stri = strii


def get_stri():
    return GlobalVar.stri


def set_pointer(ptr):
    GlobalVar.pointer = ptr


def get_pointer():
    return GlobalVar.pointer


def set_id_name(identifier):
    GlobalVar.id_name = identifier


def get_id_name():
    return GlobalVar.id_name


def get_table():
    return GlobalVar.table


def set_table(table):
    GlobalVar.table = table


def get_error_happen():
    return GlobalVar.error_happen


def set_error_happen(happen):
    GlobalVar.error_happen = happen


def get_error():
    return GlobalVar.error


def set_error(error):
    GlobalVar.error = error



def show():
    print("symbol="+str(GlobalVar.symbol))
    print("num="+str(GlobalVar.num))
    print("stri="+GlobalVar.stri)
    print("pointer="+str(GlobalVar.pointer))

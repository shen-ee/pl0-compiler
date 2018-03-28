# coding:utf-8
import globalvar
import token
import tab
import generator
import grammar
from Tkinter import *

# file = raw_input("请输入文件名：")
# file = "test.txt"
# f = open(file).read()
# print(f)
# f = "const true =  1,false=0;" \
#   "var x,y,m,n,pf;" \
#   "procedure prime;" \
#   " var i,f;" \
#   " procedure mod;" \
#   "     x:=x-x/y*y;" \
#   " begin" \
#   "     f:=true;" \
#   "     i:=3;" \
#   "     while i<m do" \
#   "         begin" \
#   "             x:=m;" \
#   "             y:=i;" \
#   "             call mod;" \
#   "             if x=0 then f:=false;" \
#   "             i:=i+2" \
#   "         end;" \
#   "     if f=true then" \
#   "         begin" \
#   "             write(m);" \
#   "             pf:=true" \
#   "         end" \
#   "     end;" \
#   " begin" \
#   "     pf:=false;" \
#   "     read(n);" \
#   "     while n>=2 do" \
#   "     begin" \
#   "         write(2);" \
#   "         if n=2 then pf:=true;" \
#   "         m:=3;" \
#   "         while m<=n do" \
#   "             begin" \
#   "                 call prime;" \
#   "                 m:=m+2" \
#   "             end;" \
#   "         read(n)" \
#   "     end;" \
#   "     if pf=false then write(0)" \
#   "end."
# f = "const constant := 0;."  # error1 的出错情况
# f = "const constant = 0;."
# f = "const constant = tt;."  # error2 的出错情况
# f = "const constant = 1;."
# f = "const constant 1;."  # error3 的出错情况
# f = "const constant  = 1;."
# f = "const = 1;."  # error4 的出错情况
# f = "var = 1;."
# f = "procedure = 1;."
# f = "const constant = 1;var variable;."
# f = "const constant = 1."
# f = "procedure tt;;."
# f = "const constant = 1."  # error5 的出错情况:<常量说明部分>没有分号
# f = "var variable = 1."  # error5 的出错情况:<变量说明部分>没有分号
# f = "procedure tt."  # error5 的出错情况:<过程首部>没有分号
# f = "procedure proc;var variable;."  # error5 的出错情况:<过程说明部分>没有分号
# f = "procedure proc;var variable;;."
# f = " "  # error 6 不知道要干什么
# f = "var tt;ts := 4."  # error 11的出错情况：赋值语句中的identifier未声明
# f = "procedure proc;;call prob."  # error 11的出错情况：过程调用语句中的identifier未声明
# f = "var variable;read(vari)."  # error 11的出错情况：读语句中的identifier未声明
# f = "var variable;variable := varia +1."  # error 11的出错情况：因子中的identifier未声明
# f = "const constant=3;var variable;procedure proc ;; proc :=1."  # error 12的出错情况：向过程赋值
# f = "const constant=3;var variable;procedure proc ;; constant :=1."  # error 12的出错情况：向常量赋值
# f = "const constant=3;var variable;procedure proc ;; read(constant)."  # error 12的出错情况：向常量赋值
# f = "const constant=3;var variable;procedure proc ;; read(proc)."  # error 12的出错情况：向过程赋值
# f = "const constant=3;var variable;procedure proc ;; variable = 3."  # error 13的出错情况：应为赋值运算符
# f = "const constant=3;var variable;procedure proc ;; call 333."  # error 14的出错情况：call后面应为标识符
# f = "const constant=3;var variable;procedure proc ;; call constant."  # error 15的出错情况：调用常量
# f = "const constant=3;var variable;procedure proc ;; call variable."   # error 15的出错情况：调用变量
# f = "const constant=3;var variable;procedure proc ;; if 1=1 hahaha."  # error 16的出错情况：没有then
# f = "const constant=3;var variable;procedure proc ;; begin variable :=4 ."  # error 17的出错情况：没有end符号
# f = "const constant=3;var variable;procedure proc ;; while 1=1 ."  # error 18的出错情况：没有do
# f = "const constant=3;var variable;procedure proc ;; while 1 1 do variable :=4 ."  # error 20的出错情况：没有关系运算符
# f = "const constant=3;var variable;procedure proc ;; variable := 1 + proc."  # error 21的出错情况：表达式中出现了过程标识符
# f = "const constant=3;var variable;procedure proc ;; variable := (1 + 2."  # error 22的出错情况：因子中缺少右括号
# f = "const constant=3;var variable;procedure proc ;; read(variable ."  # error 22的出错情况：读语句中缺少右括号
# f = "const constant=3;var variable;procedure proc ;; write(variable ."  # error 22的出错情况：写语句中缺少右括号
# f = "const constant=2066;var variable;procedure proc ;;."  # error 30的出错情况：声明了过大的常量
# f = "consT constant=3;var variable;procedure proc ;; variable := 206."  # error 30的出错情况：因子中的数过大
# f = "const constant=3;var variable;procedure proc ;; read variable ) ."  # error 40的出错情况：读语句中没有左括号
# f = "const constant=3;var variable;procedure proc ; write variable) ."  # error 40的出错情况：写语句中没有左括号
# f = "var variable;const constant;procedure proc;; variable := proc +1 ."
# f = "const constant=3;var variable;procedure proc ; read(variable)."

# f=f.lower()
# globalvar.set_stri(f)
# token.getsym()
# grammar.program()
# tab.show()
# generator.show()
# tab.show()
# print(globalvar.get_error_happen())

root = Tk()

class App:
    def __init__(self, master):
        frame1 = Frame(master)
        frame1.pack()
        frame2 = Frame(master)
        frame2.pack()
        w = Label(frame1,text="输入文件名")
        w.pack()
        self.e = Entry(frame1)
        button = Button(frame1,text="确认",command = self.confirm)
        self.e.pack()
        button.pack()
        roll = Scrollbar(frame2, orient=VERTICAL)
        self.result = Text(frame2,yscrollcommand=roll.set)
        roll.config(command =self.result.yview)
        roll.pack(fill="y", expand=0, side=RIGHT, anchor=N)
        self.result.pack()

    def confirm(self):
        file = self.e.get()
        f = open(file).read()
        f = f.lower()
        globalvar.set_stri(f)
        token.getsym()
        grammar.program()
        # tab.show()
        # generator.show()
        tab.show()
        final_string = ''
        if globalvar.get_error_happen():
            error = globalvar.get_error()
            final_string = error
        else:
            code = globalvar.get_code()
            for i in code:
                final_string += str(code.index(i))+"  "+str(i.operator)+"  "+str(i.s1)+"  "+str(i.s2)+'\n'
        self.result.delete(0.0, END)
        self.result.insert(1.0,final_string)
        globalvar.reset()


app = App(root)
root.mainloop()

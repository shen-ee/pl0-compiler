
stack = []
class Item:
    def __init__(self,name,typ,c):
        self.name = name
        self.typ = typ
        self.c = c

ll = Item("hahaha",1,6)
lll = Item("hahahaha",2,6)
stack.append(ll)
stack.append(lll)
print(stack.pop().name)
print(stack.pop().name)
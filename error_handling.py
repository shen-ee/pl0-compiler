# coding:utf-8
import globalvar


def error(number):
    switcher = {
        1: "error 1:There should be an equal symbol.",
        2: "error 2:There should be a number following '='.",
        3: "error 3:There should be an equal symbol following identifier.",
        4: "error 4:There should be '=' following 'var''const''procedure'.",
        5: "error 5:A ';' or ',' missing.",
        6: "error 6:Mistake character after procedure declaration.",
        7: "error 7:There should be a statement.",
        8: "error 8:Mistake character in block.",
        9: "error 9:There should be a '.'",
        10: "error 10:Missing ';' between statements",
        11: "error 11:Identifier undeclared.",
        12: "error 12:Cannot assign a constant or a procedure.",
        13: "error 13:It should be a ':='",
        14: "error 14:There should be an identifier following call.",
        15: "error 15:Cannot call a constant or a variable.",
        16: "error 16:It should be 'then'.",
        17: "error 17:It should be ';'or'end'.",
        18: "error 18:It should be 'do'.",
        19: "error 19:Wrong characters after statement.",
        20: "error 20:It should be a relation operator.",
        21: "error 21:There cannot be a procedure identifier in expressions.",
        22: "error 22:Missing ')'.",
        23: "error 23:Cannot be this character after factor.",
        24: "error 24:Expressions cannot start with this character.",
        30: "error 30:Too large a number.",
        40: "error 40:It should be a '('."
    }
    print(switcher.get(number,"nothing"))

    error = switcher.get(number,"nothing")
    if not globalvar.get_error_happen():
        globalvar.set_error(error)
    globalvar.set_error_happen(1)


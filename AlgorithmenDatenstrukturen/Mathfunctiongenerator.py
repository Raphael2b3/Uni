import math as math


def CUSTOM_UNUSED_EVAL(str=""):
    tree = []
    buffer = []
    str.replace("log(", "l")

    for s in str:
        if s == " ": continue

        if s == "(":
            buffer.append(tree)
            tree = []
        if s == ")":
            buffer[-1].append(tree)
            tree = buffer.pop()
        if s == "l":
            buffer[-1] = ""

    def func(x):
        eval(str, x)


def str_to_func(str=""):
    def func(x):
        return eval(str, {"x": x, "math": math})

    return func

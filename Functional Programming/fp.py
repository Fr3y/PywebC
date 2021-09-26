#functional programming
def apply_twice(func,arg):
    return func(func(arg))
def ass_five(x):
    return x+5
print(apply_twice(ass_five, 10))

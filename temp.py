var_1 = (1, 2)
def test(a, b, *arg):
    print(type(arg), arg)
    return a + b + sum(*arg)
print(test(*var_1, (1, 3)))

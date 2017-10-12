'''
kwargs refers to a keyword variable-length argument list
** maps the kwargs nd pass them to a function as a non-positional argument
'''
def method(arg1, arg2, arg3):
    print("arg1: {}".format(arg1))
    print("arg2: {}".format(arg2))
    print("arg3: {}".format(arg3))

if __name__ == "__main__":
    kwargs = {"arg3":3, "arg2":"two","arg1":1}
    method( **kwargs )

'''
 output:

arg1: 1
arg2: two
arg3: 3
'''
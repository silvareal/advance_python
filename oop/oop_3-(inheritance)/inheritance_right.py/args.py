'''
before showing the further example of the right way to call an inheritance
we need to know what *args and **kwargs is
*args refers to a non keyword argument variable list
* unpackes content inside the list args and pass to a function as position argument
'''

def method2( f_arg, *args):
    print("the first arg( {} )is normal".format(f_arg))
    for f in args:
        print("the next arg is: {}".format(f))

if __name__ == "__main__":
    method2("lorem", "ipsum", "struggles", "lorem", "ipsum", "struggles")

'''
outpuut:

the first arg( lorem )is normal
the next arg is: ipsum
the next arg is: struggles
the next arg is: lorem
the next arg is: ipsum
the next arg is: struggles
'''
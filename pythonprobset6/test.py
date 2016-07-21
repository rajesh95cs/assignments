def fun(a, funarg):
    print "a inside fun is ", a
    funarg(2,3)

def fun1(a, b):
    print "inside funarg here fun1"
    print a + b

fun(4, fun1)   

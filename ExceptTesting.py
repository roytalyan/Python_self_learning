# -*- coding: utf-8 -*-

def test():
    try:
        print 'this is before exception'
        raise Exception, "test"
        print 'this is after exception'

    except:
        print 'this is in except'
    finally:
        print 'this is in finally'


def test2():
    try:
        print 'this is before exception'
        # raise test
        print 'this is after exception'
    except:
        print 'in except'
    else:
        print 'this is in else'

test2()

# def mye( level ):
#     if level < 1:
#         raise Exception,"Invalid level!"
#         # 触发异常后，后面的代码就不会再执行
# try:
#     mye(0)            # 触发异常
# except Exception,err:
#     print 1,err
# else:
#     print 2
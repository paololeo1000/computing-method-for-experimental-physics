import os

def join1(*args):
    """Horrible: do not use the + operator with string in a loop.
    """
    out = ''
    for arg in args:
        out += '%s/' % arg
    return out.rstrip('/')

def join2(*args):
    """This a more sensible version---and you get the idea of the *.
    """
    return '/'.join(args)

def join3(*args):
    """Even better---this will work on any OS.
    """
    sep = os.path.sep
    return sep.join(args)

print(join1('path', 'to', 'file'))
print(join2('path', 'to', 'file'))
print(join3('path', 'to', 'file'))

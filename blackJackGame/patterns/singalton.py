class SingletonType(type):
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(SingletonType, cls).__call__(*args, **kw)
        return cls.instance


class Singleton(object):
    __metaclass__ = SingletonType

    def do_something(self):
        print('Singleton')


s = Singleton()
s.do_something()

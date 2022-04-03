from datetime import datetime
from time import time


class MyClass:
    def __init__(self):
        self.init_time = time()

    def __str__(self):
        dt = datetime.fromtimestamp(self.init_time)
        return 'MyClass1 created at {:%H:%M on %m-%d-%Y}'. \
            format(dt)


class MyClass2:
    def __init__(self):
        self.init_time = time()

    def __str__(self):
        dt = datetime.fromtimestamp(self.init_time)
        return 'MyClass2 created at {:%H:%M on %m-%d-%Y}'. \
            format(dt)


class MyClass3:
    def __init__(self):
        self.init_time = time()

    def add(self, a, b):
        return a + b

    def __str__(self):
        dt = datetime.fromtimestamp(self.init_time)
        return 'MyClass3 created at {:%H:%M on %m-%d-%Y} ;)'. \
            format(dt)

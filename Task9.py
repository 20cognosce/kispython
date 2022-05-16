class main(object):
    states = ['a', 'b', 'c', 'd', 'e', 'f']

    def __init__(self):
        self.state = 'a'

    def crush(self):
        if self.state == 'a':
            self.state = 'd'
            return 1
        if self.state == 'b':
            self.state = 'c'
            return 3
        if self.state == 'c':
            self.state = 'd'
            return 4
        if self.state == 'd':
            self.state = 'd'
            return 7
        if self.state == 'e':
            self.state = 'f'
            return 8
        else:
            raise KeyError

    def visit(self):
        if self.state == 'a':
            self.state = 'b'
            return 0
        else:
            raise KeyError

    def spawn(self):
        if self.state == 'a':
            self.state = 'e'
            return 2
        if self.state == 'c':
            self.state = 'e'
            return 5
        if self.state == 'd':
            self.state = 'e'
            return 6
        else:
            raise KeyError


o = main()

print(o.visit())  # 0
print(o.crush())  # 3
print(o.crush())  # 4
print(o.visit())  # KeyError
print(o.crush())  # 7
print(o.visit())  # KeyError
print(o.crush())  # 7
print(o.visit())  # KeyError
print(o.spawn())  # 6
print(o.visit())  # KeyError
print(o.crush())  # 8



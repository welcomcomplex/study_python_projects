class A:
    def hello(self):
        print("Hello from A")
class B(A):
    def hello(self):
        print("Hello from B")
        super().hello()  # This will call the hello method of class A
class C(A):
    def hello(self):
        print("Hello from C")
        super().hello()  # This will call the hello method of class B
class D(B,C):
    def hello(self):
        print("Hello from D")
        super().hello()  # This will call the hello method of class C

d = D()
d.hello()  # This will call the hello method of class D
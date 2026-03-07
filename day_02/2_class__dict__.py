class A:
    x = 1

a = A()
a.y = 2

print(a.__dict__)      # → ?
print(A.__dict__.keys())  # → ?（只写 keys，不写值）
print(hasattr(a, 'x'))   # → ?
print(hasattr(a, 'y'))   # → ?

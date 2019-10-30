def foo(a):
    if a == 1:
        return 1
    else:
        return a * foo(a-1)

print(foo(3))

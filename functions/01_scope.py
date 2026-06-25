# username = "chaiaurcode"

# def func():
#     username = "chai"
#     print(username)

# print(username)
# func()

# x  = 99
# def func2(y):
#     z = x + y
#     return z

# print(func2(1))


# x  = 99 
# def func3():
#     x =88
#     print(x)

# func3()

# x = 99

# def func4():
#     global x
#     x = 12
    
# func4()
# print(x)

# x = 99 
# def f1():
#    x = 88 
#    def f2():
#        print(x)
#    return f2
    
# result = f1()
# result()
x = 99
def chaicoder(num):
    def actual(x):
        return x**num
    return actual

f = chaicoder(2)
g = chaicoder(3) 

print(f(3))
print(g(3))



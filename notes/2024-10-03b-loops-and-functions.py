
# i = 0
# while i < 10:
#     print(i)
#     if i == 4:
#         break

#     # if i % 2 == 1:
#     #     continue
#     # i = i + 1
#     i += 1

# for i in range(0, 10):
#     print(i)
#     if i % 2 == 1:
#         continue
#     print('Done with', i)

# for i in range(0, 5, 2):
#     print(i)

# s = "abcdefghijklmnop"
# print(s[0:10:3])
# print(s[:5])
# print(s[12:])
# print('[' + s[1000:] + ']')
# print(s[:-3])
# print(s[7:3:-1])
# print(s[1:3:-1])

# for i in range(1, 10, 4):
#     print(i)

# def doit():
#     for x in range(2, 10):
#         for y in range(10):
#             if y == x:
#                 print('Found it!', x, y)
#                 return
# doit()

# def foo(x):
#     return x
#     print('foo(' + x + ')')

# ret = foo('hi')
# print(ret)

def bar(a, b='B', c=True):
    print('--- bar() ---')
    print('a =', a)
    print('b =', b)
    print('c =', c)

bar(1, 'hi', False)
bar(2, c='C')

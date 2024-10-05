import sys

print('sys.argv:')
print(sys.argv)

# print('Your name: ')
# name  = input()
# color = input('Your favorite color: ')

# print(name + '\'s favorite color is ' + color)

for line in sys.stdin:
    print('You said: ' + line, end='')

print('Done!')

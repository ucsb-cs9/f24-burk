# # Read from stdin
# x = input('Enter something: ')
# print('You said', x)
# print('Your input is a', type(x))

# # But I wanted an int...
# x = int(x)

# print('Your input squared is ' + str(x * x))

# mylist = [1, 1, 2, 3, 5, 8, 13]
# for x in mylist:
#     print(x)

# for x in mylist:
#     print(x)
# exit()

# # Read from a file
# file = open('2024-10-08-input.txt')
# # all_the_text = file.read()
# # print(all_the_text, end='')

# line_number = 1
# for line in file:
#     print(line_number, line, end='')
#     line_number += 1

# file.close()
# file = open('2024-10-08-input.txt', 'rb')

# all_the_text = file.read()
# print(type(all_the_text))
# print(all_the_text, end='')

# file.close()


# # But remembering to close() is hard...
# with open('2024-10-08-input.txt') as file:
#     lines = 0
#     for line in file:
#         lines += 1
#     print('The file had ' + str(lines) + ' lines.')

# print('Outside the with block.')

# with open('2024-10-08-input.txt', 'rb') as file:
#     print(file.read(12))
#     print(file.readline())


# with open('2024-10-08-output.txt', 'w') as file:
#     file.write('Hello!\n')

import sys
# print(type(sys.stdout))
# sys.stdout.write('Hello?\n')
# sys.stderr.write('This went to sys.stderr...\n')

for line in sys.stdin:
    print('[' + line.strip() + ']')

# Connect `cat`s stdout with your program's stdin
# cat 2024-10-08-input.txt | python3 2024-10-08-files.py 

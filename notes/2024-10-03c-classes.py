# a = ['purple', 12]
# b = ['green',  10]

# def print_bb_info(bb):
#     print('Color is', bb[0])
#     print('Weight is', bb[1], 'pounds.')

# print_bb_info(a)

# c = [8, 'red']
# print_bb_info(c)

class BowlingBall:
    def __init__(self, color, weight=10, owner=None):
        self.color  = color
        self.weight = weight
        self.owner  = owner

def print_bb_info(bb):
    print('Color is',  bb.color)
    print('Weight is', bb.weight, 'pounds.')
    print('Owner is',  bb.owner)

a = BowlingBall('blue', 14)
b = BowlingBall('grey')
c = BowlingBall(
    weight = 20,
    color  = 'white'
)

print_bb_info(a)
print_bb_info(b)
print_bb_info(c)

c.color = 'black'
print_bb_info(c)

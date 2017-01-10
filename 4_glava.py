# 1
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')
# 2
guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1
# 3
for i in [3, 2, 1, 0]:
    print(i)
# 4
number_list = [x for x in range(1, 10, 2)]
print(number_list)
# 5
number_dict = {x: x ** 2 for x in range(10)}
print(number_dict)
# 6
number_set = {x for x in range(10) if x % 2 == 0}
print(number_set)


# 7

# 8

def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())
# 9

def my_range(first=0,	last=10,	step=2):
    number = first
    while number < last:
        yield number
        number += step

for i in my_range():
    print(i)
# 10


def decor(func):

    def new_function(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result

    return new_function


@decor
def add_ints(a, b):
    print(a + b)
    return a + b

add_ints(4, 5)
# 11


class OopsException(Exception):
    pass

try:
    raise OopsException('Caught an oops')
except OopsException as exc:
    print(exc)
# 12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)

# 1
year_list = [x for x in range(1975, 1981)]
print(year_list)
# 2
print(year_list[3])
# 3
print(year_list[len(year_list) - 1])
# 4
things = ['mozzarella', 'salmonella', 'cinderella']
# 5
things[1] = things[1].capitalize()
print(things)
# 6
things[0] = things[0].upper()
print(things)
# 7
things.remove('Salmonella')
print(things)
# 8
surprise = ['Grouncho', 'Chico', 'Harpo']
# 9
surprise[2] = surprise[2].lower()
surprise[2] = surprise[2][::-1]
surprise[2] = surprise[2].capitalize()
print(surprise)
# 10
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f)
# 11
print(e2f['walrus'])
# 12
f2e = dict([(x, y) for y, x in e2f.items()])
print(f2e)
# 13
print(f2e['chien'])
# 14
set_word = set(e2f)
print(set_word)
# 15
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': [], 'emus': []}, 'plants': {}, 'other': {}}
print(life)
# 16
print(life.keys())
# 17
print(life['animals'].keys())
# 18
print(life['animals']['cats'])

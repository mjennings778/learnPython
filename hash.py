s = set()
print(s)

s.add("test")
s.add(2)
s.add(3)
s.add(4)

print(s)

string = 'aaaaaaabbbbbbbbbbbccccccccceeeeeeeee'
sett = set(string)

print(sett)
print(string)


dict = {'thomas': 1, 'steve': 2, 'rob': 3}
print(dict)

for key, val in dict.items():
    print(f'key {key}: val {val}')